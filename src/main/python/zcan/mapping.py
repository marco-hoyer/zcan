def transform_temperature(value: list) -> float:
    parts = value[0:2]
    return (parts[0] - parts[1]) / 10


def transform_air_volume(value: list) -> float:
    parts = value[0:2]
    return float(parts[0] + parts[1] * 255)


mapping = {
    "00148041": {
        "name": "unknown_decreasing_number",
        "unit": "unknown",
        "transformation": lambda x: float(x[0])
    },
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
    "001E8041": {
        "name": "speed_input_ventilator",
        "unit": "rpm",
        "transformation": transform_air_volume
    },
    "001E4041": {
        "name": "speed_output_ventilator",
        "unit": "rpm",
        "transformation": transform_air_volume
    },
    "00488041": {
        "name": "air_humidity_outlet_before_recuperator",
        "unit": "%",
        "transformation": lambda x: float(x[0])
    },
    "0048C041": {
        "name": "air_humidity_inlet_before_recuperator",
        "unit": "%",
        "transformation": lambda x: float(x[0])
    },
    "00200041": {
        "name": "total_power_consumption",
        "unit": "W",
        "transformation": lambda x: float(x[0])
    },
    "001D4041": {
        "name": "power_percent_output_ventilator",
        "unit": "%",
        "transformation": lambda x: float(x[0])
    },
    "001D8041": {
        "name": "power_percent_input_ventilator",
        "unit": "%",
        "transformation": lambda x: float(x[0])
    },
    "0082C042": {
        "name": "0082C042",
        "unit": "unknown",
        "transformation": transform_air_volume
    },
    "004C4041": {
        "name": "004C4041",
        "unit": "unknown",
        "transformation": transform_air_volume
    },
    "00384041": {
        "name": "00384041",
        "unit": "unknown",
        "transformation": lambda x: float(x[0])
    },
    "00144041": {
        "name": "remaining_s_in_currend_ventilation_mode",
        "unit": "s",
        "transformation": transform_air_volume
    },
    "00824042": {
        "name": "00824042",
        "unit": "unknown",
        "transformation": transform_air_volume
    },
    "00810042": {
        "name": "00810042",
        "unit": "unknown",
        "transformation": transform_air_volume
    },
    "00208041": {
        "name": "total_power_consumption",
        "unit": "kWh",
        "transformation": transform_air_volume
    },
    "00344041": {
        "name": "00344041",
        "unit": "unknown",
        "transformation": transform_air_volume
    },
    "00370041": {
        "name": "00370041",
        "unit": "unknown",
        "transformation": transform_air_volume
    },
    "00300041": {
        "name": "days_until_next_filter_change",
        "unit": "days",
        "transformation": transform_air_volume
    },
    "00044041": {
        "name": "00044041",
        "unit": "unknown",
        "transformation": lambda x: float(x[0])
    },
    "00204041": {
        "name": "total_power_consumption_this_year",
        "unit": "kWh",
        "transformation": transform_air_volume
    },
    "00084041": {
        "name": "00084041",
        "unit": "unknown",
        "transformation": lambda x: float(x[0])
    },
    "00804042": {
        "name": "00804042",
        "unit": "unknown",
        "transformation": transform_air_volume
    },
    "00644041": {
        "name": "00644041",
        "unit": "unknown",
        "transformation": lambda x: float(x[0])
    },
    "00354041": {
        "name": "00354041",
        "unit": "unknown",
        "transformation": transform_air_volume
    },
    "00390041": {
        "name": "frost_disbalance",
        "unit": "%",
        "transformation": lambda x: float(x[0])
    },

    "0035C041": {
        "name": "total_power_savings",
        "unit": "kWh",
        "transformation": transform_air_volume
    },

    "0044C041": {
        "name": "0044C041",
        "unit": "unknown",
        "transformation": transform_air_volume
    },

    "0080C042": {
        "name": "0080C042",
        "unit": "unknown",
        "transformation": transform_air_volume
    },

    "000E0041": {
        "name": "000E0041",
        "unit": "unknown",
        "transformation": lambda x: float(x[0])
    },

    "00604041": {
        "name": "00604041",
        "unit": "unknown",
        "transformation": lambda x: float(x[0])
    },

    "00450041": {
        "name": "00450041",
        "unit": "unknown",
        "transformation": transform_air_volume
    },

    "00378041": {
        "name": "00378041",
        "unit": "unknown",
        "transformation": lambda x: float(x[0])
    },

    "00818042": {
        "name": "00818042",
        "unit": "unknown",
        "transformation": lambda x: float(x[0])
    },

    "00820042": {
        "name": "00820042",
        "unit": "unknown",
        "transformation": lambda x: float(x[0])
    },

    "001D0041": {
        "name": "001D0041",
        "unit": "unknown",
        "transformation": lambda x: float(x[0])
    },

    "00490041": {
        "name": "00490041",
        "unit": "unknown",
        "transformation": lambda x: float(x[0])
    },

    "00350041": {
        "name": "00350041",
        "unit": "unknown",
        "transformation": transform_air_volume
    },

    "0081C042": {
        "name": "0081C042",
        "unit": "unknown",
        "transformation": lambda x: float(x[0])
    },

    "00448041": {
        "name": "00448041",
        "unit": "unknown",
        "transformation": lambda x: float(x[0])
    },

    "00560041": {
        "name": "00560041",
        "unit": "unknown",
        "transformation": lambda x: float(x[0])
    },

    "00374041": {
        "name": "00374041",
        "unit": "unknown",
        "transformation": transform_air_volume
    },

    "00808042": {
        "name": "00808042",
        "unit": "unknown",
        "transformation": lambda x: float(x[0])
    },

    "00040041": {
        "name": "00040041",
        "unit": "unknown",
        "transformation": lambda x: float(x[0])
    },

    "10040001": {
        "name": "10040001",
        "unit": "unknown",
        "transformation": lambda x: float(x[0])
    },

    "00120041": {
        "name": "00120041",
        "unit": "unknown",
        "transformation": lambda x: float(x[0])
    },

    "00688041": {
        "name": "00688041",
        "unit": "unknown",
        "transformation": lambda x: float(x[0])
    },

    "00358041": {
        "name": "total_power_savings_this_year",
        "unit": "kWh",
        "transformation": transform_air_volume
    },

    "ventilation_level": {
        "name": "00104041",
        "unit": "ventilation_level",
        "transformation": lambda x: float(x[0])
    },

    "00544041": {
        "name": "00544041",
        "unit": "unknown",
        "transformation": lambda x: float(x[0])
    },

    "00498041": {
        "name": "00498041",
        "unit": "unknown",
        "transformation": lambda x: float(x[0])
    },

    "00814042": {
        "name": "00814042",
        "unit": "unknown",
        "transformation": lambda x: float(x[0])
    },

    "000C4041": {
        "name": "000C4041",
        "unit": "unknown",
        "transformation": lambda x: float(x[0])
    },

    "00828042": {
        "name": "00828042",
        "unit": "unknown",
        "transformation": lambda x: float(x[0])
    },

    "00494041": {
        "name": "00494041",
        "unit": "unknown",
        "transformation": lambda x: float(x[0])
    },

    "004C8041": {
        "name": "004C8041",
        "unit": "unknown",
        "transformation": transform_air_volume
    },
    "00388041": {
        "name": "00388041",
        "unit": "unknown",
        "transformation": transform_air_volume
    },
    "00188041": {
        "name": "bypass_a_status",
        "unit": "unknown",
        "transformation": transform_air_volume
    },
    "00184041": {
        "name": "bypass_b_status",
        "unit": "unknown",
        "transformation": transform_air_volume
    },
    "00108041": {
        "name": "bypass_state",
        "unit": "0=auto,1=open,2=close",
        "transformation": lambda x: float(x[0])
    },
    "0038C041": {
        "name": "bypass_open",
        "unit": "%",
        "transformation": lambda x: float(x[0])
    }
}

command_mapping = {
    "set_ventilation_level_0": b'T1F07505180100201C00000000\r',
    "set_ventilation_level_1": b'T1F07505180100201C00000100\r',
    "set_ventilation_level_2": b'T1F07505180100201C00000200\r',
    "set_ventilation_level_3": b'T1F07505180100201C00000300\r',
    "auto_mode": b'T1F075051485150801\r', # verified (also: T1F051051485150801\r)
    "manual_mode": b'T1F07505180084150101000000\r', # verified (also: T1F051051485150801\r)
    "temperature_profile_cool": b'T0010C041101\r',
    "temperature_profile_normal": b'T0010C041100\r',
    "temperature_profile_warm": b'T0010C041102\r',
    "close_bypass": b'T00108041102\r',
    "open_bypass": b'T00108041101\r',
    "auto_bypass": b'T00108041100\r',
    "basis_menu": b"T00400041100\r",
    "extended_menu": b"T00400041101\r"
}
