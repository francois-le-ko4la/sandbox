import inspect

class A:
    def one(self):
        pass

    def two(self):
        pass

    def three(self):
        pass

    def four(self):
        pass

def linenumber_of_member(m):
    try:
        print("\n{}\n\n".format(m[1].im_func.func_code.co_firstlineno))
        return m[1].im_func.func_code.co_firstlineno
    except AttributeError:
        return -1

a = A()
l = inspect.getmembers(a)
print(l)
print("\n\n\n******************\n")
l.sort(key=linenumber_of_member)
print(l)

