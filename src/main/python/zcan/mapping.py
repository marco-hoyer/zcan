def transform_temperature(value: list) -> float:
    parts = value[0:2]
    return (parts[0] - parts[1]) / 10


def transform_air_volume(value: list) -> float:
    parts = value[0:2]
    return float(parts[0] + parts[1] * 255)


mapping = {
    "00454041": {
        "name": "temperature_inlet_before_recuperator",
        "unit": "°C",
        "transformation": transform_temperature
    },
    "00458041": {
        "name": "temperature_inlet_after_recuperator",
        "unit": "°C",
        "transformation": transform_temperature
    },
    "001E0041": {
        "name": "air_volume_output_ventilator",
        "unit": "m3",
        "transformation": transform_air_volume
    },
    "001DC041": {
        "name": "air_volume_input_ventilator",
        "unit": "m3",
        "transformation": transform_air_volume
    }
}
