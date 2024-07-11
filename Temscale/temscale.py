from Temscale import temerror


class Temscale:
    """main class that describes the temperature and functions for temperature output and conversion"""
    temperature_value = 0
    temperature_type = None
    temperature_list = ["C", "K"]

    def __init__(self, new_temperature_value: float, new_temperature_type: str) -> None:
        self.set_value(new_temperature_value)
        self.set_type(new_temperature_type)

    def get_value(self) -> float:
        """get the temperature value"""

        return self.temperature_value

    def get_type(self) -> str:
        """get the temperature type"""

        return self.temperature_type

    def set_value(self, new_temperature_value: float) -> None:
        self.temperature_value = new_temperature_value

    def set_type(self, new_temperature_type: str) -> None:
        if new_temperature_type in self.temperature_list:
            self.temperature_type = new_temperature_type
        else:
            raise (TypeError, "temperature value is not correct")

    def CtoK(self) -> None:
        """converts temperature Celsius to Kelvin"""

        if self.temperature_type == "C":
            self.temperature_value += 273.15
            self.temperature_type = "K"
        else:
            raise (temerror.TemperatureError, "Temperature type is not C")

    def KtoC(self) -> None:
        """converts temperature Kelvin to Celsius"""

        if self.temperature_type == "K":
            self.temperature_value -= 273.15
            self.temperature_type = "C"
        else:
            raise (temerror.TemperatureError, "Temperature type is not K")
