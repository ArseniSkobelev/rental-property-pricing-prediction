<div align="center">
<h1>Predicting rental property pricing based on a multiple linear regression model</h1>
</div>

### Introduction

The motivation for this project was to dive slightly below the surface level on a topic with such a widespread of information and knowledge as **AI.** My goal was to ensure that my recently acquired knowledge on the **artificial intelligence** and **machine learning** basics _([Introduction to AI](https://course.elementsofai.com/) and [Building AI](https://buildingai.elementsofai.com/) course curriculum provided by [Elements of AI](https://www.elementsofai.com/))_ wouldn't go to waste in the never ending pit of new technologies and concepts that I am invested in. This article may _(or may not)_ include some technical information represented with either _code blocks_ or screenshots. Those of you whom are less engaged in the technical side of things may skip those visual representations.

_P.S The training data for the model was gathered in **May, 2023** and will most likely never get updated. Please be critical to the numbers that you are seeing/reading._

<br />

As I quickly understood, a one-of project with some kind of publically available dataset wouldn't do it to staple the knowledge once and for all _(or atleast the nearest future)._ I had to improvise and find a problem that at the same time was interesting for me and that I could solve quickly.
<br />
Another goal for the project was to ensure that the dataset it was based upon was gathered fully by me (me as in **Python** and **Beautiful Soup 4**).

<br />

### The problem in question

Even before the course curriculum was fully embraced by me, I've started planning and noting down some of the ideas and possible features that I wanted to implement. I knew that my current field of education _(Web development)_ would slightly help me to achieve the goal I wanted; Create a service/micro-frontend that allows a person to predict the **monthly value of their rental property.** The implementation had to be simple yet functional and on the frontend and ~~good~~ _functional_ on the backend.

<br />

Unfortunately, the project scale restricted me early and defined its boundaries as following; <br/>

- _1 cities_ worth of rental property data _(Oslo, Norway)_
- ~400 entries in the dataset

This meant that the model would not be able to compete with any proffesional rental property brokers or even be a helpful tool for them to use. The goal was to get an approximate and ensure that the newly predicted data could be tracked down in the dataset and confirmed to an extent of accuracy.

<br />

### Performance

\- _Speaking of accuracy, how does it perform?_ <br />
This is the part of the project which I was less excited about because of the earlier mentioned reasons. If the [R-Squared](https://en.wikipedia.org/wiki/Coefficient_of_determination) proportion or the _coefficient of determination_ value is something that seems respectable in your eyes:

```py3
def gather_model_performance_data(model):
    # Gather the predictions of our model
    model_predictions = model.predict(feature_test_data)

    # Get the r-squared proportion of the model and present it
    print(r2_score(value_test_data, model_predictions))
```

```py3
# lr = sklearn.linear_model.LinearRegression().fit(X_train_data, y_train_data)
>>> gather_model_performance_data(lr)
0.6363826621317836
```
