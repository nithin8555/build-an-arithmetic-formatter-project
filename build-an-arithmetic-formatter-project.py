def arithmetic_arranger(problems, show_answers=False):
    arranged_problems = ''
    if len(problems) > 5:
        arranged_problems = "Error: Too many problems."
        return arranged_problems
    
    operators = []
    for problem in problems:
        array = problem.split()
        operators.append(array[1])

    for operator in operators:
        if operator in ['*','/']:
            arranged_problems = "Error: Operator must be '+' or '-'."
            return arranged_problems
        
    numbers = []
    for problem in problems:
        array = problem.split()
        numbers.append(array[0])
        numbers.append(array[2])

    for number in numbers:
        if not number.isdigit():
            arranged_problems = 'Error: Numbers must only contain digits.'
            return arranged_problems
        elif len(number) > 4:
            arranged_problems = 'Error: Numbers cannot be more than four digits.'
            return arranged_problems
        
    answers = []
    top_line = ''
    bottom_line = ''
    answer_row = ''
    lines = ''

    for i in range(0, len(numbers), 2):
        num1 = int(numbers[i])
        num2 = int(numbers[i+1])
        operator = operators[i // 2]

        if operator == "+":
            result = num1 + num2
        else:
            result = num1 - num2
        answers.append(result)

        space_width = max(len(numbers[i]),len(numbers[i+1])) + 2
        top_line += numbers[i].rjust(space_width)
        bottom_line += operator + numbers[i+1].rjust(space_width - 1)
        lines += '-' * space_width

        if i != len(numbers) - 2:
            top_line += ' ' * 4
            bottom_line += ' ' * 4
            lines += ' ' * 4

    for i in range(len(answers)):
        space_width = max(len(numbers[2 * i]), len(numbers[2 * i + 1])) + 2
        answer_row += str(answers[i]).rjust(space_width)

        if i != len(answers) - 1:
            answer_row += ' ' * 4

    if show_answers:
        arranged_problems = '\n'.join((top_line, bottom_line,lines, answer_row))
    else:
        arranged_problems = '\n'.join((top_line, bottom_line, lines))
    return arranged_problems

print(arithmetic_arranger(["3801 - 2", "123 + 49"]))
