print('Pomyśl liczbę od 1 do 1000, a ja ją zgadnę w max 10 próbach')
min = 0
max = 1000
wynik = ''

while wynik != 'zgadłeś':
    guess = int((max - min) / 2) + min
    print(f'Zgaduję {guess}, zgadłem?')
    wynik = input('')
    if wynik == 'za dużo':
        max = guess
    elif wynik == 'za mało':
        min = guess
    elif wynik == 'zgadłeś':
        pass
    else:
        print('Nie oszukuj')
print('Wygrałem!')


