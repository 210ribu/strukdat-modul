#Buat function untuk mengkonversikan ekspressi aritmatik infix menjadi ekspressi aritmatik postfix

def infixToPrefix(infix):
    output = stack()
    operator = stack()
    priority = {')': 0, '+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    for i in infix[::-1]:
        if i == ')':
            push(operator, i)
        elif i == '(':
            while peek(operator) != ')':
                push(output, pop(operator))
            pop(operator)
        elif i == '^' or i == '*' or i == '/' or i == '+' or i == '-':
            while not isEmpty(operator) and priority[i] < priority[peek(operator)]:
                push(output, pop(operator))
                if isEmpty(operator):
                    break
            push(operator, i)
        else:
            push(output, i)

    while not isEmpty(operator):
        push(output, pop(operator))

    prefix = ''
    for i in output[::-1]:
        prefix += i
    return prefix


print(infixToPrefix('A+B'))
print(infixToPrefix('(A+B)*C'))
print(infixToPrefix('(A+B)*(C-D)'))
print(infixToPrefix('A+B*C-D'))
print(infixToPrefix('A+B-C+D'))
print(infixToPrefix('A*B-C*D'))