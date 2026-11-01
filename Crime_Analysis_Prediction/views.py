from pathlib import Path
from django.shortcuts import render
from django.http import HttpResponse
from sklearn.linear_model import LinearRegression
import pandas as pd
import category_encoders as ce
import matplotlib.pyplot as plt 
from io import BytesIO
import base64
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from django.template import loader

DATA_FILE = Path(r"F:\College\Khalsa College\Training\Minor Project\Minor Project\Minor Project\Data\States Data 2001-2021.xlsx")

# Load data
data = pd.read_excel(DATA_FILE)


# Filtering the data to include only the relevant crime types
relevant_crimes = ["Murder", "Kidnapping", "Rape", "Theft", "Cheating"]
crime_data = data[data["Crime Type"].isin(relevant_crimes)]

# Encode the "City" feature using TargetEncoder
encoder = ce.TargetEncoder()
crime_data["City"] = encoder.fit_transform(crime_data["City"], crime_data["Total Crimes"])

# Splitting the data into features and target
X = crime_data.drop(["Crime Type", "Total Crimes"], axis=1)
y = crime_data["Crime Type"]


def home(request):
    return render(request, 'Crime_Prediction.html')

def predict_total_crime(request):
    # Get input from user
    City = request.POST.get('City')
    crime_type = request.POST.get('crime_type')
    year = int(request.POST.get('year'))

    if year > 2025:
        return render(request, 'Crime_Prediction.html', {'prediction': "Please enter a year on or before 2025"})

    # Check if input data is already present in dataset
    filtered_data = data[(data['City'] == City) & (data['Crime Type'] == crime_type) & (data['Year'] == year)]
    if not filtered_data.empty:
        prediction = int(filtered_data['Total Crimes'].iloc[0])
    else:
        # Filter data based on user input
        filtered_data = data[(data['City'] == City) & (data['Crime Type'] == crime_type) & (data['Year'] < year) & (data['Year'] <= 2025)]

        # Create X and y arrays
        X = filtered_data[['Year']].values
        y = filtered_data[['Total Crimes']].values

        # Perform linear regression
        regressor = LinearRegression()
        regressor.fit(X, y)

        # Predict crime numbers for the given year
        prediction = int(regressor.predict([[year]]).item())

    # Check for negative predictions
    if prediction < 0:
        return render(request, 'Crime_Prediction.html', {'prediction': f"Expected No Crime would occur in the near future for {crime_type}"})
    else:
        if year<=2021:
            return render(request, 'Crime_Prediction.html', {'prediction': f"Total number of {crime_type} crimes for {City} in {year}: {prediction}"})
        else:
            return render(request, 'Crime_Prediction.html', {'prediction': f"Predicted number of {crime_type} crimes for {City} in {year}: {prediction}"})

def crime_analysis(request):
        # Get input from user
    city = request.POST.get('city')

    # Filter data based on user input
    filtered_data = data[data['City'] == city]

    # Calculate total number of crimes for each year
    total_crimes = filtered_data.groupby('Year')['Total Crimes'].sum()

    # Create line plot
    fig, ax = plt.subplots()
    ax.plot(total_crimes.index, total_crimes.values)
    ax.set_title(f"Total number of crimes in {city}")
    ax.set_xlabel("Year")
    ax.set_ylabel("Total number of crimes")

    # Save plot to buffer
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    # Encode plot image as base64 string
    image_string = base64.b64encode(buffer.read()).decode('utf-8')

    # Render plot in template
    return render(request, 'Crime_analysis.html', {'image': image_string})

def spatial_data_analysis(request):
    return render(request, 'spatial_data_analysis.html')

def about(request):
    return render(request, 'about.html')

def create_line_chart(request):
    return render(request, 'total_crimes.html')