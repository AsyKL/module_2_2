number_1 = int(input('Введите первое число от 3 до 20:'))
s = []
for i in range(1,21):
    for j in range(1,i):
        if number_1 % (i + j) == 0:
            k = str(j) + str(i)
            s.append(int(k))
s = sorted(s)
new_s = ''
for i in s:
    new_s += str(i)
print(new_s)