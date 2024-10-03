#acces

class Employee:
    def __init__(self):
        self.__name = "shubham"
        self._level = "100"

a= Employee()
# print (a.__name)
print(a._Employee__name)
#

print(a._level)
print(a.__dir__())