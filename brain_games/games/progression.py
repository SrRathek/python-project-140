import random

RULE = 'What number is missing in the progression?'

def generate_round():
    length = random.randint(5, 10)
    start = random.randint(1, 20)
    step = random.randint(2, 10)

    progression = []
    for i in range(length):
        next_number = start + step * i
        progression.append(next_number)

    hidden_index = random.randint(0, length - 1)
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = '..'
    question = ' '.join(map(str, progression))
    return question, correct_answer
