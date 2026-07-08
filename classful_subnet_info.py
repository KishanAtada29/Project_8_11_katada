"""
Program Name: Subnet Planner 2.0
Author: Kishan Atada
Purpose: Calculate and display default Class A, Class B, and Class C subnet information.
Starter Code Information: This code was refactored from my own Project 1 code. No instructor starter code was used.
Date: July 8th, 2026
"""

from functions import Functions
from subnet_report import SubnetReport
from subnetmask_calculator import SubnetMaskCalculator


class ClassfulSubnetInfo:
    """Displays default Class A, Class B, and Class C subnet information."""

    def __init__(self):
        """Store default classful subnet CIDR values."""
        self.__classful_data = {
            "Class A": 8,
            "Class B": 16,
            "Class C": 24
        }

    def get_classful_data(self):
        """Return classful subnet data."""
        return self.__classful_data

    def calculate_usable_hosts(self, cidr):
        """Calculate usable hosts from a CIDR prefix."""
        host_portion = Functions.total_bits() - cidr
        return (2 ** host_portion) - Functions.unusable_IPs()

    def display_classful_subnet(self):
        """Display Class A, Class B, and Class C subnet information."""
        for class_name, cidr in self.__classful_data.items():
            usable_hosts = self.calculate_usable_hosts(cidr)
            calculator = SubnetMaskCalculator(cidr)
            subnet_mask = calculator.calculate_subnetmask()
            description = f"Default {class_name} subnet."

            report = SubnetReport(cidr, usable_hosts, subnet_mask, description)

            print()
            print(class_name)
            report.display_report()
            print("-------------------------")