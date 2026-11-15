pressure_readings_list = [3150, 2780, 3040, 3180, 2510,2815]

temperature_readings_tuple = (186, 172, 195, 180, 187, 166)

sensor_active_set = [True, False]

well_readings = {
    "pressure": pressure_readings_list,
    "temperature": temperature_readings_tuple,
    "sensor_active": sensor_active_set
}
print("Well readings dictionary:", well_readings)

#indexing
print("pressure reading:", well_readings["pressure"][0])
print("temperature reading:", well_readings["temperature"][4])
print("sensor active status:", well_readings["sensor_active"][1])