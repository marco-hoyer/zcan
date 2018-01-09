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
        "name": "air_volume_input_ventilator",
        "unit": "m3",
        "transformation": transform_air_volume
    },
    "001DC041": {
        "name": "air_volume_output_ventilator",
        "unit": "m3",
        "transformation": transform_air_volume
    },
    "00488041": {
        "name": "air_humidity_outlet_before_recuperator",
        "unit": "%",
        "transformation": lambda x: int(x[0])
    },
    "0048C041": {
        "name": "air_humidity_inlet_before_recuperator",
        "unit": "%",
        "transformation": lambda x: int(x[0])
    },
    "00200041": {
        "name": "total_power_consumption",
        "unit": "W",
        "transformation": lambda x: int(x[0])
    },
    "001D4041": {
        "name": "power_percent_output_ventilator",
        "unit": "%",
        "transformation": lambda x: int(x[0])
    },
    "001D8041": {
        "name": "power_percent_input_ventilator",
        "unit": "%",
        "transformation": lambda x: int(x[0])
    }
}
