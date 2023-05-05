import math
from sklearn.model_selection import train_test_split
import pandas as pd
# from sklearn.linear_model import LinearRegression
import joblib
from flask import Flask, Response, request, jsonify
import traceback

application = Flask(__name__)

# _dataset_file_path = './assets/data/rentals.csv'
_model_file_name = 'rental.pkl'
_model_columns_file_name = 'rental_columns.pkl'
_API_PORT = 9999

# df = pandas.read_csv(_dataset_file_path)

# X = df[['Area in sqm', 'Number of bedrooms']]
# y = df['Monthly price']

# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=.2, random_state=42)

# lr = LinearRegression()
# lr.fit(X_train, y_train)

# joblib.dump(lr, _model_file_name)
# print("[Rental price prediction] Model saved successfully")
# features_columns = list(X_train.columns)
# joblib.dump(features_columns, _model_column_file_name)
# print("[Rental price prediction] Columns saved successfully")


@application.route('/prediction', methods=['POST'])
def predict():
    if lr:
        try:
            json = request.json
            print(json)

            query = pd.get_dummies(pd.DataFrame({'Area in sqm': [
                                   json['Area in sqm']], 'Number of bedrooms': [json['Number of bedrooms']]}))
            query = query.reindex(columns=features_columns, fill_value=0)

            predict = list(lr.predict(query))

            monthly_price_prediction = math.ceil(predict[0])
            monthly_price_prediction -= monthly_price_prediction % -100

            return jsonify({'monthly_price': monthly_price_prediction})
        except Exception as e:
            print(e)
            return jsonify({'message': 'InternalServerError'})


if __name__ == "__main__":
    lr = joblib.load(_model_file_name)
    features_columns = joblib.load(_model_columns_file_name)

    print("[Rental price prediction] Model and columns successfully")

    application.run(port=_API_PORT, debug=True)
