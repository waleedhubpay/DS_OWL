import logging
from src.pipeline_class import Pipeline
import multiprocessing

# Set up logging
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    # Adding descriptive comments to the code
    logger.info("Starting the OWL.")
    logger.info("Press Ctrl+C to stop the pipeline(s).")
    logger.info("For documentation: https://github.com/waleedhubpay/DS_OWL\n")

    # initiate the pipeline(s)
    process_1 = Pipeline()
    process_2 = Pipeline()

    # define the pipeline(s) as Process object(s)
    process_1 = multiprocessing.Process(target=process_1.schedule)
    process_2 = multiprocessing.Process(target=process_2.schedule)

    # Start the processes
    process_1.start()
    process_2.start()

    processes = [process_1, process_2]

    try:
        for process in processes:
            process.join()
    except KeyboardInterrupt:
        logger.info("Terminating Pipelines")
        for process in processes:
            process.terminate()