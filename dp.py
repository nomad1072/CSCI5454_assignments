import math

def provideDenominations(weight, denominations=[1, 10, 50, 70, 100]):
    output_list = [99999999] * (weight + 1)
    output_list[0] = 0
    print(len(output_list))
    print('Denominations: ', denominations)
    for denom in denominations:
        for index, number in enumerate(output_list):
            if index-denom < 0:
                pass
            else:
                output_list[index] = min(output_list[index], 1 + output_list[index-denom])

    return (output_list[weight])



coins42 = provideDenominations(42)
print('Number of coins for 42: ', coins42)
print("-----------------------------------------------------------------------")
coins1728 = provideDenominations(1728)
print('Number of coins for 1728: ', coins1728)
print("-----------------------------------------------------------------------")
coins42_change = provideDenominations(42, [1, 8, 20, 30, 80, 200])
print('Number of coins for 42 with input denominations: ', [1, 8, 20, 30, 80, 200], ' is: ', coins42_change)
print("-----------------------------------------------------------------------")
coins1728_change = provideDenominations(1728, [1, 8, 20, 30, 80, 200])
print('Number of coins for 1728 with input denominations: ', [1, 8, 20, 30, 80, 200], ' is: ',coins1728_change)
print("-----------------------------------------------------------------------")



    
