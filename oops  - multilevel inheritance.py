class Electronic_device:
    power_consumpsion = 1
    circuits_type = 'AC'

    def circuit_details(self):
        return f'The circuit type is:{self.circuits_type}'


class Pocket_gadget(Electronic_device):
    power_consumpsion = 2

    def print_gadget(self):
        return f'Gadget names are: {self.name}'


class Phone(Pocket_gadget):
    power_consumpsion = 3

    def phone_names(self):
        return f'phone names are: {self.name}'


android = Phone()
android.name = ("Pixel", "Vivo", "xiomi")

print(android.phone_names())
print(android.power_consumpsion)
print(android.print_gadget())

print(android.circuits_type)
print(android.circuit_details())
