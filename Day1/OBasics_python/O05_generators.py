from sys import getsizeof # A built-in Python function used to measure the exact memory footprint of an object in bytes.
# The term exact memory footprint refers to the precise amount of RAM (measured in bytes) that a specific object, variable, or data structure consumes in your computer's memory while your program is running.

max_limit = 1000000
l1 = [x**2 for x in range(1,max_limit)]
g1 = (x**2 for x in range(1,max_limit))
# print("sizeof(l1)",getsizeof(l1),"Type",type(l1),sep="\t:\t")
# print("sizeof(g1)",getsizeof(g1),"Type",type(g1),sep="\t:\t")

# print("sum(l1)",sum(l1),sep="\t:\t")
# print("sum(g1)",sum(g1),sep="\t:\t")
#----------------------------------------------------------------
# print(l1) :--> If you try to print g1 directly using print(g1), Python will not print the numbers. Instead, it will output a string representation of the generator object itself, looking something like this:<generator object <genexpr> at 0x7f9a1b2c3d4e>.  Why Does This Happen?
# Unlike a list comprehension (which computes and stores every single item in memory immediately), a generator expression uses lazy evaluation.

# When you define g1 = (x**2 for x in range(1, max_limit)), Python does not calculate any squares yet.

# It simply creates a generator object—a recipe or blueprint for producing the numbers on-the-fly, one at a time, only when explicitly asked.
#---------------------------------------------------------------

# print(next(g1))   # The Crash (print(next(g1))): Because sum(g1) already consumed the generator all the way to the end, g1 is now completely exhausted and empty. When you immediately try to call next(g1) on it afterward, Python throws a StopIteration error because there are no items left.
# print(next(g1))
# print(next(g1))
# print(next(g1))
# print(next(g1))
# print(next(g1))
# print(next(g1))
print("_" * 60)

def surabhi():
    print("Apple")
    yield 100
    print("Orange")
    yield 200
    print("Pine")
    yield 300

result = surabhi()

print(type(result))

print(next(result))
print(result.__next__())
print(result.__next__())
# print(result.__next__()) # stopiteration 
print("_" * 60)

for x in surabhi():
    print(x)

# When you run a for loop on a generator like for x in surabhi():, Python automatically automates all the manual next() calls and error handling for you behind the scenes.

# Here is exactly what happens step by step:

# The for loop calls surabhi(), creating the generator object.

# It automatically starts pulling values by calling next() under the hood.

# Every time a value is yielded, it assigns that value to x and runs your loop body (print(x)).

# When the generator finally runs out of items and raises a StopIteration error, the for loop catches that error silently and exits cleanly without crashing your program.