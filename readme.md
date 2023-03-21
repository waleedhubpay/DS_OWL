# DS_OWL - Orchestrated Wisdom Layer

OWL (Orchestrated Wisdom Layer) is an MLOps pipeline designed to streamline the process of fetching new data, updating and re-running models, and saving model outputs. OWL is built using Python and leverages SQLAlchemy for data handling. This repository provides a detailed overview of the code structure and libraries used for implementing OWL.

## Table of Contents

- [DS\_OWL - Orchestrated Wisdom Layer](#ds_owl---orchestrated-wisdom-layer)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Dependencies](#dependencies)
  - [Installation](#installation)
  - [Code Structure](#code-structure)
  - [Usage](#usage)

## Introduction

In today's fast-paced world, machine learning models need to be updated frequently to maintain their accuracy and effectiveness. OWL aims to simplify this process by automating the entire pipeline from data ingestion to model output storage. This ensures that your ML models are always up-to-date and delivering the best possible results.

## Dependencies

The primary dependencies for OWL are:

- Python 3.7+
- SQLAlchemy
- pandas
- numpy
- scikit-learn
- joblib

## Installation

To install OWL and its dependencies, follow these steps:

1. Clone the repository:

```
git clone https://github.com/hubpay/DS_OWL.git
cd OWL
```


2. Create and activate a virtual environment:
```
python3 -m venv venv
source venv/bin/activate
```


3. Install the required packages:
```
pip install -r requirements.txt
```

## Code Structure

The OWL repository is organized as follows:

- `data/`: Directory containing raw and processed data
- `models/`: Directory for storing trained models and their outputs
- `src/`: Contains the source code for the pipeline, organized into subdirectories:
  - `data_ingestion/`: Scripts for fetching new data using SQLAlchemy
  - `data_preprocessing/`: Scripts for cleaning, transforming, and preparing data for ML models
  - `model_training/`: Scripts for training, updating, and evaluating ML models
  - `model_output/`: Scripts for saving model outputs and performance metrics
- `tests/`: Unit tests for various pipeline components
- `config.py`: Configuration settings for the pipeline
- `requirements.txt`: List of required Python packages
- `main.py`: Main script that ties the pipeline together

## Usage

To run the OWL pipeline, execute the following command:


