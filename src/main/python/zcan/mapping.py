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
    },
    "0082C042": {
        "name": "0082C042",
        "unit": "unknown",
        "transformation": lambda x: int(x[0])
    },
    "004C4041": {
        "name": "004C4041",
        "unit": "unknown",
        "transformation": lambda x: int(x[0])
    },
    "00384041": {
        "name": "00384041",
        "unit": "unknown",
        "transformation": lambda x: int(x[0])
    },
    "00144041": {
        "name": "00144041",
        "unit": "unknown",
        "transformation": lambda x: int(x[0])
    },
    "00824042": {
        "name": "00824042",
        "unit": "unknown",
        "transformation": lambda x: int(x[0])
    },
    "00810042": {
        "name": "00810042",
        "unit": "unknown",
        "transformation": lambda x: int(x[0])
    },
    "00208041": {
        "name": "00208041",
        "unit": "unknown",
        "transformation": lambda x: int(x[0])
    },
    "00344041": {
        "name": "00344041",
        "unit": "unknown",
        "transformation": lambda x: int(x[0])
    },
    "00370041": {
        "name": "00370041",
        "unit": "unknown",
        "transformation": lambda x: int(x[0])
    },
    "00300041": {
        "name": "00300041",
        "unit": "unknown",
        "transformation": lambda x: int(x[0])
    },
    "00044041": {
        "name": "00044041",
        "unit": "unknown",
        "transformation": lambda x: int(x[0])
    },
    "00204041": {
        "name": "00204041",
        "unit": "unknown",
        "transformation": lambda x: int(x[0])
    },
    "00084041": {
        "name": "00084041",
        "unit": "unknown",
        "transformation": lambda x: int(x[0])
    },
    "00804042": {
        "name": "00804042",
        "unit": "unknown",
        "transformation": lambda x: int(x[0])
    },
    "00644041": {
        "name": "00644041",
        "unit": "unknown",
        "transformation": lambda x: int(x[0])
    },
    "00354041": {
        "name": "00354041",
        "unit": "unknown",
        "transformation": lambda x: int(x[0])
    },
    "001E8041": {
        "name": "001E8041",
        "unit": "unknown",
        "transformation": lambda x: int(x[0])
    },
    "00390041": {
        "name": "00390041",
        "unit": "unknown",
        "transformation": lambda x: int(x[0])
    },

    "0035C041": {
        "name": "0035C041",
        "unit": "unknown",
        "transformation": lambda x: int(x[0])
    },

    "0044C041": {
        "name": "0044C041",
        "unit": "unknown",
        "transformation": lambda x: int(x[0])
    },

    "0080C042": {
        "name": "0080C042",
        "unit": "unknown",
        "transformation": lambda x: int(x[0])
    },

    "000E0041": {
        "name": "000E0041",
        "unit": "unknown",
        "transformation": lambda x: int(x[0])
    },

    "00604041": {
        "name": "00604041",
        "unit": "unknown",
        "transformation": lambda x: int(x[0])
    },

    "00450041": {
        "name": "00450041",
        "unit": "unknown",
        "transformation": lambda x: int(x[0])
    },

    "00378041": {
        "name": "00378041",
        "unit": "unknown",
        "transformation": lambda x: int(x[0])
    },

    "00818042": {
        "name": "00818042",
        "unit": "unknown",
        "transformation": lambda x: int(x[0])
    },

    "00820042": {
        "name": "00820042",
        "unit": "unknown",
        "transformation": lambda x: int(x[0])
    },

    "001D0041": {
        "name": "001D0041",
        "unit": "unknown",
        "transformation": lambda x: int(x[0])
    },

    "00490041": {
        "name": "00490041",
        "unit": "unknown",
        "transformation": lambda x: int(x[0])
    },

    "00350041": {
        "name": "00350041",
        "unit": "unknown",
        "transformation": lambda x: int(x[0])
    },

    "10000002": {
        "name": "10000002",
        "unit": "unknown",
        "transformation": lambda x: int(x[0])
    },

    "0081C042": {
        "name": "0081C042",
        "unit": "unknown",
        "transformation": lambda x: int(x[0])
    },

    "00448041": {
        "name": "00448041",
        "unit": "unknown",
        "transformation": lambda x: int(x[0])
    },

    "00560041": {
        "name": "00560041",
        "unit": "unknown",
        "transformation": lambda x: int(x[0])
    },

    "00374041": {
        "name": "00374041",
        "unit": "unknown",
        "transformation": lambda x: int(x[0])
    },

    "00808042": {
        "name": "00808042",
        "unit": "unknown",
        "transformation": lambda x: int(x[0])
    },

    "00040041": {
        "name": "00040041",
        "unit": "unknown",
        "transformation": lambda x: int(x[0])
    },

    "10040001": {
        "name": "10040001",
        "unit": "unknown",
        "transformation": lambda x: int(x[0])
    },

    "00120041": {
        "name": "00120041",
        "unit": "unknown",
        "transformation": lambda x: int(x[0])
    },

    "00688041": {
        "name": "00688041",
        "unit": "unknown",
        "transformation": lambda x: int(x[0])
    },

    "00358041": {
        "name": "00358041",
        "unit": "unknown",
        "transformation": lambda x: int(x[0])
    },

    "00104041": {
        "name": "00104041",
        "unit": "unknown",
        "transformation": lambda x: int(x[0])
    },

    "001E4041": {
        "name": "001E4041",
        "unit": "unknown",
        "transformation": lambda x: int(x[0])
    },

    "00544041": {
        "name": "00544041",
        "unit": "unknown",
        "transformation": lambda x: int(x[0])
    },

    "00498041": {
        "name": "00498041",
        "unit": "unknown",
        "transformation": lambda x: int(x[0])
    },

    "00814042": {
        "name": "00814042",
        "unit": "unknown",
        "transformation": lambda x: int(x[0])
    },

    "000C4041": {
        "name": "000C4041",
        "unit": "unknown",
        "transformation": lambda x: int(x[0])
    },

    "00828042": {
        "name": "00828042",
        "unit": "unknown",
        "transformation": lambda x: int(x[0])
    },

    "10000001": {
        "name": "10000001",
        "unit": "unknown",
        "transformation": lambda x: int(x[0])
    },

    "00494041": {
        "name": "00494041",
        "unit": "unknown",
        "transformation": lambda x: int(x[0])
    },

    "004C8041": {
        "name": "004C8041",
        "unit": "unknown",
        "transformation": lambda x: int(x[0])
    },

    "00388041": {
        "name": "00388041",
        "unit": "unknown",
        "transformation": lambda x: int(x[0])
    }
}
