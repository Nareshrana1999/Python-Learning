# Strings
x = "Hello World"
#display x:
print(x)
#display the data type of x:
print(type(x))

y = "Naresh Rana"
print(y)
print(type(y))


# Strings
x = 20
#display x:
print(x)
#display the data type of x:
print(type(x))

# Floats
x = 2.0
print(x)
print(type(x))

# Complex
x = 3+4j
print(x)
print(type(x))

#list
x = ["apple", "banana", "cherry"]
print(x)
print(type(x))

#tuple
x = ("apple", "banana", "cherry")
print(x)
print(type(x))

# Comparison Overview BlW List and Tuple

# Feature :              List (list)                                                 Tuple (tuple)
# Mutability  :          Mutable (add, remove, change items)                         Immutable (read-only)
# Syntax      :          Square brackets [1, 2, 3]                                   Parentheses (1, 2, 3)
# Memory      :          More memory (allocates extra space for resizing)            Less memory (fixed size block)
# Methods     :          Many - append(), pop(), remove(), sort()                    Few count(), index()
# Dictionary Keys   :    No (unhashable)                                             Yes (if elements inside are also immutable)
# Semantic Intent   :    Homogeneous data (items of the same type)                   Heterogeneous data (items of different types)


# Range

x = range(6)
print(x)
print(type(x))

x = range(10 - 20)
print(x)
print(type(x))

x = range(10*9)
print(x)
print(type(x))

#Dictionary
x = {"name" : "John", "age" : 36}
print(x)
print(type(x))

x = {"Fruit" : "Apple", "Price" : 200}
print(x)
print(type(x))

#Set
x = set(("apple", "banana", "cherry"))
print(x)
print(type(x))

# Comparison Overview between List and Tuple

# Feature :              Dictionary (dict)                                           Set (set)
# Data Format :          Key-value pairs {key: value}                                Single elements {item1, item2}
# Duplicates  :          Duplicate keys forbidden (values can duplicate)             Duplicate elements forbidden entirely
# Access Method  :       MethodBy key my_dict[key]                                   Membership testing item in my_set
# Syntax      :          {key: value, key2: value2}                                  {item1, item2, item3}
# Empty Init   :         empty_dict = {}                                             empty_set = set()
# Core Use Case   :      Mapping data for quick lookups                              Filtering duplicates and math operations



x = frozenset(["apple", "banana", "cherry"])
print(x)
print(type(x))

y = frozenset(("Cake", "Coke", "Rice"))
print(y)
print(type(y))

z = frozenset({'Cricket', 'Tennis', 'Football'})
print(z)
print(type(z))


# A frozenset is simply an immutable version of a Python set.
# While a standard set can be modified after creation, a frozenset is completely read-only.

# Standard Set vs. Frozenset

# Feature                Set (set)                              Frozenset (frozenset)
# Mutability         :   Mutable (add/remove items)             Immutable (read-only)
# Syntax             :   {1, 2, 3}                              frozenset([1, 2, 3])
# Hashable           :   No (cannot be a dict key)              Yes (can be a dict key)
# Nesting            :   Cannot contain other sets              Can be nested inside other sets
# Modifying Methods  :   Has .add(), .remove(), .pop()          No modifying methods available


# Boolean   either True or False
x = bool(0)
print(x)
print(type(x))

x = bool(1)
print(x)
print(type(x))

print(bool(0))
print(bool(1))

print(bool("Hello"))  # Output: True  (Non-empty string)
print(bool(100))      # Output: True  (Non-zero number)

print(bool(""))       # Output: False (Empty string)
print(bool(0))        # Output: False (Zero)

# "Truthy" vs. "Falsy" Values

# In Python, every object can be evaluated in a boolean context (like an if statement).
# Python evaluates objects as either "Truthy" (behaves like True) or "Falsy(behaves likeFalse`).

# 1. Falsy ValuesThese are the only values that Python evaluates as False:
# False
# None
# Zero of any numeric type (0, 0.0, 0j)
# Empty sequences and collections ("", [], (), {}, set())

# 2. Truthy ValuesAbsolutely everything else evaluates to True.
# This includes non-empty strings, non-empty lists, and any non-zero number (even negative numbers like -5).



# Byte
x = bytes(5)
print(x)
print(type(x))

# ByteArray
mybytes = bytearray([25, 55, 100])
print(mybytes)
print(type(mybytes))

# MemoryView
x = memoryview(bytes(10))
print(x)
print(type(x))


# In Python, bytes is an immutable sequence of integers ranging from 0 to 255
# used to represent raw binary data (such as files, network packets, or images).

# Key Characteristics
# Immutable: Once created, you cannot change individual bytes within the sequence.
# Format: Represented by the prefix b before a string literal (e.g., b'hello').
# Values: Only ASCII characters or hex escape sequences (\x00 to \xff) are allowed inside the literal.


# None
x = None
print(x)
print(type(x))

# In Python, None is a special constant used to represent the absence of a value or a null status.
# It is a unique object, meaning it is not the same as 0, False, or an empty string "".

# Key Characteristics
# Single Instance (Singleton): There is only ever one instance of None in a running Python program.
# Every variable assigned to None points to the exact same spot in memory.
# Its Own Type: It belongs to its own data type called NoneType.
# Default Return Value: If a function does not explicitly use a return statement, it automatically returns None