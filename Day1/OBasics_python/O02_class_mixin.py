# class mixin: A Mixin is a special kind of class designed to provide extra methods and functionality to other classes through multiple inheritance, but it is not meant to stand alone as a main base class.
class StateMixin:
    def ShowState(self):
        members = {mem:getattr(self,mem) for mem in vars(self)}
        print(members)

class Person:
    def __init__(self):
        self.id = 101
        self.name = "Sachin"
        self.age = 51


class Employee:
    def __init__(self):
        self.eid=1001
        self.e_name="tendulkar"
        self.salary = 100

class Product:
    def __init__(self):
        self.p_pid  = 111
        self.p_name = "nail polish"
        self.price = 125


class PersonIntrospect(Person,StateMixin):
    pass

class EmployeeIntrospect(Employee,StateMixin):
    pass

class ProductIntrospect(Product,StateMixin):
    pass


person_intro = PersonIntrospect() # This line is called instantiation (or creating an instance / object creation)
employee_intro = EmployeeIntrospect()
product_intro = ProductIntrospect()
person_intro.ShowState()
employee_intro.ShowState()
product_intro.ShowState()