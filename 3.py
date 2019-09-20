import math
# Weight = int(raw_input("Enter the change number: "))

def provideDenominations(Weight, change=[1, 5, 10, 25, 50, 100]):
    weight = Weight
    number_of_coins = 0
    denominations = []
    while(weight > 0):
        maximum = list()
        for ch in change:
            if ch < weight:
                maximum.append(math.floor(weight/ch))
            else:
                maximum.append(ch)
        
        max_index = maximum.index(min(maximum))
        max_coin = change[max_index]
        for index, w in enumerate(maximum):
            if w == maximum[max_index]:
                if change[index] > max_coin:
                    max_coin = change[index]
                

        weight = weight - (max_coin * maximum[max_index])
        number_of_coins += maximum[max_index]
        denominations.append((maximum[max_index], max_coin))

    return number_of_coins, denominations

coins42, denominations42 = provideDenominations(42)
print('Number of coins for 42: ', coins42)
print('Denominations of change for 42: ', denominations42)
print("-----------------------------------------------------------------------")
coins1728, denominations1728 = provideDenominations(1728)
print('Number of coins for 1728: ', coins1728)
print('Denominations of change for 1728: ', denominations1728)
print("-----------------------------------------------------------------------")
coins42_change, denominations42_change = provideDenominations(42, [1, 8, 20, 30, 80, 200])
print('Number of coins for 42 with input denominations: ', [1, 8, 20, 30, 80, 200], ' is: ', coins42_change)
print('Denominations of change for 42 with input denominations: ', [1, 8, 20, 30, 80, 200], ' is:', denominations42_change)
print("-----------------------------------------------------------------------")
coins1728_change, denominations1728_change = provideDenominations(1728, [1, 8, 20, 30, 80, 200])
print('Number of coins for 1728 with input denominations: ', [1, 8, 20, 30, 80, 200], ' is: ',coins1728_change)
print('Denominations of change for 1728 with input denominations: ', [1, 8, 20, 30, 80, 200], ' is: ',denominations1728_change)
print("-----------------------------------------------------------------------")

coins1728_change, denominations1728_change = provideDenominations(121, [1, 10, 50, 70, 100])
print('Number of coins for 121 with input denominations: ', [1, 10, 50, 70, 100], ' is: ',coins1728_change)
print('Denominations of change for 121 with input denominations: ', [1, 10, 50, 70, 100], ' is: ',denominations1728_change)


    
