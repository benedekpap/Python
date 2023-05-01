def arithmetic_arranger(problems, show_result=None):
    # Check if too many problems are supplied
    if len(problems) > 5:
        return "Error: Too many problems."

    # Initialize lists for top, bottom, operator, and results strings
    top_list = []
    bottom_list = []
    operator_list = []
    line = []
    result_list = []

    # Loop through each problem
    for i, problem in enumerate(problems):
        # Split problem into its components
        components = problem.split()
        # Check if operator is valid
        if components[1] not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        # Check if operands contain only digits
        if not components[0].isdigit() or not components[2].isdigit():
            return "Error: Numbers must only contain digits."

        # Check if operands have four or fewer digits
        if len(components[0]) > 4 or len(components[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Append operands, operator, and result to respective lists
        length = []
        for component in components:
            length.append(int(len(component)))
        line.append(max(length))
        top_list.append(components[0].rjust((line[i])+2))
        bottom_list.append(components[2].rjust(line[i]))
        operator_list.append(components[1])
        if components[1] == "+":
            result = int(components[0]) + int(components[2])
        else:
            result = int(components[0]) - int(components[2])
        result_list.append(str(result).rjust((line[i])+2))


    # Combine lists into formatted string
    if show_result == True:
        arranged_problems = top_list[0]
        for i in range(1, len(problems)):
            arranged_problems += "    " + top_list[i]
        arranged_problems += "\n"
        arranged_problems += operator_list[0] + ' ' + bottom_list[0]
        for i in range(1, len(problems)):
            arranged_problems += "    " + operator_list[i] + ' ' + bottom_list[i]
        arranged_problems += "\n"
        arranged_problems += str("-" *(line[0] + 2))
        for i in range(1, len(problems)):
            arranged_problems += "    " +  str("-" *(line[i] + 2))
        arranged_problems += "\n"
        arranged_problems += result_list[0]
        for i in range(1, len(problems)):
            arranged_problems += "    " + result_list[i]
        return arranged_problems
    else:
        arranged_problems = top_list[0]
        for i in range(1, len(problems)):
            arranged_problems += "    " + top_list[i]
        arranged_problems += "\n"
        arranged_problems += operator_list[0] + ' ' + bottom_list[0]
        for i in range(1, len(problems)):
            arranged_problems += "    " + operator_list[i] + ' ' + bottom_list[i]
        arranged_problems += "\n"
        arranged_problems += str("-" *(line[0] + 2))
        for i in range(1, len(problems)):
            arranged_problems += "    " +  str("-" *(line[i] + 2))

        return arranged_problems

gg = arithmetic_arranger(["3801 - 2", "3452 + 1117", "4 - 194"])
print(gg)
