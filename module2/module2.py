# accessing object methods using dot notation
# add . in Pycharm to get hints for methods - ignore self argument for now
my_string = 'something'

print('Getting string length using builtin function and object method')
my_str_len = my_string.__len__()
print('Method "__len__" returned: ', my_str_len)
my_str_len = len(my_string)
print('Builtin function "len" returned: ', my_str_len)
print()

# dot notation can be used on the variable pointing to our object or directly on the object
print('Length of variable and object are equal: ', my_string.__len__() == 'something'.__len__())
print()

# Exercise - use capitalise method with dot notation
print('Use string object method to capitalize word')
my_cap_str = my_string.capitalize()
print('Capitalized string is: ', my_cap_str)
print()

# Exercise - use format method with dot notation and one argument
my_format_str = my_string.format('_new')
print('Nothing seems to happen after format: ', my_format_str)
# https://docs.python.org/3.7/library/string.html#string.Formatter.format - let's try adding {}
my_string = 'something{}'
my_format_str = my_string.format('_new')
print('The {} in the string is replaced with argument provided to format: ', my_format_str)
print()

# Integers methods and operations
my_int1 = 3
my_int2 = 2

print('Result of multiplication using * sign: ', my_int1 * my_int2)
print('Result of multiplication using method __mul__": ', my_int1.__mul__(my_int2))
print()

# Raising a number to a power can be done in 3 different ways:
print('Result of using ** notation to raise to power: ', my_int1 ** my_int2)
print('Result of using "pow" function to raise to power: ', pow(my_int1, my_int2))
print('Result of using "__pow__" method to raise to power: ', my_int1.__pow__(my_int2))
print()

# issues with ints and dot notation
# adding a dot after an int will transform that int into a float and Python will expect other numbers to follow
# 3.__mul__(2) - is a SyntaxError
print('Ints required parenthesis to call method (3).__mul__(2): ', (3).__mul__(2))
print('Other types do not require them 3.0.__mul__(1)', 3.0.__mul__(2))
print()

# Float methods and operations
# Floats are used to represent numbers with a floating point
nr1 = 3
nr2 = 2
print('Result of division "3/2" requires a float ', nr1 / nr2)
print('Python automatically converts results to float if required:', type(nr1 / nr2))
print()

# More complex number types are not converted to less complex when possible (float to int)
fl1 = 1.991
fl2 = 0.009
print("Result of adding {} to {} is: ".format(fl1, fl2), fl1 + fl2)
print("Result type of adding {} to {} is: ".format(fl1, fl2), type(fl1 + fl2))
print()

# Non rational numbers
print('Non rational numbers are approximated to floats 1/3 is: ', 1 / 3)
print("Python uses power to calculate the root of a number", 3 ** (1 / 2))
print()

# Complex methods and operations
# Complex number are formed from rational part + non rational part indicated by multiplication wih j (sqrt -1)
print('Value of square root of -1', (-1) ** (1 / 2))  # the rational value is a close to 0 as Python can approximate
print('Type of object representing square root of -1', type((-1) ** (1 / 2)))
print()

# Numbers with exponent can be used to facilitate readability of long numbers
print('Python will accept and print numbers using exponent notation "5.5e100" is: ', 5.5e100)
print('Type of object containing number with exponent is always: ', type(5.5e-100))
print()

# Number base for numbers can be binary, octal, decimal and hexadecimal.
print('Python converts printed numbers to decimal base')
print('Binary number "0b10101111" is printed: ', 0b10101111)
print('Octal number "0o17" is printed: ', 0o17)
print('Hexadecimal number "0xff" is printed: ', 0xff)
print()

# Relational operators
nr1 = 3
nr2 = 2
print('The "==" operator compares values: ', nr1 == 3)
print('The "is" operator compares identity of object (memory location):', nr2 is 2)  # note SyntaxWarning
print('Use "!=" and "is not" to check values and objects respectively are different: ', nr1 != nr2, nr1 is not nr2)
print('"nr1 is nr3" is equivalent to "id(nr1) == id(nr3)"')

# Type bool and None
my_null = None
my_true = True
my_false = False
# note no SyntaxWarning when checking identity
print('Bool and None objects are created when execution starts: ', my_null is None, my_true is True, my_false is False)
print('Not has precedence over or: ',
      (not False or True) is ((not False) or True),
      (not False or True) is not (not (False or True))
      )
print('Not has precedence over and: ',
      ((not False) and False) is (not False and False),
      (not False and False) is not (not (False and False))
      )
print('And has precedence over or: ',
      (False or False and True or True)  # use this to resolve homework2 !!!
      )
print()


# Simple condition evaluation
def devide(x, y):
    if y == 0:
        return None
    return x / y


print('For x=8, y=8 our function returns: ', devide(8, 8))
print('For x=8, y=0 our function returns: ', devide(8, 0))


# Python can evaluate an object for truthfulness
def just_true():
    if True:
        print('just true')


just_true()

# All objects with the exception of False, None, objects with length 0, objects with value 0, are evaluated as True
print('Empty string, 0, 0.0, 0.0j, None, and False are: ', bool(''), bool(0), bool(0.0), bool(0 + 0j), bool(None))
print('A string containing text is evaluated to: ', bool('some_text'))

# Because we can evaluate the truthfulness of objects we can also apply boolean operators on them
print('Operator "not" can be applied any objects and will return bool value ', not '')
# and and or for objects -  for got to explain it
print()

# String structure and methods

# new line is not permitted with strings using single set of quotes
str1 = u"abc\ndef\tghi"
print('The u or no char before string quotes indicate escaped character is interpreted: ', str1)
str2 = r"abc\ndef\tghi"
print('The r before string quotes indicate escaped character is not interpreted: ', str2)
print()

# new line (multiline text) is permitted with tipple set of quotes
str3 = '''
abc\tdef
123\t456
'''
str4 = r"""
abc\tdef
123\456
"""
print('Multi line text with and without escape character interpretation: ', str3, str4)
