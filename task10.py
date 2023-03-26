


coins_number = int(input("Введите количество монет: "))
eagle_coin = 0
tails_coin = 0
for i in range(coins_number):
    flag_coin = int(input(
        f"если монета под номером {i + 1} лежит орлом вверх введите еденицу, если решкой вверх то ноль: "))
    if flag_coin == 0:
        tails_coin += 1
    else:
        eagle_coin += 1
if eagle_coin > tails_coin:
    print(f" Минимальное количество монет которое нужно перевернуть - {tails_coin}")
else:
    print(f" Минимальное количество монет которое нужно перевернуть - {eagle_coin}")
