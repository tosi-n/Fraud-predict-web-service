Fraud-predict-web-service
================
Tosin Dairo
MAY 13, 2020

Web API for predicting fraud claims from data trained and evaluated on a
Decision Tree Classifier. The data used for training is an [Auto
Insurance Claims
Data](https://www.kaggle.com/roshansharma/insurance-claim) sourced from
kaggle. The data consist of 39 datapots and 1000 observations. In order
to effectively select a classifier model for a prediction service,
multiple machine learning algorithms are trained to achieve a binary
prediction output. After evalution of the 6 trained predictive model,
the most efficient model was serialized and deployed for production
ready prediction service.

![Predictive API
Endpoints](MISC/API_test.png)

#### Trained Machine Learning Algorithms

  - Logistic Regression
  - K Nearest Neighbor
  - Decision Tree
  - Random Forest
  - Linear Discriminant Analysis
  - Support Vector Machine

#### Requirements

Python 3 or 3.6

#### Setup

With VENV Create a new virtual environment and install packages.

    virtualenv -p python3 venv

    source ./venv/bin/activate

Install requirements

    pip3 install requirements.txt

#### Usage

Model training can be done from notebook with sufficient documentation,
which can be found in
[fraud\_claim.ipynb](https://github.com/tosi-n/Fraud-predict-web-service/blob/master/src/fraud_claim.ipynb)
link.

> Trained and selected Decision Tree model is saved as a pickle
> serialized file found in directory /src/model\_weight/

In order to effectively evaluate the predictive model a calibration and
discrimination technique is applied. The figure below shows a ROC Curve
with Decision Tree Classifier having an AUC value of 0.71 which is
slightly above 0.5. This means that the Decision Tree Classifier has
sufficient information for predicting fraud claims. ![ROC
Curve](MISC/model_performance.png)

Run API using Django rest framework

    ./manage.py createsuperuser
    
    ./manage.py runserver

In order to test API prediction endpoints, an API client application
like [Postman](https://www.postman.com/) can be used on local host to
make predictions on endpoints.

<hr>

</hr>

#### Challenges

  - Data missingness required the use of a Multiple Imputation by
    Chained Equations package for imputing missing data
  - Data for prediction had imbalanced class. This was dealt with using
    oversampling techniques for minority class using the SMOTE package
  - Model metrics can be improved for better discrimination by training
    model on more data samples for fraud prediction
