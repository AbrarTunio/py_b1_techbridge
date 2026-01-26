class Circle:

    pi = 3.14

    @classmethod
    def change_pi(cls , new_value):
        cls.pi = new_value

Circle.change_pi(2.12)
# Circle.pi = 45


print(Circle.pi)
c = Circle
print(c.pi)