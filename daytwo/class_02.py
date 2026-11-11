

# 1. CREATE EIGHT OBSERVATION DICTIONARIES

observations = [
    {
        "well_id": "WELL-07",
        "pressure_psi": 3150.0,
        "temperature_f": 186.0,
        "sensor_active": True
    },
    {
        "well_id": "WELL-08",
        "pressure_psi": 2800.0,
        "temperature_f": 122.0,
        "sensor_active": True
    },
    {
        "well_id": "WELL-07",
        "pressure_psi": 3200.0,
        "temperature_f": 190.0,
        "sensor_active": True
    },
    {
        "well_id": "WELL-09",
        "pressure_psi": 2950.0,
        "temperature_f": 150.0,
        "sensor_active": False
    },
    {
        "well_id": "WELL-08",
        "pressure_psi": 2850.0,
        "temperature_f": 130.0,
        "sensor_active": True
    },
    {
        "well_id": "WELL-10",
        "pressure_psi": 3100.0,
        "temperature_f": 175.0,
        "sensor_active": True
    },
    {
        "well_id": "WELL-07",
        "pressure_psi": 3300.0,
        "temperature_f": 195.0,
        "sensor_active": True
    },
    {
        "well_id": "WELL-08",
        "pressure_psi": 2900.0,
        "temperature_f": 140.0,
        "sensor_active": False
    }
]


# 2. DISPLAY THE TWO EARLIEST OBSERVATIONS AND LAST RECORD

print("=" * 55)
print("OBSERVATION RECORDS")
print("=" * 55)

print("\nFirst two observations:")

for observation in observations[:2]:
    print(observation)

print("\nLast observation:")
print(observations[-1])

# 3. DISPLAY SORTED DISTINCT WELL IDs

print("\n" + "=" * 55)
print("DISTINCT WELL IDs")
print("=" * 55)

well_ids = sorted({
    observation["well_id"]
    for observation in observations
})

for well_id in well_ids:
    print(well_id)


# 4. DISPLAY DISTINCT DICTIONARY FIELDS

print("\n" + "=" * 55)
print("DISTINCT OBSERVATION FIELDS")
print("=" * 55)

fields = sorted({
    field
    for observation in observations
    for field in observation.keys()
})

for field in fields:
    print(field)

# 5. CALCULATE TOTAL AND MEAN PRESSURE

print("\n" + "=" * 55)
print("PRESSURE ANALYSIS")
print("=" * 55)

pressure_readings = [
    float(observation["pressure_psi"])
    for observation in observations
    if observation.get("pressure_psi") is not None
]

total_pressure = sum(pressure_readings)

if pressure_readings:
    mean_pressure = total_pressure / len(pressure_readings)
else:
    mean_pressure = 0.0

print(f"Total pressure: {total_pressure:.2f} psi")
print(f"Mean pressure: {mean_pressure:.2f} psi")

# 6. COUNT OBSERVATIONS PER WELL

print("\n" + "=" * 55)
print("OBSERVATIONS PER WELL")
print("=" * 55)

observations_per_well = {}

for observation in observations:

    well_id = observation["well_id"]

    observations_per_well[well_id] = (
        observations_per_well.get(well_id, 0) + 1
    )

for well_id, count in sorted(observations_per_well.items()):
    print(f"{well_id}: {count} observations")


# 7. DISPLAY FINAL TELEMETRY SUMMARY

print("\n" + "=" * 55)
print("TELEMETRY SUMMARY")
print("=" * 55)

print(f"Total observations: {len(observations)}")
print(f"Unique wells: {len(well_ids)}")
print(f"Total distinct fields: {len(fields)}")

print("\nAnalysis completed successfully.")
