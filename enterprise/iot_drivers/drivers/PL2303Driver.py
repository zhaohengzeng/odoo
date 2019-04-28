import serial
from odoo.addons.hw_drivers.controllers.driver import USBDriver

class SylvacUSBDriver(USBDriver):

    def supported(self):
        return getattr(self.dev, 'idVendor') == 0x067b and getattr(self.dev, 'idProduct') == 0x2303

    def run(self):
        connection = serial.Serial('/dev/serial/by-id/usb-Prolific_Technology_Inc._USB-Serial_Controller-if00-port0',
                                   baudrate=4800,
                                   bytesize=7,
                                   stopbits=2,
                                   parity=serial.PARITY_EVEN)
        measure = b''
        no_except = True
        while no_except:
            try:
                char = connection.read(1)
                if ord(char) == 13:
                    # Let's send measure
                    self.value = measure.decode("utf-8")
                    measure = b''
                else:
                    measure += char
            except:
                no_except = False

    def action(self, action):
        pass