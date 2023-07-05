def display(early, goals):
    if  early== 'A' and goals == 'B' :
        early = A
        goals = B
    elif early == 'A' and goals == 'C' :
        early = A
        goals = C
    elif early == 'B' and goals == 'A' :
        early = B
        goals = A
    elif early == 'B' and goals == 'C' :
        early = B
        goals = C
    elif early == 'C' and goals == 'A' :
        early = C
        goals = A
    elif early == 'C' and goals == 'B' :
        early = C
        goals = B
    goals.insert(0, early.pop(0))
    print('A: ')
    for i in A:
        print(f'|{i}|')
    print('B: ')
    for i in B:
        print(f'|{i}|')
    print('C: ')
    for i in C:
        print(f'|{i}|')

def towers(n, early, help, goals):
    if n == 1:
        print(f'Lempengan - 1 dari {early} ke {goals}')
        display(early, goals)
    else:
        towers(n-1, early, goals, help)
        print(f'Lempengan - {n} dari {early} ke {goals}')
        display(early, goals)
        towers(n-1, help, early, goals)

A = [1, 2, 3, 4]
B = []
C = []
for i in A:
    print('|{i}|')
towers(4, "A", "B", "C")