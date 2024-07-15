from src.Temscale import temerror


class Temscale:
    """main class that describes the temperature and functions for temperature output and conversion"""
    temperature_value = 0
    temperature_type = None
    temperature_list = ["C", "K", "F"]

    def __init__(self, new_temperature_value: float, new_temperature_type: str) -> None:
        self.set_value(new_temperature_value)
        self.set_type(new_temperature_type)

    def __eq__(self, other) -> int:
        """
        translate into Kelvin and compare the value
        :type other: Temscale
        """
        if isinstance(other, Temscale):
            if self.temperature_type == "K":
                if other.temperature_type == "K":
                    return self.temperature_value == other.temperature_value
                else:
                    other.to_kelvin()
                    return self.temperature_value == other.temperature_value
            else:
                self.to_kelvin()
                if other.temperature_type == "K":
                    return self.temperature_value == other.temperature_value
                else:
                    other.to_kelvin()
                    return self.temperature_value == other.temperature_value

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

    def to_celsius(self) -> None:
        """converts temperature to Celsius"""

        match self.temperature_type:
            case "C":
                raise (temerror.TemperatureError, "The temperature's already Celsius")
            case "K":
                self.temperature_value -= 273.15
                self.temperature_type = "C"
            case "F":
                self.temperature_value = (self.temperature_value - 32) / 1.8
                self.temperature_type = "C"
            case _:
                raise (temerror.TemperatureError,
                       f"the value '{self.temperature_type}' is not a temperature type")

    def to_kelvin(self) -> None:
        """converts temperature to Kelvin"""

        match self.temperature_type:
            case "C":
                self.temperature_value += 273.15
                self.temperature_type = "K"
            case "K":
                raise (temerror.TemperatureError, "The temperature's already Kelvin")
            case "F":
                self.temperature_value = (self.temperature_value + 459.67) / 1.8
                self.temperature_type = "K"
            case _:
                raise (temerror.TemperatureError,
                       f"the value '{self.temperature_type}' is not a temperature type")

    def to_fahrenheit(self) -> None:
        """converts temperature to Fahrenheit"""

        match self.temperature_type:
            case "C":
                self.temperature_value = (self.temperature_value * 1.8) + 32
                self.temperature_type = "F"
            case "K":
                self.temperature_value = (self.temperature_value * 1.8) - 459.67
                self.temperature_type = "F"
            case "F":
                raise (temerror.TemperatureError, "The temperature's already Fahrenheit")
            case _:
                raise (temerror.TemperatureError,
                       f"the value '{self.temperature_type}' is not a temperature type")
