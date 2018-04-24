
class A(object):
    def __init__(self, value):
        self.x = value

    @property
    def x(self):
        print('set')
        return self.__x

    @x.setter
    def x(self, value):
        print('check')
        if value is not 0:
            raise ValueError("No !")
        else:
            print("OK")
            self.__x = value

print('instance')
myA = A(0)
print(myA.x)

print('instance')
myA = A(2)






