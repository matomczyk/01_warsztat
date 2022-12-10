from random import sample

lista = [i+1 for i in range(49)]
totek = sample(lista, 6)
#print(totek)
user_nums = []
i = 0
trafione = 0
while i < 6:
    try:
        kolejna = int(input('Podaje liczbę: '))
        if kolejna in user_nums:
            print('Już podałeś tę liczbę!')
        else:
            if 0 < kolejna < 50:
                user_nums.append(kolejna)
                i += 1
            else:
                print('Liczba musi należec do zakresu 1-49')
    except ValueError:
        print('To nie jest liczba!')

user_nums.sort()
print(user_nums)

for number in user_nums:
    if number in totek:
        trafione += 1
    else:
        pass

if trafione > 2:
    print(f'Gratulacje, trafiłeś {trafione}!')
else:
    print('Niestety, tym razem się nie udało')






