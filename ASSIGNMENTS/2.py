

# Define a function named calculate_bmi that takes a person's weight (in kilograms)
# and height (in meters) as parameters and returns their BMI. (BMI = weight/height)
# Calculate and sen their BMI category: 


def calculate_bmi(weight, height):
    """Calculate BMI and return the BMI value and category."""
    bmi = weight / (height ** 2)
    
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"
    
    return bmi, category


weight = 70  # in kilograms
height = 1.75  # in meters
bmi_value, bmi_category = calculate_bmi(weight, height)
print(f"BMI: {bmi_value:.2f}, Category: {bmi_category}")




# ii)
#Use a function to calculate the volume of a cylinder V = π r2 h. Choose a function
# name in line with what you want to 
# achieve. Radius r and height h should be in parameters. Make sure you use the real 
# pie value (import math)


import math

def calculate_cylinder_volume(radius, height):
    """Calculate the volume of a cylinder."""
    volume = math.pi * (radius ** 2) * height
    return volume


radius = 5  # in meters
height = 10  # in meters
cylinder_volume = calculate_cylinder_volume(radius, height)
print(f"Volume of the cylinder: {cylinder_volume:.2f} cubic meters")
