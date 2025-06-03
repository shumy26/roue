import unittest
from src.structures import Time, TimeBlock, DayBlock, Week

class StructureTest(unittest.TestCase):
    def test_add_time(self):
        time1 = Time(1,40)
        time2 = Time(3,20)
        time3 = Time(4,40)
        time4 = Time(6,15)

        self.assertEqual(time1 + time2, Time(5,0))
        self.assertEqual(time1 + time3, Time(6,20))
        self.assertEqual(time1 + time4, Time(7,55))
        with self.assertRaises(AttributeError):
            time1 + 2