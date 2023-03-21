import logging
from src.pipeline_class import Pipeline

# Set up logging
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    # Adding descriptive comments to the code
    logger.info("Starting the Iris MLOps pipeline.")
    logger.info("Press Ctrl+C to stop the pipeline.")
    logger.info("For documentation: https://github.com/waleedhubpay/DS_OWL\n")

    # initiate the pipeline(s)
    iris = Pipeline()

    # schedule the pipeline(s)
    iris.schedule()
