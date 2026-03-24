class animal:
    def p(self):
        print("animal eats food")
class dog(animal):
    def p1(self):
        print("the dog barks")
class puppy(animal):
    def p2(self):
        print("the puppy weeeps")
a=animal()
a.p()
d=dog()
d.p()
d.p1()
c=puppy()
c.p()
c.p2()
