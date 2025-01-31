weight = input('Weight: ')
unit = input('(L)bs or (K)g: ')


if unit.upper() == 'L' :
    weight = float(weight) * 0.45359237
    print(f'Weight in Kg: {weight:.2f}')
    
else :
    weight = float(weight) / 0.45359237
    print(f'Weight in Lbs: {weight:.2f}')