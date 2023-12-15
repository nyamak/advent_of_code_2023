import unittest
from main import get_gear_ratio_part_one, get_gear_ratio_part_two


class TestGearRatio(unittest.TestCase):
    def test_get_gear_ratio_part_one(self) -> None:
        with open("test.txt") as f:
            content = f.read()
            res = get_gear_ratio_part_one(content)
        self.assertEqual(res, 4361)

    def test_get_gear_ratio_part_two(self) -> None:
        with open("test.txt") as f:
            content = f.read()
            res = get_gear_ratio_part_two(content)
        self.assertEqual(res, 467835)


if __name__ == "__main__":
    unittest.main()
