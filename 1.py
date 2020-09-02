def op1(A, a, b):
    A.insert(a, b)


def op2(A, a):
    A.pop(a-1)


def op3(A):
    print(A)


n = int(input('m个操作：'))
B = []
A = []
for i in range(n):
    print('数字中间用空格隔开')
    arr = input('指令')
    num = [int(n) for n in arr.split()]
    B.append(num)
    if B[i][0] == 1:
        op1(A, B[i][1], B[i][2])
    if B[i][0] == 2:
        op2(A, B[i][1])
    if B[i][0] == 3:
        op3(A)
