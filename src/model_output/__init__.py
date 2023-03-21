import joblib
import os, datetime

def save_model_output(model, train_acc, test_acc):
    # Save the model accuracy to disk
    with open(os.path.join("data","output", "model_accuracy.txt"), "a+") as f:
        f.write(f"time: {datetime.datetime.now()}\n")
        f.write(f"Training accuracy: {train_acc}\n")
        f.write(f"Testing accuracy: {test_acc}\n\n\n")
