__author__ = 'mueller-klieser'

class phySWP:
    """
    PHYTEC Softwareplatform. This is the class for all software compatible boards from PHYTEC.
    For each board change which requires a single line of code to be changed, we need to add a new phySW instance.
    This could be a chip revision update which changes the chip id, or a option change which is incompatible, or
    a jumper setting on a baseboard which turns the software incompatible. So we will get a huge number of
    Softwareplatforms over time.
    """

    """ Version class variable
    we do versioning on the class abstraction level. Whenever we need a new software platform version we create a new
    instance of the with a version denotifier in the name. It will get a new id too.
    """
    version = 1
    patchlevel= 0

    def __init__(self, machine, machineid, shortname):
        """instance initialization"""
        """each software platform instance has to have a"""
        self.__machine = machine
        self.__machineid = machineid
        self.__shortname = shortname
        """each instance may have an:"""
        self.ipl = phyIPL()
        self.bootloader = phyBootloader()
        self.devicetree = phyDeviceTree()
        self.kernel = phyKernel()
        self.skernel = phyServiceKernel()

    """
    " Properties
    """

    """ PHYTEC machine name: This id is the name of the software platform, it is used as the target "machine"
    build variable in Yocto """
    @property
    def machine(self):
        return self.__machine
    @machine.setter
    def machine(self, machine):
        self.__machine = machine
    """ PHYTEC machine id: This id is the numerical id of the software platform, it is used in the eeprom for runtime
    hardware introspection."""
    @property
    def machineid(self):
        return self.__machineid
    @machineid.setter
    def machineid(self, machineid):
        self.__machineid = machineid
    """ A shortname is sometimes needed. It was used in the Kernel and Barebox. Should we use the ID or the
    shortname? Should we even include the shortname?"""
    @property
    def shortname(self):
        return self.__shortname
    @shortname.setter
    def shortname(self, shortname):
        self.__shortname = shortname


