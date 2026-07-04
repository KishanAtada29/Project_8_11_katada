class SubnetReport:
    def __init__(self, cidr,usable_ip, subnetmask,description):
        self._cidr = cidr
        self._usable_ip = usable_ip
        self._subnetmask = subnetmask
        self._description = description

    def get_cidr(self):
        """Return the CIDR prefix."""
        return self.__cidr

    def get_usable_ip(self):
        """Return the number of usable IP addresses."""
        return self.__usable_ip

    def get_subnetmask(self):
        """Return the subnet mask."""
        return self.__subnetmask

    def get_description(self):
        """Return the CIDR description."""
        return self.__description

    def display_report(self):
        """Display the subnet report."""
        print(f"CIDR: /{self.__cidr}")
        print(f"Number of usable host: {self.__usable_ip}")
        print(f"Subnet Mask: {'.'.join(map(str, self.__subnetmask))}")
        print(f"Description: {self.__description}")