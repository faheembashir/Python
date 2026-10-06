class dog:
    def speak(self):
        print("vow vow")
class cow(dog):
    def speak(self):
        super().speak()
        print("mow mow")
c=cow()
c.speak()

