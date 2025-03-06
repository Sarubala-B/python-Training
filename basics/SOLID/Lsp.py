class Bird:
    def fly(self):
        print("Flying")

class Penguin(Bird):  # ❌ Penguins can't fly!
    def fly(self):
        raise Exception("Penguins can't fly!")


class Bird:
    pass  # ✅ Common behavior

class FlyingBird(Bird):
    def fly(self):
        print("Flying")

class Penguin(Bird):  # ✅ Penguins don't inherit fly()
    def swim(self):
        print("Swimming")

# ✅ No risk of runtime errors
