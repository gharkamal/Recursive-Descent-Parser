
import lex
from operator import add, sub, mul, truediv, lt, gt, eq, ne, le, ge

# For the homework, uncomment the import below

# from operator import lt, gt, eq, ne, le, ge

# List of token names - required
tokens = ('FLOAT', 'INT',
          'ADD_OP', 'MULT_OP',
          'LPAREN', 'RPAREN',
          'COMP_OP', 'BOOL',
          'AND', 'OR', 'NOT')

# global variables
token = None
lexer = None
parse_error = False