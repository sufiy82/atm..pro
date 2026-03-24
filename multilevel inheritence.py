class animal:
    def p(self):
        print("animal eats food")
class dog(animal):
    def p1(self):
        print("the dog sounds bow bow")
class puppy(dog):
    def p2(self):
        print("the puppy weeeps")
a=animal()
a.p()
d=dog()
d.p1()
c=puppy()
c.p2()
