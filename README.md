# Crime Data Analysis and Prediction

This project is a Django-based crime data analysis and prediction system built for academic and project demonstration purposes.

## Project Overview
The application analyzes crime data and predicts total crime counts for a selected city and year using a linear regression model. It also provides basic crime analysis views and visualization support.

## Software Used

### 1. Python
Python was used as the main programming language for data processing, machine learning, and backend logic.

### 2. Django
Django was used to build the web application, handle routing, render templates, and process the prediction form submissions.

### 3. Pandas
Pandas was used to read and manipulate Excel datasets, filter rows, group records, and prepare data for analysis and modeling.

### 4. scikit-learn
scikit-learn was used to build the machine learning model, especially the LinearRegression model used to predict crime counts based on historical year-wise trends.

### 5. category_encoders
This library was used to encode categorical values such as city names before analysis or model preparation when needed.

### 6. Matplotlib
Matplotlib was used to generate plots and charts for crime trend visualization and analysis.

### 7. OpenPyXL
OpenPyXL was used to allow pandas to read Excel files (.xlsx) correctly.

## Dependencies and Their Roles

- Django: Web framework for the application and routes
- pandas: Data loading and preprocessing
- scikit-learn: prediction model implementation
- category_encoders: categorical encoding for non-numeric fields
- matplotlib: chart creation and visualization
- openpyxl: Excel file reading support

## Project Structure

- `manage.py` — Django project entry point
- `Crime_Prediction/` — project settings and configuration
- `Crime_Analysis_Prediction/` — main app logic, views, and templates
- `Data/` — project dataset files used for analysis and prediction

## Setup Instructions

1. Create a virtual environment

```bash
python -m venv .venv
```

2. Activate the environment

On Windows:

```bash
.venv\Scripts\activate
```

3. Install dependencies

```bash
pip install Django==4.1.7 pandas category_encoders matplotlib openpyxl scikit-learn
```

4. Run the project

```bash
python manage.py runserver
```

5. Open the app in the browser:

```text
http://127.0.0.1:8000/
```

## Important Note on Figures and Statistics
This project is developed for educational, academic, and demonstration purposes only. The predictions, charts, and output values should not be treated as official government or institutional statistics. They are based on sample/project data and model estimations, and may not reflect real-world official crime figures.

## Disclaimer
The project is intended for learning, experimentation, and academic demonstration. It should not be used for official reporting, legal decisions, or public policy claims without valid and verified official data sources.
