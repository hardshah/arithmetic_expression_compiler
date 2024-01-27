# A basic arithmetic expression interpreter to intermediate representation

Building a basic interpreter for simple arithmetic expressions using LLVM to generate intermediate representation
For more information check out the examples of usage for this simple language frontend.

examples of usage:

# Variable declaration:
To initialize and declare a variable you must use the let keyword

'let x = 5;' or 'let x = 5 * 2/(2+3);' are both valid statements to declare a variable x with a value

# Assignment
In order to assign a variable's value, it must be declared before the assignment

'let x = 5;
 x = 4;' 

 or
 
'let x = 9;
 let y = 3
 x = x/y;' 

 are both valid re-assignments of the variable x's value

# Addition and Substraction

'let x = 2 + 3;' or 'let x = 3-2;' are both valid ways to assign x a value via addition or substraction

# Multiplication and Division

'let x = 2 * 3;' or 'let x = 4/2;' are both valid ways to assign x a value via multiplication or division

# Expressions with complex order of operations

The interpreter can correctly interpret the order of operations in an arithmetic expression.

'let x = (3-2) * (((4/2)+1))/3) / (2+1-2)'

is correctly interpreted in the order of operations following basic BEDMAS rules by the parser.

