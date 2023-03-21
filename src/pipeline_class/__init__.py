import logging
import os
from dotenv import load_dotenv
from src.data_ingestion import fetch_new_data
from src.data_preprocessing import preprocess_data
from src.model_training import train_model
from src.model_output import save_model_output
import schedule, time

# Set up logging
logger = logging.getLogger(__name__)

class Pipeline:
    def __init__(self):
        # Load environment variables
        load_dotenv()

        self.db_host = os.environ.get("DB_HOST")
        self.db_port = int(os.environ.get("DB_PORT"))
        self.db_username = os.environ.get("DB_USERNAME")
        self.db_password = os.environ.get("DB_PASSWORD")
        self.db_name = os.environ.get("DB_NAME")
        self.data_dir = os.environ.get("DATA_DIR")
        self.model_dir = os.environ.get("MODEL_DIR")
        self.output_dir = os.environ.get("OUTPUT_DIR")

    def execute(self):
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

    def schedule(self):
        self.execute()
        schedule.every().hour.do(self.execute)
        while True:
            schedule.run_pending()
            time.sleep(1)
