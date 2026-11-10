class Person:
    @classmethod
    def getGender(cls):
        pass
class Male(Person):
    print("男")

class Female(Person):
    print("女")
male=Male()
female=Female()
male.getGender()
female.getGender()