# Chapter 3 — Functions
# Concept 2: Parameters and arguments

# --- Single parameter ---
# 'name' is the parameter: a local placeholder that receives the argument.
# Each time we call greet(), 'name' takes on whatever value we pass in.

def greet(name):
    print('Hello, ' + name + '!')

greet('Spencer')   # argument: 'Spencer'
greet('Alice')     # argument: 'Alice'
greet('Bob')       # argument: 'Bob'


# --- Multiple parameters ---
# Functions can accept more than one parameter, separated by commas.
# Arguments are matched to parameters by position (left to right).

def describe_pet(animal, name):
    print(name + ' is a ' + animal + '.')

describe_pet('dog', 'Rex')    # animal='dog', name='Rex'
describe_pet('cat', 'Luna')   # animal='cat', name='Luna'


# --- Default parameter values ---
# You can give a parameter a default value using '='.
# If the caller doesn't supply that argument, the default is used instead.
# If they do supply one, it overrides the default.
#
# Rule: parameters WITH defaults must come AFTER parameters without defaults.

def greet_with_title(name, title='Friend'):
    print('Hello, ' + title + ' ' + name + '!')

greet_with_title('Spencer', 'Mr.')   # overrides default: title='Mr.'
greet_with_title('Alice')            # uses default:    title='Friend'
