# Temperature Classifier: Using a function, write a Python script that takes a temperature as input and classifies it into the 
# following categories:

def classify_temperature(temperature):
    """Classify the temperature into categories."""
    if temperature < 0:
        return "Freezing"
    elif 0 <= temperature <= 10:
        return "Cold"
    elif 11 <= temperature <= 20:
        return "Moderate"
    elif 21 <= temperature <= 30:
        return "Warm"
    else:
        return "Hot"


temp = float(input("Enter the temperature in °C: "))
classification = classify_temperature(temp)
print(f"The temperature is classified as: {classification}")


# ii)
# The volume of a sphere with radius r is (4/3)*pie*r**2. What is the volume of the sphere with radius 8. 
# Use a function and make sure the radius is entered from the keyboard and provide the answer in 1 decimal place

import math

def calculate_sphere_volume(radius):
    """Calculate the volume of a sphere given its radius."""
    volume = (4/3) * math.pi * (radius ** 3)
    return volume

# Get radius input from the user
radius = float(input("Enter the radius of the sphere: "))
sphere_volume = calculate_sphere_volume(radius)
print(f"The volume of the sphere with radius {radius} is: {sphere_volume:.1f} cubic units")

