# Each variable below is an instance of a class.
example_list = ["Dave", "Rob", "Stephen"] # instance of the 'list' class
example_boolean = True  # instance of the 'bool' class
example_string = "hello world"  # instance of the 'str' class
# Printing the type of each variable to verify their class instances
print(type(example_list))  # Output: <class 'list'>
print(type(example_boolean))  # Output: <class 'bool'>
print(type(example_string))   # Output: <class 'str'>
# Even a function is an instance of the 'function' class
def this_is_a_function(a, b):
 return a * b
# Printing the type of the function to verify its class instance
print(type(this_is_a_function))   # Output: <class 'function'>