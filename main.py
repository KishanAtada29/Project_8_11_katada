"""
    Program Name: Subnet Planner
    Author: Kishan Atada
    Purpose: Provide classful subnet information and calculate subnet masks
    from CIDR prefixes.
    Starter Code Information: No starter code was used.
    Date: June 23, 2026
"""

import classful_subnet_info as csi
from cidr_input import CidrInput 


ci = CidrInput()
def display_menu():
    """Display the main menu options."""
    print('1. Claseful Subnet Info')
    print('2. Manual CIDR Calculator')
    print('3. Exit')


while True:
    print('')
    print('Subnetmask Planner')
    print('-------------------')
    print('')
    display_menu()
    print('')
    try:
        user_choice = int(input('Please Enter One of the Choice (1-3): '))
    except ValueError:
        print('Please Enter the Number..')
        continue
    if user_choice not in [1,2,3]:
        print('')
        print('Invalid option...')
        print('')
        display_menu()
        print('')
        user_choice = int(input('Please Enter One of the Choice (1-3): '))

    if user_choice == 1:
        csi.classful_subnet()
    elif user_choice == 2:
        ci.cidr_calculator()
        
    elif user_choice == 3:
        print('')
        print('Goodbye !')
        print('')
        break
    print('')
    input('Press Enter to continue...')







