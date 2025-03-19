# Assisted by watsonx Code Assistant 
import unittest
from src.risk_atlas_nexus.toolkit.error_utils import type_check, value_check

class TestErrorUtils(unittest.TestCase):

    def test_type_check(self):
        with self.assertRaises(TypeError):
            type_check("type_check_error", int, "value", value="not_an_int")

        with self.assertRaises(RuntimeError):
            type_check("type_check_error", str, None, allow_none=False)

        with self.assertRaises(RuntimeError):
            type_check("type_check_error")

        with self.assertRaises(RuntimeError):
            type_check("type_check_error", int)

    def test_value_check(self):
        val = 25
        with self.assertRaises(ValueError):
            value_check("value_check_error", val > 25, "value is not larger than 25")

        with self.assertRaises(ValueError):
            value_check("value_check_error", 0, "value is not greater than 0")

        with self.assertRaises(ValueError):
            value_check("value_check_error", 0 < val < 1, "value is not between 0 and 1", val)

if __name__ == '__main__':
    unittest.main()