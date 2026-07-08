"""
Program Name: Subnet Planner 2.0
Author: Kishan Atada
Purpose: Collect and validate CIDR input, then display subnet information.
Starter Code Information: This code was refactored from my own Project 1 code. No instructor starter code was used.
Date: July 8th, 2026
"""
from subnetmask_calculator import SubnetMaskCalculator
from functions import Functions
import cidr_desc as cd
from subnet_report import SubnetReport
from file_manager import FileManager

class CidrInput:
    def __init__(self):
        self._function = Functions()
        self._file_manger = FileManager()

    def get_result(self,cidr,desc):
        """
        Display the calculated CIDR information.

        Args:
        cidr: An integer from 0 to 32.
        desc: A description of the CIDR prefix.
        """
        if cidr == 31:
            ip = 2
        elif cidr == 32:
            ip = 1
        else: 
            ip = self._function.usable_ip(cidr)

        calculator = SubnetMaskCalculator(cidr)
        subnet_mask = calculator.calculate_subnetmask()
        report = SubnetReport(cidr, ip, subnet_mask, desc)
        report.display_report()
        save_choice = input("Do you want to save this report? yes/no: ").lower()

        if save_choice == "yes":
            self._file_manger.save_report(report)           
            

    def cidr_calculator(self):
        """
        Ask the user for a CIDR prefix and display the subnet information.

        The function validates that the CIDR value is between 0 and 32.
        """
        print('')
        while True:

            try:
                cidr = int(input('Please enter CIDR (0-32): '))
                if cidr > 32 or cidr < 0:
                    print('Error... CIDR must be btween 0 to 32')
                else:
                    break
            
            except ValueError:
                print('Please Enter the number.')
        print('')
        self.get_result(cidr, cd.cidr_desc(cidr))
    
    

    