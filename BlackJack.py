#BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
#blackjack(5,6,7) --> 18
#blackjack(9,9,9) --> 'BUST'
#blackjack(9,9,11) --> 19

#two different ways to do the same thing

def black_jack(num1,num2,num3):
    if num1+num2+num3 == 21:
        print('BLACKJACK!!')
    elif num1+num2+num3 > 21:
       print('BUST!')
    else:
       return num1+num2+num2
    
print(black_jack(10,10,1))


