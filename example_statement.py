price = 100000000
has_ggod_cradit = True

if has_ggod_cradit:
    down_payment = 0.1 * price
    
else:
    down_payment = 0.02 * price
    
print(f'Down payment: {down_payment}')