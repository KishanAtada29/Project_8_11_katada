"""
Program Name: Subnet Planner 2.0
Author: Kishan Atada
Purpose: Save subnet report data to a JSON file.
Starter Code Information: No starter code was used.
Date: July 8th, 2026
"""

import json
from pathlib import Path


class FileManager:
    """Handles saving subnet reports to a JSON file."""

    def __init__(self):
        """Create the file path for the saved subnet report."""
        self.__file_path = Path("saved_reports/subnet_report.json")

    def save_report(self, report):
        """Save a subnet report object to a JSON file."""
        report_data = {
            "cidr": report.get_cidr(),
            "usable_ip": report.get_usable_ip(),
            "subnetmask": report.get_subnetmask(),
            "description": report.get_description()
        }

        try:
            self.__file_path.parent.mkdir(exist_ok=True)

            with open(self.__file_path, "w") as file:
                json.dump(report_data, file, indent=4)

            print("Report saved successfully.")

        except OSError:
            print("Error: Report could not be saved.")