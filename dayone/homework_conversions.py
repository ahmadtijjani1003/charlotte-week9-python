
# Charlotte Projects - Week 9, Class 1
# Python Fundamentals and Engineering Units

# Question 9: First measurement set
well_id = "WELL-001"
pressure_psi = 2500.0
temperature_f = 140.0
sensor_active = True

# Convert pressure from PSI to KPA
pressure_kpa = pressure_psi * 6.894757293

# Convert Fahrenheit to Celsius
temperature_c = (temperature_f - 32) * 5 / 9

print("QUESTION 9")
print(f"Well identifier: {well_id}")
print(f"Pressure: {pressure_kpa:.1f} kPa")
print(f"Temperature: {temperature_c:.1f} °C")
print(f"Sensor status: {'Active' if sensor_active else 'Inactive'}")


# Question 10: Second measurement set
pressure_psi = 3000.0
temperature_f = 32.0

pressure_kpa = pressure_psi * 6.894757293
temperature_c = (temperature_f - 32) * 5 / 9

print("\nQUESTION 10")
print(f"Well identifier: {well_id}")
print(f"Pressure: {pressure_kpa:.1f} kPa")
print(f"Temperature: {temperature_c:.1f} °C")
print(f"Sensor status: {'Active' if sensor_active else 'Inactive'}")


# Question 11: Intentional type mismatch
raw_pressure = "3150"
conversion_factor = 6.894757293

# This line deliberately causes a TypeError.
# pressure_kpa = raw_pressure * conversion_factor

# Correct the error using float()
pressure_kpa = float(raw_pressure) * conversion_factor

print("\nQUESTION 11")
print(f"Converted pressure: {pressure_kpa:.1f} kPa")
