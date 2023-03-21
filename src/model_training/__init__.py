from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import joblib

def train_model(X_train, X_test, y_train, y_test):
    # Train a support vector machine model
    model = SVC(kernel="linear", C=1)
    model.fit(X_train, y_train)

    # Calculate the training and testing accuracy
    train_acc = accuracy_score(y_train, model.predict(X_train))
    test_acc = accuracy_score(y_test, model.predict(X_test))

    # Save the trained model to disk
    joblib.dump(model, "data/output/model.pkl")

    return model, train_acc, test_acc