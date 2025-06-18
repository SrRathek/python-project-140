import operator
import random

RULE = 'What is the result of the expression?'

OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}


def generate_round():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    op_symbol, op_func = random.choice(list(OPERATIONS.items()))

    question = f'{num1} {op_symbol} {num2}'
    correct_answer = str(op_func(num1, num2))
    return question, correct_answer
