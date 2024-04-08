'''
Script to convert integers into Roman numerals
'''

#Tuples with corresponding ints and roman numerals
rom_num_list = [(1000, 'M'),(900, 'CM'),(500, 'D'),(400, 'CD'),(100, 'C'),(90, 'XC'),(50, 'L'),(40, 'XL'),(10, 'X'),(9, 'IX'),(8, 'VIII'),(7, 'VII'),(6, 'VI'),(5, 'V'),(4, 'IV'),(3,'III'),(2, 'II'),(1, 'I')]


def int_to_roman(num):
    '''Function that takes a given integer and converts to roman numerals'''

    roman = ''

    while num > 0:
        for i, r in rom_num_list:
            if num >= i:
                roman += r
                num -= i
    
    return roman


#Take an integer from the user
number = int(input("Please enter a number: "))



#print the outcome
print(str(number) + " in roman numerals is: " + str(int_to_roman(number)))
    





    


    