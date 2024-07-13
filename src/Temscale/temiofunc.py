from src.Temscale import temscale


def to_tuple(tem: temscale.Temscale) -> tuple:
    return tem.get_value(), tem.temperature_type


def from_tuple(t: tuple) -> temscale.Temscale:
    return temscale.Temscale(*t)


def to_list(tem: temscale.Temscale) -> list:
    return [tem.get_value(), tem.temperature_type]


def from_list(ls: list) -> temscale.Temscale:
    return temscale.Temscale(*ls)


def to_dict(tem: temscale.Temscale) -> dict:
    return {"temperature_value": tem.get_value(), "temperature_type": tem.temperature_type}


def from_dict(d: dict) -> temscale.Temscale:
    return temscale.Temscale(d["temperature_value"], d["temperature_type"])


def output_format(tem: temscale.Temscale, format_temperature: str) -> str:
    """returns data in formats
    parameters "format_temperature":
    v - temperature value
    t - type of temperature scale
    For example: v = 100, t = "C", "{v}:{t}" - "100:C" """

    return format_temperature.format(v=str(tem.temperature_value), t=tem.temperature_type)


def input_format(format_temperature: str, divider: str) -> temscale.Temscale:
    """accepts data in formats
    parameters "format_temperature":
    For example: d = ":", "100:C" - v = 100, t = "C" """

    value = format_temperature.split(divider)
    return temscale.Temscale(float(value[0]), value[1])
