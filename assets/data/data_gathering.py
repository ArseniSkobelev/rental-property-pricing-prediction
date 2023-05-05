from pprint import pprint
import unicodedata
from bs4 import BeautifulSoup
import numpy
import requests


class Property:
    area_sqm = 0
    bedrooms = 0
    monthly_price = 0
    deposit = 0
    url = ""

    def __init__(self, area_sqm, bedrooms, monthly_price, deposit):
        self.area_sqm = area_sqm
        self.bedrooms = bedrooms
        self.monthly_price = monthly_price
        self.deposit = deposit

    def __init__(self) -> None:
        self.area_sqm = 0

    def __str__(self) -> str:
        return f'Area in square meters: {self.area_sqm}\nAmount of bedrooms: {self.bedrooms}\nMonthly price in NOK: {self.monthly_price}\nDeposit: {self.deposit}'


def main():
    found_properties = []

    for i in range(1, 9):
        param = "" if i == 1 else "&page=2" if i == 2 else "&page=3" if i == 3 else "&page=4" if i == 4 else "&page=5" if i == 5 else "&page=6" if i == 6 else "&page=7" if i == 7 else "&page=8"
        current_url = f"https://www.finn.no/realestate/lettings/search.html?location=0.20061{param}&sort=PUBLISHED_DESC"

        response = requests.get(current_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        listings = soup.find('div', {'class': "ads"}).find_all(
            'div', {'class': 'f-card'})

        for listing in listings:
            listing_link = listing.find('a').get('href')

            current_property = Property()

            current_property.url = listing_link

            listing_response = requests.get(listing_link)

            listing_soup = BeautifulSoup(listing_response.text, 'html.parser')

            listing_key_info_element = listing_soup.find(
                'section', {'data-testid': 'key-info'})

            try:
                listing_sqm = listing_key_info_element.find('dl').find(
                    'div', {'data-testid': 'info-usable-area'}).find('dd').text.split(' ')[0]
                current_property.area_sqm = listing_sqm
            except:
                try:
                    listing_sqm = listing_key_info_element.find('dl').find(
                        'div', {'data-testid': 'info-primary-area'}).find('dd').text.split(' ')[0]
                    current_property.area_sqm = listing_sqm
                except:
                    pass

            try:
                listing_bedrooms = listing_key_info_element.find('dl').find(
                    'div', {'data-testid': 'info-bedrooms'}).find('dd').text
                current_property.bedrooms = listing_bedrooms
            except:
                pass

            try:
                listing_pricing_details_element = listing_soup.find(
                    'section', {'data-testid': 'pricing-details'})
                listing_monthly_price = listing_pricing_details_element.find('dl').find(
                    'div', {'data-testid': 'pricing-common-monthly-cost'}).find('dd').text.split(' ')[0].replace('&nbsp;', '')
                current_property.monthly_price = unicodedata.normalize('NFKD', listing_monthly_price.replace(
                    ',–', '')).replace(' ', '')
            except:
                pass

            try:
                listing_deposit = listing_pricing_details_element.find('dl').find(
                    'div', {'data-testid': 'pricing-deposit'}).find('dd').text.split(' ')[0].replace('&nbsp;', '')
                current_property.deposit = unicodedata.normalize('NFKD', listing_deposit.replace(
                    ',–', '')).replace(' ', '')
            except:
                current_property.deposit = int(
                    current_property.monthly_price) * 3

            if current_property.deposit == 0:
                current_property.deposit == int(
                    current_property.monthly_price) * 3

            found_properties.append(current_property)

    with open('rentals.csv', 'w') as f:
        for x in found_properties:
            f.write(
                f'{x.area_sqm},{x.bedrooms},{x.monthly_price},{x.deposit},{x.url}\n')


if __name__ == "__main__":
    main()
