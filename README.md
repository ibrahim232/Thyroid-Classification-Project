# Thyroid Disease Prediction

## Background

The Thyroid Disease dataset consists of information on 3,772 patients from two medical centers in Germany. It targets individuals diagnosed with thyroid disease, encompassing a variety of details such as demographic data, thyroid hormone levels, and diagnostic information. The main objective is to forecast the presence and type of thyroid disease in a patient.

## Problem Statement

The aim is to develop a classification model that accurately predicts the type of thyroid disease (hypothyroidism, hyperthyroidism, or euthyroidism) a person has, based on a range of features.

## Dataset Features

The dataset includes the following attributes:

- **Age** (Numeric): Age of the patient.
- **Sex** (Categorical): Sex of the patient (M or F).
- **On_thyroxine** (Categorical): Indicates if the patient is on thyroxine treatment (f or t).
- **Query_on_thyroxine** (Categorical): Indicates if the patient has queries about thyroxine treatment (f or t).
- **On_antithyroid_medication** (Categorical): Indicates if the patient is on antithyroid medication (f or t).
- (Additional features continue in the same structure)
- **TBG** (Numeric): Level of thyroxine-binding globulin in the patient's blood.

## Methodology

1. **Importing Libraries**: Initial step involves importing essential libraries for data manipulation, visualization, preprocessing, and modeling.
2. **Data Cleaning & Preprocessing**: This step covers cleaning and preprocessing the dataset for analysis, which includes handling missing values and converting data types.
3. **Exploratory Data Analysis (EDA)**: In this phase, the data is analyzed to gain a better understanding through univariate, bivariate, and multivariate analysis.
4. **Data Encoding and Scaling**: This process involves encoding categorical variables and scaling numerical features to prepare the data for modeling.
5. **Data Modeling**: Describes building the classification model, including selecting model types, the training process, and any hyperparameter tuning that was conducted.
6. **Model Evaluation**: Details the methods used to evaluate the model's performance, such as accuracy, precision, recall, and F1-score, and discusses the outcomes.

## Potential Challenges and Solutions

- **Differentiating the classes of thyroid diseases**: Advanced machine learning techniques, like RandomForest and Gradient boosting.
- **Overcoming the extreme imbalance in the target variable**: Using techniques like ADASYN from imbalanced-learn and TomekLinks for under-sampling.
- **Patient Safety**: Adding awareness messages to help patients.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to have Anaconda distribution installed to create virtual environments and manage packages. You can download it from [here](https://www.anaconda.com/products/distribution).

### Setting Up

1. **Clone the repository**: Open your terminal and clone this repository by running:
git clone https://github.com/ibrahim232/Thyroid-Classification-Project.git

2. **Create a Conda virtual environment**: Navigate into the cloned project directory and create a new Conda environment by running:
cd Thyroid-Classification-Project
conda create --name env_name python=3.x

Replace `env_name` with your preferred name for the virtual environment, and `3.x` with your preferred Python version (e.g., 3.7).

3. **Activate the virtual environment**: Activate the created virtual environment by running:
conda activate env_name

Replace `env_name` with the name of the virtual environment you created.

4. **Install required packages**: Install the required packages by running:
conda install imbalanced-learn==0.12.0 joblib==1.2.0 pandas==2.0.3 plotly==5.9.0 scikit-learn==1.3.0 streamlit==1.31.1
conda install --channel=conda-forge --name=base conda-libmamba-solver


### Running the Notebook

Follow the instructions in the notebook to run the cells and perform the analysis.

### Streamlit App

You can also run the Streamlit app to simulate and show the results. To do so, follow these steps:

1. **Install Streamlit**: Install Streamlit by running:
pip install streamlit.
or
conda install -c conda-forge streamlit.

2. **Run the Streamlit app**: Navigate to the project directory and run the Streamlit app by running:
streamlit run app.py

You will enter the parameters and get the prediction.

## Built With

- Python
- Jupyter Notebook
- Pandas
- Numpy
- Matplotlib
- Seaborn
- Scikit-Learn
- Plotly
- SciPy

## Author

[Ibrahim Abdelnasr Yakout](https://github.com/ibrahim232)



