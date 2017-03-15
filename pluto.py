
import lex
from operator import add, sub, mul, truediv, lt, gt, eq, ne, le, ge

# For the homework, uncomment the import below

# from operator import lt, gt, eq, ne, le, ge

# List of token names - required
tokens = ('FLOAT', 'INT',
          'ADD_OP', 'MULT_OP',
          'LPAREN', 'RPAREN', 'COMP_OP', 'BOOL',
          'AND', 'OR', 'NOT')

# global variables
token = None
lexer = None
parse_error = False

# Regular expression rules for simple tokens
# r indicates a raw string in Python - less backslashes
t_ADD_OP = r'\+|-'
t_MULT_OP = r'\*|/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMP_OP = r'\<|>|<=|>=|==|!='
#t_BOOL = r'True|False'
t_AND = r'and'
t_OR = r'or'
t_NOT = r'not'



# Regular expression rules with some action code
# The order matters
def t_FLOAT(t):
    r'\d*\.\d+|\d+\.\d*'
    t.value = float(t.value)  # string must be converted to float
    return t


def t_INT(t):
    r'\d+'
    t.value = int(t.value)  # string must be converted to int
    return t

def t_BOOL(t):
    r'(True|False)'
    mapping = {'True': True, 'False': False}
    t.value = mapping[t.value]
    return t


# For the homework, you will add a function for boolean tokens

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Lexical error handling rule
def t_error(t):
    print(t)
    global parse_error
    parse_error = True
    print("ILLEGAL CHARACTER: {}".format(t.value[0]))
    t.lexer.skip(1)


# For homework 2, add the comparison operators to this dictionary
SUPPORTED_OPERATORS = {'+': add, '-': sub, '*': mul, '/': truediv, '<=': le, '>=': ge, '<': lt,
                       '>': gt, '==': eq, '!=': ne}


def command():
    """
    <command> ::= <arith_expr>
    """
    result = bool_expr()
    if not parse_error:  # no parsing error
        if token:  # if there are more tokens
            print("in command if more tokens")
            error('END OF COMMAND OR OPERATOR')
        else:
            print(str(result))


def bool_expr():
    """
    <bool_expr> -> <bool_term> {OR <bool_term>}
    """
    result = bool_term()
    while token and token.type == 'OR':
        match()
        operand = bool_term()
        match()
        if not parse_error:
            result = (result or operand)
    return result

def bool_term():
    """
    <bool_term> -> <not_factor> {AND <not_factor>}
    :return:
    """
    result = not_factor()
    while token and token.type == 'AND':
        match()
        operand = not_factor()
        if not parse_error:
            result = result and operand
    return result


def not_factor():
    """
    <not_factor> -> {NOT} <bool_factor>
    :return:
    """
    if token and token.type == 'NOT':
         while token and token.type == 'NOT':
                count = 0
                count = count + 1
                match()
         operand = bool_factor()
         if not parse_error:
             if(count % 2 == 0):
                 result = operand
                 return result
             else:
                 result = not operand
                 return result
    else:
         result = bool_factor()
         return result