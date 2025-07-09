print('When prompted for an answer, type only the alphabet\n')

ip_file = 'question_and_answers.txt'
total_questions = 0
correct_answers = 0
with open(ip_file) as ipf:
    for line in ipf:
        if line.startswith('--> '):
            answer = line[4]
            line = line[4:]
            total_questions += 1
        print(line, end='')

        if line == '\n':
            usr_ip = input('Enter you answer: ')
            if usr_ip == answer:
                correct_answers += 1
                print('Correct answer!')
            else:
                print(f'Oops! The right choice is: {answer}')
            print('-' * 50 + '\n')

print(f'You answered {correct_answers}/{total_questions} correctly.\n')

