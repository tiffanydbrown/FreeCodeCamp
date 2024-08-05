def arithmetic_arranger(problems, display_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    
    first_line = ""
    second_line = ""
    dashes_line = ""
    answers_line = ""

    for i, problem in enumerate(problems):
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid problem format."

        operand1, operator, operand2 = parts

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."
        
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        if operator == '+':
            result = str(int(operand1) + int(operand2))
        else:
            result = str(int(operand1) - int(operand2))
        
        width = max(len(operand1), len(operand2)) + 2
        top_operand = operand1.rjust(width)
        bottom_operand = operator + operand2.rjust(width - 1)
        dashes = '-' * width
        answer = result.rjust(width)

        if i > 0:
            first_line += "    "
            second_line += "    "
            dashes_line += "    "
            if display_answers:
                answers_line += "    "
        
        first_line += top_operand
        second_line += bottom_operand
        dashes_line += dashes
        if display_answers:
            answers_line += answer

    if display_answers:
        arranged_problems = f"{first_line}\n{second_line}\n{dashes_line}\n{answers_line}"
    else:
        arranged_problems = f"{first_line}\n{second_line}\n{dashes_line}"
    
    return arranged_problems

# Example usage:
print(arithmetic_arranger(["3801 - 2", "123 + 49"]))
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
