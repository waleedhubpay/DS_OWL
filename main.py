import logging
import os
from dotenv import load_dotenv
from src.data_ingestion import fetch_new_data
from src.data_preprocessing import preprocess_data
from src.model_training import train_model
from src.model_output import save_model_output
import schedule, time

# Load environment variables
load_dotenv()

# Set up logging
logger = logging.getLogger(__name__)

def execute():
    # Load configuration settings from environment variables
    db_host = os.environ.get("DB_HOST")
    db_port = int(os.environ.get("DB_PORT"))
    db_username = os.environ.get("DB_USERNAME")
    db_password = os.environ.get("DB_PASSWORD")
    db_name = os.environ.get("DB_NAME")
    data_dir = os.environ.get("DATA_DIR")
    model_dir = os.environ.get("MODEL_DIR")
    output_dir = os.environ.get("OUTPUT_DIR")
    try:
        # Fetch new data
        # data, target = fetch_new_data(db_host, db_port, db_username, db_password, db_name)
        data, target = fetch_new_data()

        # Preprocess the data
        X_train, X_test, y_train, y_test = preprocess_data(data, target)

        # Train the model
        model, train_acc, test_acc = train_model(X_train, X_test, y_train, y_test)

        # Save the model output
        save_model_output(model, train_acc, test_acc)
    except Exception as e:
        logger.exception(f"An error occurred: {e}")

def schedule_iris():
    execute()
    schedule.every().hour.do(execute)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    # Add descriptive comments to the code
    logger.info("Starting the Iris MLOps pipeline.")
    logger.info("Press Ctrl+C to stop the pipeline.")

    # Start the pipeline
    schedule_iris()
