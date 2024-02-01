class Dad:
    basketball = 1


class Son(Dad):
    badminton = 1

    def printS(self):
        return f"yes i play badminton {self.badminton} no. of times. "


class GrandSon(Son):
    badminton = 8

    def printS(self):
        return f"yes i play badminton awesomely {self.badminton} no. of times. "


aman = Dad()
pranav = Son()
ashutosh = GrandSon()
print(pranav.printS())
print(pranav.basketball)
print(ashutosh.printS())
