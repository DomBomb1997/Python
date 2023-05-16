class Protected:
    def __init__(self):
        self.__privateVar = 23

    def getPrivate(self):
        print(self._privateVar)

    def setPrivate(self.__privateVar):
        self.__privateVar = private

obj = protected()
obj.getPrivate()
onj.setPrivate(40)
onj.getPrivate()
