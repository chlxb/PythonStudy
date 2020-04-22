__metaclass__ = type # python2 需要包含这行代码

class Person:
    def set_name(self, name):
        self.name = name

    def get_name(self, name):
        return self.name

    def greet(self):
        print("Hello, world! I'm {}.".format(self.name))


p1 = Person()
p1.set_name('kity')

p2 = Person()
p2.set_name('locy')

p1.greet()
