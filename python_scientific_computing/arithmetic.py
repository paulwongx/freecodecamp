def arithmetic_arranger(problems, *args):
    line1 = ''
    line2 = ''
    line3 = ''
    line4 = ''
    for idx, p in enumerate(problems):
        s = p.split(' ')
        operator = s[1]
        longest = max(len(s[0]),len(s[2])) # 3

        if len(problems) > 5:
            print('Error: Too many problems.')
            return('Error: Too many problems.')
        elif not s[0].isnumeric() or not s[2].isnumeric():
            print('Error: Numbers must only contain digits.')
            return('Error: Numbers must only contain digits.')
        elif operator != '+' and operator != '-':
            print('Error: Numbers must only contain digits.')
            return("Error: Operator must be '+' or '-'.")
        elif len(s[0]) > 4 or len(s[2]) > 4:
            print('Error: Numbers cannot be more than four digits.')
            return('Error: Numbers cannot be more than four digits.')

        spacing = longest + 1 # 4
        line1 += ' ' * (1 + spacing - len(s[0]))
        line1 += s[0]
        if idx != len(problems)-1: # add space if not the last problem
            line1 += '    ' # four spaces between each problem

        line2 += operator
        line2 += ' ' * (spacing - len(s[2]))
        line2 += s[2]
        if idx != len(problems)-1: # add space if not the last problem
            line2 += '    ' # four spaces between each problem

        line3 += '-' * (longest+2)
        if idx != len(problems)-1:
            line3 += ' ' * 4

        ans = str(eval(p))
        line4 += ' ' * (1 + spacing - len(ans))
        line4 += ans
        if idx != len(problems)-1: # add space if not the last problem
            line4 += '    ' # four spaces between each problem

    if args != () and args[0] == True:
        output = line1 + '\n' + line2 + '\n' + line3 + '\n' + line4
        # print(line1,line2,line3,line4, sep='\n')
    else:
        output = line1 + '\n' + line2 + '\n' + line3
        # print(line1,line2,line3, sep='\n')

    print(output)
    return output



# arithmetic_arranger(["32 + 698", "3801 * 2", "45 + 43", "123 + 49"], True)

# arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])
arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"])