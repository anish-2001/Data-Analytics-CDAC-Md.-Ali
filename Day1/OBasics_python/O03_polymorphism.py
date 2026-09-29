from abc import ABC,abstractmethod # ABC: Abstract Base Class

class Account(ABC):
    @abstractmethod
    def do_job(self):
        pass

def Business(acc_lst):
    print("Business Started")
    for acc in acc_lst:
        acc.do_job()
    else:
        print("Completed All account type verification")
    print("Business Completed")
print("_" * 60)
# -----------------------------------------------------

class Savings(Account):
    def do_job(self):
        print("Savings job done")

class Current(Account):
    def do_job(self):
        print("Current job done")

class DMat(Account):
    def do_job(self):
        print("DMat job done")

class OD(Account):
    def do_job(self):
        print("OD job done")

# acc = Account() # Can't instantiate abstract class Account | This error means we are trying to create an object directly from a class (Account) that has been designated as an Abstract Base Class (ABC). Python explicitly blocks us from doing this.

# sa = Savings()
# curr =  Current()
# dmat = DMat()

# Business([sa,curr,dmat])
# sub_classes = [sub for sub in Account.__subclasses__()]
sub_classes = [sub.__name__ for sub in Account.__subclasses__()]
print(sub_classes)
str_class_name = "Savings"
# sub_object =[ eval(f"{str_class_name}()")]
#Step 1: The f-string builds the string
# When Python evaluates the f-string f"{str_class_name}()":
# It looks up the variable str_class_name, which holds the text "savings".
# It substitutes that value into the placeholder and tacks () onto the end.
# The result of this step is the raw string: "savings()".

# Step 2: eval() executes that string as code
# This is where the magic (and danger) happens. The eval() function takes that string ("savings()") and hands it over to Python's interpreter to run as live code.
# It does not return a string.
# Instead, it treats "savings()" as a command, calls the savings class constructor, and returns an actual Python object (an instance of that class).

sub_object = [eval(f"{sub.__name__}()") for sub in Account.__subclasses__()]
Business(sub_object)
