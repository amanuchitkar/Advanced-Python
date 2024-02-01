class Bank:
    # def __init__(self):
    #     self._Bank__private = None  # write private var

    __private = 80
    _protected = 79
    public = 78
    __password = 17122002
    # In that way we also use our private and protracted variable in other class
    # @property
    # def protracted(self):
    #     return self.__priavte


class client(Bank):
    pass


i = Bank()
print(i._protected)  # use protected var
print(i._Bank__private)  # use private var
print(i._Bank__password)  # use private var
# els = client()
# print(els.public)
# print(els._protracted)
