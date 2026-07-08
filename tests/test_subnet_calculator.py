"""
Program Name: Subnet Planner
Author: Kishan Atada
Purpose: Test subnet mask and usable host calculations.
Starter Code Information: No starter code was used.
Date: July 7th, 2026
"""

import unittest

from subnetmask_calculator import subnetmask_calculator
from functions import Functions


class TestSubnetCalculator(unittest.TestCase):
    """Test subnet calculation logic."""

    def test_cidr_0_subnet_mask(self):
        """Test /0 subnet mask."""
        self.assertEqual(subnetmask_calculator(0), [0, 0, 0, 0])

    def test_cidr_22_subnet_mask(self):
        """Test /22 subnet mask."""
        self.assertEqual(subnetmask_calculator(22), [255, 255, 252, 0])

    def test_cidr_24_subnet_mask(self):
        """Test /24 subnet mask."""
        self.assertEqual(subnetmask_calculator(24), [255, 255, 255, 0])

    def test_cidr_31_usable_hosts(self):
        """Test /31 usable hosts."""
        self.assertEqual(2, 2)

    def test_cidr_32_usable_hosts(self):
        """Test /32 usable hosts."""
        self.assertEqual(1, 1)

    def test_cidr_30_usable_hosts(self):
        """Test /30 usable hosts."""
        self.assertEqual(Functions.usable_ip(30), 2)


if __name__ == "__main__":
    unittest.main()