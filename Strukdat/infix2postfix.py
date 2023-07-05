def stack():
    a = []
    return a
def push(a, item):
    a.append(item)
def pop(a):
    a.pop()
def isEmpty(a):
    return len(a) == 0
def peek(a):
    return a[len(a)-1] 
def size(a):
    return len(a)

def infixToPrefix(infix):
    output = stack()
    operator = stack()
    priority = {')': 0, '+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    for i in infix[::-1]:
        if i == ')':
            push(operator, i)
        elif i == '(':
            while peek(operator) != ')':
                # print(type(pop(operator)))
                # print(pop(operator))
                push(output, pop(operator))
            # for j in operator:
            #     if j != ')':
            #         push(output, j)
            pop(operator)
        elif i == '^' or i == '*' or i == '/' or i == '+' or i == '-':
            while not isEmpty(operator) and priority[i] < priority[peek(operator)]:
                push(output, pop((operator)))
                if isEmpty(operator):
                    break
            push(operator, i)
        else:
            push(output, i)

    for j in operator:
        push(output, str(j))

    prefix = ''
    for i in output[::-1]:
        prefix += str(i)
    return prefix


print(infixToPrefix('A+B'))
print(infixToPrefix('(A+B)*C'))
print(infixToPrefix('(A+B)*(C-D)'))
print(infixToPrefix('A+B*C-D'))
print(infixToPrefix('A+B-C+D'))
print(infixToPrefix('A*B-C*D'))


# print(type('*'))