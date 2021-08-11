def arithmetic_arranger(problems, result=False):

    arranged_problems = ""

    if len(problems) <= 5:

        temp = ["   ", "   ", "   ", "   "]

        for item in problems:
            section = item.split()

            if str(section[1]) != "+" and str(section[1]) != "-" and str(section[1]) != "/" and str(section[1]) != "*":
                return "Error: Operator must be '+', '-', '*' or '/'."

            if len(section[0]) > 6 or len(section[2]) > 6:
                return "Error: Numbers cannot be more than six digits."

            try:

                max_len = len(str(max(int(section[0]), int(section[2])))) + 2
                holder = ""

                if str(section[1]) == "+":
                    holder = str(int(section[0]) + int(section[2])).rjust(max_len) + "    "
                elif str(section[1]) == "-":
                    holder = str(int(section[0]) - int(section[2])).rjust(max_len) + "    "
                elif str(section[1]) == "*":
                    holder = str(int(section[0]) * int(section[2])).rjust(max_len) + "    "
                elif str(section[1]) == "/":
                    holder = str(round(float(section[0]) / float(section[2]), 2)).rjust(max_len) + "    "

                if result:
                    temp[3] += holder

                temp[0] += section[0].rjust(max_len) + "    "
                temp[1] += section[1].ljust(max_len - len(section[2])) + section[2] + "    "
                temp[2] += ("-" * max_len) + "    "

            except ValueError:

                return "Error: Numbers must only contain digits."

            arranged_problems = "\n".join(temp)

    else:
        return "Error: Too many problems."

    return arranged_problems
