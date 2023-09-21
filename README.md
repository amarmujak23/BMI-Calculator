# BMI-Calculator
Basic BMI (Body Mass Index)  Calculator
This program calculates and displays a person's Body Mass Index (BMI) based on their weight and height input. Here's a step-by-step explanation of what the program does:

It defines four constants representing BMI thresholds:

underweight_upper_limit: This is set to 18.5, indicating the upper limit of the underweight BMI range.
healthy_lower_limit: This is also set to 18.5, indicating the lower limit of the healthy BMI range.
healthy_upper_limit: This is set to 24.9, indicating the upper limit of the healthy BMI range.
overweight_upper_limit: This is set to 29.9, indicating the upper limit of the overweight BMI range.
It prompts the user to input their weight in any unit (e.g., pounds or kilograms). The program then converts the weight input to kilograms by multiplying it by the conversion factor 0.45359237.

It prompts the user to input their height in two parts: feet and inches. 
The program converts these inputs into a single height value in meters. 
It does this by converting feet to meters using the conversion factor 0.3048 (since 1 foot = 0.3048 meters) and converting inches to meters using the conversion factor 0.0254 (since 1 inch = 0.0254 meters). 
The two converted values are then added together to get the height in meters.

It calculates the BMI using the formula for BMI:
BMI = (weight in kilograms) / (height in meters)^2

It prints the calculated BMI with three decimal places, displaying the result to the user.

In summary, this program takes user input for weight (in any unit), height (in feet and inches), and then calculates the BMI using the provided formula. 
It then displays the BMI with three decimal places and can be used to categorize the BMI based on the predefined threshold values for underweight, healthy, and overweight ranges.
