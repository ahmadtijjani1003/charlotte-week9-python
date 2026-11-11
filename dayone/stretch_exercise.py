# INDEPENDENT STRETCH EXERCISE - WELL-08

well_id = "WELL-08"
pressure_psi = 2800.0
temperature_f = 122.0

# Convert pressure from PSI to kPa
pressure_kpa = pressure_psi * 6.8947572932

# Convert temperature from Fahrenheit to Celsius
temperature_c = (temperature_f - 32) * 5 / 9

# Display the results
print("WELL TELEMETRY REPORT")
print(f"Well identifier: {well_id}")
print(f"Pressure: {pressure_kpa:.1f} kPa")
print(f"Temperature: {temperature_c:.1f} °C")