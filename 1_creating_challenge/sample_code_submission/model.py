"""This file is for patches classification (step 1).

Sample predictive model.
You must supply at least 4 methods:
- fit: trains the model.
- predict: uses the model to perform predictions.
"""
from sklearn.base import BaseEstimator

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import Activation, Dropout, Flatten, Dense

class Model(BaseEstimator):
    """Main class for Classification problem."""

    def __init__(self):
        """Init method.

        We define here a simple (shallow) CNN.
        """
        self.is_trained = False

        self.model = Sequential()

        self.model.add(Conv2D(32, (3, 3), input_shape=(40, 40, 3)))
        self.model.add(Activation('relu'))
        self.model.add(MaxPooling2D(pool_size=(2, 2)))

        self.model.add(Flatten())
        self.model.add(Dense(16))

        self.model.add(Activation('relu'))
        self.model.add(Dropout(0.1))
        self.model.add(Dense(1))
        self.model.add(Activation('sigmoid'))

        self.model.compile(loss='binary_crossentropy', optimizer='rmsprop',
                           metrics=['accuracy'])

    def fit(self, X, y):
        """Fit method.

        This function should train the model parameters.
        Args:
            X: Training data matrix of dim num_train_samples * num_feat.
               An image has the following shape (40, 40, 3) then 4800 features.
            y: Training label matrix of dim num_train_samples.
        Both inputs are numpy arrays.
        """
        self.num_train_samples = X.shape[0]
        X = X.reshape((self.num_train_samples, 40, 40, 3))
        self.model.fit(X / 255, y, epochs=5)
        self.is_trained = True

    def predict(self, X):
        """Predict method.

        Args:
            X: Training data matrix of dim num_train_samples * num_feat.
               An image has the following shape (40, 40, 3) then 4800 features.
        This function should provide predictions of labels on (test) data.
        Make sure that the predicted values are in the correct format for the
        scoring metric. For example, binary classification problems often
        expect predictions in the form of a discriminant value (if the area
        under the ROC curve it the metric) rather that predictions of the class
        labels themselves.
        The function predict eventually can return probabilities.
        """
        num_test_samples = X.shape[0]
        X = X.reshape((num_test_samples, 40, 40, 3))
        return self.model.predict_proba(X / 255)[:, 0]
