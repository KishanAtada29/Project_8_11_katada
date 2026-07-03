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

def get_result(cidr,desc):
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
            
        print(f'CIDR: /{cidr}')
        print(f'Number of useable host: {ip}')
        print(f'Subnet Mask: {".".join(map(str,(sc.subnetmask_calculator(cidr))))}')
        print('Description: ' + desc)

def cidr_calculator():
    """
    Ask the user for a CIDR prefix and display the subnet information.

    The function validates that the CIDR value is between 0 and 32.
    """
    print('')
    cidr = int(input('Please enter CIDR (0-32): '))
    while cidr > 32 or cidr < 0:
        print('Error...')
        cidr = int(input('Please enter CIDR (0-32): '))


    print('')
    get_result(cidr, cd.cidr_desc(cidr))
   
   

    