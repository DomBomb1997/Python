#Protected Var
class Protected:
    def __init__(self):
        self._protectedVar = 0

obj = Protected()
obj._protectedVar = 34
print(obj._protectedVar)

