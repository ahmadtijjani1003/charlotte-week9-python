
# CHARLOTTE PROJECTS - WEEK 9, CLASS 1
# Student Lab: Python Fundamentals and Telemetry Calculations

# Activity B: Store raw sensor values as strings first.
well_id = "WELL-07"
raw_pressure = "3150.0"
raw_temperature = "186.0"
sensor_active = True

# Convert raw sensor strings to numeric floats.
pressure_psi = float(raw_pressure)
temperature_f = float(raw_temperature)

# Activity C: Convert pressure from psi to kPa.
pressure_kpa = pressure_psi * 6.8947572932

# Convert temperature from Fahrenheit to Celsius.
temperature_c = (temperature_f - 32) * 5 / 9

# Activity D: Generate a clear telemetry report.
sensor_status = "Active" if sensor_active else "Inactive"

print("WELL TELEMETRY REPORT")
print(f"Well identifier: {well_id}")
print(f"Pressure: {pressure_kpa:.1f} kPa")
print(f"Temperature: {temperature_c:.1f} °C")
print(f"Sensor status: {sensor_status}")


# INDEPENDENT STRETCH EXERCISE
# Change the values below when practising.

# well_id = "WELL-08"
# pressure_psi = 2800.0
# temperature_f = 122.0

# pressure_kpa = pressure_psi * 6.8947572932
# temperature_c = (temperature_f - 32) * 5 / 9

# print(f"Well identifier: {well_id}")
# print(f"Pressure: {pressure_kpa:.1f} kPa")
# print(f"Temperature: {temperature_c:.1f} °C")
