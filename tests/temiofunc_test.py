import unittest
from src.Temscale import temiofunc
from src.Temscale import temscale


class TestTemIOFunc(unittest.TestCase):
    def test_to_tuple(self):
        tem = temscale.Temscale(100, "C")
        self.assertEqual(temiofunc.to_tuple(tem), (100, "C"))

    def test_from_tuple(self):
        tem = temiofunc.from_tuple((100, "C"))
        self.assertEqual(temiofunc.to_tuple(tem), (100, "C"))

    def test_to_list(self):
        tem = temscale.Temscale(100, "C")
        self.assertEqual(temiofunc.to_list(tem), [100, "C"])

    def test_from_list(self):
        tem = temiofunc.from_list([100, "C"])
        self.assertEqual(temiofunc.to_list(tem), [100, "C"])

    def test_to_dict(self):
        tem = temscale.Temscale(100, "C")
        self.assertEqual(temiofunc.to_dict(tem), {"temperature_value": 100, "temperature_type": "C"})

    def test_from_dict(self):
        tem = temiofunc.from_dict({"temperature_value": 100, "temperature_type": "C"})
        self.assertEqual(temiofunc.to_dict(tem), {"temperature_value": 100, "temperature_type": "C"})

    def test_output_format(self):
        tem = temscale.Temscale(100, "C")
        self.assertEqual(temiofunc.output_format(tem, "{v}:{t}"), "100:C")

    def test_input_format(self):
        tem = temiofunc.input_format("100.0:C", ":")
        self.assertEqual(temiofunc.output_format(tem, "{v}:{t}"), "100.0:C")


if __name__ == '__main__':
    unittest.main()
