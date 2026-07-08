"""
Program Name: Subnet Planner
Author: Kishan Atada
Purpose: Convert a CIDR prefix into a four-octet subnet mask.
Starter Code Information: No starter code was used.
Date: July 8th, 2026
"""

from functions import Functions


class SubnetMaskCalculator:
    """Calculates a subnet mask from a CIDR prefix."""

    def __init__(self, cidr):
        """Store the CIDR prefix."""
        self.__cidr = cidr
        self.__functions = Functions()

    def get_cidr(self):
        """Return the CIDR prefix."""
        return self.__cidr

    def calculate_subnetmask(self):
        """Convert a CIDR prefix into a subnet mask."""
        subnetmask = []

        if self.__cidr == 0:
            subnetmask = [0, 0, 0, 0]
        else:
            octet = 0
            octet_side = self.__cidr % self.__functions.single_octet_bits()
            each_octet = int(self.__cidr / self.__functions.single_octet_bits())

            for bit in range(each_octet):
                subnetmask.append(sum(self.__functions.prefix_bits()))

            for bit in range(octet_side):
                octet = self.__functions.prefix_bits()[bit] + octet

            if octet_side > 0:
                subnetmask.append(octet)

            while len(subnetmask) < 4:
                subnetmask.append(0)

        return subnetmask