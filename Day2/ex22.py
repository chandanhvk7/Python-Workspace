#UNIT TESTING
import unittest
from utils.days import max_days

class TestMaxDays(unittest.TestCase):
    def test_valid_31_days_months(self):
        months=[1,3,5,7,8,10,12]
        year=2024
        expected=31
        for month in months:
            actual=max_days(month,year)
            self.assertEqual(expected,actual)

    def test_valid_30_days_months(self):
        months=[4,6,9,11]
        year=2024
        expected=30
        for month in months:
            actual=max_days(month,year)
            self.assertEqual(expected,actual)

    def test_valid_days_feb(self):
        month=2
        year=2024
        expected=29
        actual=max_days(month,year)
        self.assertEqual(expected,actual)
    
    def test_wrong_type_for_month(self):
        with self.assertRaises(TypeError):
            max_days(year="asd")
            


if __name__=="__main__":
    unittest.main()