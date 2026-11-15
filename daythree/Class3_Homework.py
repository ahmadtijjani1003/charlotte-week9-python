
"""
Week 9 - Class 3 Homework
Temperature Conversion and Decision Logic
"""

# Function to convert Fahrenheit to Celsius
def temperature_f_to_c(temp_f):
    return (temp_f - 32) * 5 / 9


# Function to classify temperature readings
def temperature_label(temp_f):
    if temp_f is None or temp_f < -459.67:
        return "invalid"
    elif temp_f >= 212:
        return "hot"
    elif temp_f >= 68:
        return "moderate"
    else:
        return "cool"


# Main program
temperatures = [32, 68, 212, None, -500]

print("Temperature Conversions:")

# Demonstrate temperature conversions
for temp in [32, 68, 212]:
    celsius = temperature_f_to_c(temp)
    print(f"{temp} F = {celsius:.1f} C")


print("\nTemperature Labels:")

valid_celsius = []

# Loop through all temperature readings
for temp in temperatures:

    label = temperature_label(temp)

    if label == "invalid":
        print(f"Reading {temp}: {label}")
        continue

    celsius = temperature_f_to_c(temp)
    valid_celsius.append(celsius)

    print(f"Reading {temp} F: {label} ({celsius:.1f} C)")


# Calculate mean Celsius temperature
if valid_celsius:
    mean_celsius = sum(valid_celsius) / len(valid_celsius)
    print(f"\nMean valid temperature: {mean_celsius:.1f} C")
else:
    print("No valid temperature readings.")

