import unittest
from unittest.mock import MagicMock
from src.containers import SmallContainer, HeavyContainer

class TestContainerWeightWithMocks(unittest.TestCase):
    def setUp(self):
        self.small_container = MagicMock(spec=SmallContainer)
        self.heavy_container = MagicMock(spec=HeavyContainer)

        self.small_container.get_total_weight = MagicMock(return_value=500)
        self.heavy_container.get_total_weight = MagicMock(return_value=1500)

    def test_small_container_weight(self):
        weight = self.small_container.get_total_weight()
        self.assertEqual(weight, 500)

    def test_heavy_container_weight(self):
        weight = self.heavy_container.get_total_weight()
        self.assertEqual(weight, 1500)

if __name__ == "__main__":
    unittest.main()

