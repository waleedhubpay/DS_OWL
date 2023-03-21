import logging
import numpy as np

logger = logging.getLogger(__name__)

def fetch_new_data():
    # Load the iris dataset from a file
    data = np.loadtxt("data/iris/iris.data", delimiter=",", usecols=(0, 1, 2, 3))
    target = np.loadtxt("data/iris/iris.data", delimiter=",", usecols=(4,), dtype=np.str)

    logger.info(f"Fetched {len(data)} records")

    return data, target
