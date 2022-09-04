employee_list = [('Swastik', 160, True), ('Charlie', 800, True), ('Samuel', 1000, True),
                 ('Harvey', 1600, False)]


def max_hours_worked(example_list):
    """
    This function is used to find the best employee in a company based on their hours worked and
    verification status. Some employees can work for more hours but without a valid verification.
    In such cases, the function will only consider employees who have valid verification and find
    the best employee with most hours worked in that range.

    Parameter: a tuple consisting of Name, Hours worked, and verification status.
    Returns: The employee who has worked the most hours with valid verification.

    """

    maximum_hours = 0
    best_employee = ''

    for name, hours, verification in example_list:
        if hours > maximum_hours and verification is True:  # Only checks employee hours with valid verification
            maximum_hours = hours
            best_employee = name
        else:
            pass
    return best_employee, maximum_hours


"""

Common error example:
name, hours, validity = function_name(sample_input)
if we run the above command, an error will be thrown because 'function_name' 
could have 3 values per value in the tuple but the function only returns two values.
This is a very easy error to occur, especially when using functions from other libraries where we don't
know the exact function signatures. To fix this error we can:
Store the result of a function call in a variable like this: 
result = function_name(sample_input)
This is done so that if we get ValueError: not enough values to unpack
What we can do to diagnose the error is-
example_variable = function_name(sample_input)
print(example_variable)
example_variable would print all the values that the function returns 
This will allow us to know which value it does not return and we can modify our existing code
from above accordingly.

"""
# Alternative way of returning values from the function: name, hours, = max_hours_worked(employee_list)
print('The best employee is:', max_hours_worked(employee_list))
