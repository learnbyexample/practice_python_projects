import random

print('When prompted for an answer, type only the alphabet\n')

ip_file = 'question_and_answers.txt'
question_blocks = open(ip_file).read().rstrip().split('\n\n')
random.shuffle(question_blocks)

total_questions = 0
correct_answers = 0
for block in question_blocks:
    total_questions += 1
    question, *choices = block.split('\n')
    random.shuffle(choices)
    print(f'{total_questions}) {question[question.find(" ")+1:]}')
    for choice, option in zip(choices, 'abcdefghij'):
        if choice.startswith('--> '):
            choice = choice[4:]
            answer = option
        print(f'{option}) {choice[choice.find(" ")+1:]}')

    usr_ip = input('\nEnter you answer: ')
    if usr_ip == answer:
        correct_answers += 1
        print('Correct answer!')
    else:
        print(f'Oops! The right choice is: {answer}')
    print('-' * 50 + '\n')

print(f'You answered {correct_answers}/{total_questions} correctly.\n')

