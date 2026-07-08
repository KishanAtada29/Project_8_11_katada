"""
Program Name: Subnet Planner 2.0
Author: Kishan Atada
Purpose: Provide shared helper functions for IPv4 and CIDR calculations.
Starter Code Information: This code was refactored from my own Project 1 code. No instructor starter code was used.
Date: July 8th, 2026
"""

class Functions:
    @staticmethod
    def prefix_bits():
        """Return the bit values used to calculate one subnet-mask octet."""
        numbers = [128, 64, 32, 16, 8, 4, 2, 1]
        return numbers
    
    @staticmethod
    def single_octet_bits():
        """Return the number of bits in one IPv4 octet."""
        return len(Functions.prefix_bits())
    
    @staticmethod
    def number_of_octets():
        """Return the number of octets in an IPv4 address."""
        return 4
    
    @staticmethod
    def total_bits():
        return (Functions.single_octet_bits() * Functions.number_of_octets())


    @staticmethod
    def unusable_IPs():
        """Return the 2 traditionally reserved network and broadcast addresses."""
        return 2
    
    @staticmethod
    def octect_value():
        """Return the maximum decimal value of one IPv4 octet."""
        return sum(Functions.prefix_bits())
    
    @staticmethod
    def usable_ip(num):
        """
        Calculate the number of usable IPv4 host addresses.

        Args:
            num: The CIDR prefix.

        Returns:
            The number of usable host addresses.
        """
        num = Functions.total_bits() - num
        num = (Functions.unusable_IPs() ** num) - Functions.unusable_IPs()
        return num

