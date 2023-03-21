import os
import logging
from src.data_ingestion import fetch_new_data
from src.data_preprocessing import preprocess_data
from src.model_training import train_model
from src.model_output import save_model_output

# Set up logging
logging.basicConfig(level=logging.INFO)

def main():
    # Load configuration settings
    db_host = os.environ.get("DB_HOST")
    db_port = os.environ.get("DB_PORT")
    db_username = os.environ.get("DB_USERNAME")
    db_password = os.environ.get("DB_PASSWORD")
    db_name = os.environ.get("DB_NAME")
    data_dir = os.environ.get("DATA_DIR")
    model_dir = os.environ.get("MODEL_DIR")
    output_dir = os.environ.get("OUTPUT_DIR")

    # Fetch new data
    # data, target = fetch_new_data(db_host, db_port, db_username, db_password, db_name)
    data, target = fetch_new_data()

    # Preprocess the data
    X_train, X_test, y_train, y_test = preprocess_data(data, target)

    # Train the model
    model, train_acc, test_acc = train_model(X_train, X_test, y_train, y_test)

    # Save the model output
    save_model_output(model, train_acc, test_acc)


if __name__ == "__main__":
    main()
