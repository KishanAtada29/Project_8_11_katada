"""
    Program Name: Subnet Planner
    Author: Kishan Atada
    Purpose: Collect and validate CIDR input, then display subnet information.
    Starter Code Information: No starter code was used.
    Date: June 23, 2026
"""
import subnetmask_calculator as sc
from functions import Functions
import cidr_desc as cd
from subnet_report import SubnetReport
from file_manager import FileManager

class CidrInput:

    def get_result(self,cidr,desc):
        f = Functions()
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
            ip = f.usable_ip(cidr)

        subnet_mask = sc.subnetmask_calculator(cidr)
        report = SubnetReport(cidr, ip, subnet_mask, desc)
        report.display_report()
        save_choice = input("Do you want to save this report? yes/no: ").lower()

        if save_choice == "yes":
            file_manager = FileManager()
            file_manager.save_report(report)           
            

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
    
    

    