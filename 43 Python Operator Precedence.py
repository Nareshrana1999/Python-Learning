# Operator Precedence

# Operator precedence describes the order in which operations are performed.

# Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first:
print((6 + 3) - (6 + 3))


# Multiplication * has higher precedence than addition +, and therefore multiplications are evaluated before additions:
print(100 + 5 * 3)


# Left-to-Right Evaluation
# If two operators have the same precedence, the expression is evaluated from left to right.

# Addition + and subtraction - has the same precedence, and therefore we evaluate the expression from left to right:

print(5 + 4 - 7 + 3)


# Precedence Order

# The precedence order is described in the table below, starting with the highest precedence at the top:

# Operator	                                    Description
# ()	                                        Parentheses
# **	                                        Exponentiation
# +x  -x  ~x	                                Unary plus, unary minus, and bitwise NOT
# *  /  //  %	                                Multiplication, division, floor division, and modulus
# +  -	                                        Addition and subtraction
# <<  >>	                                    Bitwise left and right shifts
# &	                                            Bitwise AND
# ^	                                            Bitwise XOR
# |	                                            Bitwise OR
# ==  !=  >  >=  <  <=  is is not in not in 	Comparisons, identity, and membership operators
# not	                                        Logical NOT
# and	                                        AND
# or	                                        OR


# Challenge: Operators Basics

# Test your understanding of arithmetic, assignment, and comparison operators.

# Instructions
# Inside the editor, complete the following steps:
# Create two variables a = 15 and b = 4
# Print the result of a modulus b (the % operator)
# Print the result of a floor division b (the // operator)
# Print the result of a to the power of b (the ** operator)
# Use an assignment operator to add 10 to a (use +=)

# Create variables
a = 15
b = 4
# Print modulus
print(a % b)
# Print floor division
print(a // b)
# Print power
print(a ** b)
# Add 10 to a
a += 10
