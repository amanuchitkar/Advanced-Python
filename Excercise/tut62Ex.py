class Electronics_device:
    start = "It is a kind of device which uses"
    power_tack = "AC current"
    Advantage = "Faster, take less time to executing,chipper in price"
    disadvantage = "take so much electricity, difficult to carry"

    def printdevice(self):
        return f"{self.start} {self.power_tack}\nAdvantages and Disadvantages are" \
               f" following:\n   Advantages: {self.Advantage}\n   Disadvantages: " \
               f"{self.disadvantage}\n"


class Portebale_device(Electronics_device):
    Advantage = "Portable,Energy efficient"
    disadvantage = "costly in price"
    power_tack = "DC current"

    def printdevice(self):
        return f"{self.start} {self.power_tack}\nAdvantages and Disadvantages are" \
               f" following:\n   Advantages: {self.Advantage}\n   Disadvantages: " \
               f"{self.disadvantage}\n"


class Phone(Portebale_device):
    Advantage = "use to call,carry any ware, fit in pocket,it has camera,"
    disadvantage = "comparatively slower,do limited task, wast of time and money"

    def printdevice(self):
        return f"{self.start} {self.power_tack}\nAdvantages and Disadvantages are" \
               f" following:\n   Advantages: {self.Advantage}\n   Disadvantages: " \
               f"{self.disadvantage}\n"


computer = Electronics_device()
smartwatch = Portebale_device()
pocox2 = Phone()
print(computer.printdevice())
print(smartwatch.printdevice())
print(pocox2.printdevice())
