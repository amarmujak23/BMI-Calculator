underweight_upper_limit = 18.5
healthy_lower_limit = 18.5
healthy_upper_limit = 24.9
overweight_upper_limit = 29.9

#Weight
weight = input("Type in your weight: ")
weight_input = float(weight)
weight_conversion = (weight_input * 0.45359237)

#Height
height_feet = input("Type in your height in feet: ")
height_inch = input("Type in your height in inches: ")

feet_input = int(height_feet)
inch_input = int(height_inch)

feet_to_meters = (feet_input * 0.3048)  #1 foot = 0.3048 meters
inches_meters = (inch_input * 0.0254)  #1 inch = 0.0254 meters
meters_calculation = (feet_to_meters + inches_meters)

bmi_calculation = (weight_conversion / meters_calculation**2)
print("Your BMI Calculation:")
print("%.3f" % bmi_calculation)
