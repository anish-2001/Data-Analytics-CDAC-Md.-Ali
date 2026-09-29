'''
Develop a context manager
1. context manager work with "with" statements
'''
# A "context manager" is simply an object that sets up a temporary environment (a context) for a block of code to run in, handles things while it runs, and then cleans up afterward.

# class CA:
#     def __init__(self):
#         print("self",id(self))
       
#     def fun(self):
#         print("fun")

#     def __enter__(self):
#         print("Enter")

#     def __exit__(self, exc_type, exc, tb):
#         print("Exit")

# # obj = CA()
# # print(id(obj))

# obj1 = CA() #In this code, obj1 is acting as the context manager.
# with obj1:
#     obj1.fun()
#     # print(id(obj1))

#----------------------------------------------------------------

class CA:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file_object = None

    def __enter__(self):
        print("Enter: Opening the file...")
        # Open the file and assign it to self.file_object
        self.file_object = open(self.filename, self.mode)
        # Return the file object so the 'as' keyword can capture it
        return self.file_object

    def __exit__(self, exc_type, exc, tb):
        print("Exit: Closing the file safely...")
        if self.file_object:
            self.file_object.close()
        # Returning None (or False) lets Python propagate exceptions normally if any occur

# Using the context manager with the 'with' statement
with CA("sample.txt", "w") as f:
    f.write("Hello, writing to file inside a custom context manager!")
    print("Writing process is active inside the 'with' block.")