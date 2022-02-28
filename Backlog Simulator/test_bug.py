"""Testing module for Bug Class"""

import unittest
from bug import Bug


class TestBug(unittest.TestCase):
    """Test the Bug Class"""

    def setUp(self):
        self.bug = Bug(1, 10)

    def tearDown(self):
        pass

    def test_age(self):
        """Test age method"""

        self.assertEqual(self.bug.age(14), 4)

        with self.assertRaises(ValueError):
            self.bug.age(9)
            self.bug.age(-2)

    def test_null(self):
        """Test the null method"""

        self.assertEqual(self.bug.null(), 0)


if __name__ == "__main__":
    unittest.main()
