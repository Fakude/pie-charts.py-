import unittest

from visualise_enrolment import load_data


class DataTests(unittest.TestCase):
    def test_example_data_loads(self):
        rows = load_data("data/enrolment.csv")
        self.assertEqual(len(rows), 3)
        self.assertEqual(sum(value for _, value in rows), 1214)


if __name__ == "__main__":
    unittest.main()
