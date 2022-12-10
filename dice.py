from random import randint
def rolling(y, x):
    result = 0
    for i in range (x):
        result += randint(1, y)
    return result

possible_dices = ("D3", "D4", "D6", "D8", "D10", "D12", "D20", "D100")

roll = input('Jaki rzut ma być wykonany? Wpisz w postaci "xDy + z": ')
roll2 = roll.split('+')


for dice in possible_dices:
    position = roll.find(f'{dice}')
    if position != -1:
        break
if position == -1:
    raise Exception ('Wybrałeś nieistniejącą kostkę')
try:
    if position == 0:
        rolled = rolling(int(roll[1]), 1)
    elif position == 1:
        rolled = rolling(int(roll[2]), int(roll[0]))
except ValueError:
    print('Zły format rzutu')

try:
    if len(roll2) > 1:
        z = int(roll2[-1])
    else:
        z = 0
except ValueError:
    print('Parametr z nie jest liczbą')

final_result = rolled + z
print(f'Wynik Twojego rzutu to {final_result}')





