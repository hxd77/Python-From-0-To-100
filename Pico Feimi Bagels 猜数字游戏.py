import random

NUM_DIGITS=3
MAX_GUESSES=10

def main():
    print('''Bagels, a deductive logic game. 
    By hxd @hxd77.xyz
    
    I am thinking of a {}-digit number with no repeated digits.
    Try to guess what it is. Here are some clues:
    When I say:    That means:
        Pico       One digit is correct but in the wrong position.
        Fermi      One digit is correct and in the right position.
        Bagels     No digit is correct.
    For example, if the secret number was 248 and your guess was 843, the 
    clues would be Fermi Pico.'''.format(NUM_DIGITS))
    while True: #主循环
        #secretNum存储了玩家所要猜测的秘密数字
        secretNum=getSecretNum()
        print('I have thought up a number.')
        print('You  have {} guesses to get it.'.format(MAX_GUESSES))

        numGuesses=1
        while numGuesses <= MAX_GUESSES:
            guess=''
            #保持循环，直到玩家输入正确的猜测数字
            while len(guess)!=NUM_DIGITS or not guess.isdecimal():#isdecimal判断字符串 guess 是否只包含十进制数字（0–9），并且长度大于 0
                print('Guess #{}: '.format(numGuesses))
                guess=input('> ')

            clues=getClues(guess, secretNum)
            print(clues)
            numGuesses+=1

            if guess==secretNum:
                break   #玩家猜对了数字，则结束当前循环
            if numGuesses>MAX_GUESSES:
                print('You ran out of guesses.')
                print('The answer was {}.'.format(secretNum))

        #询问玩家是否想再玩一次
        print('Do you want to play again? (yes or no)')
        if not input('>').lower().startswith('y'):  #如果用户输入的内容不是以字母 y（不区分大小写）开头，就执行 if 下面的代码。
            break
        print('Thanks for playing!')


def getSecretNum():
    '''返回唯一一个长度为NUM_DIGITS且由随机数字组成的字符串'''
    numbers=list('0123456789') #创建一个包含0-9的列表
    random.shuffle(numbers)#将原列表打乱然后返回

    #获取秘密数字列表中的前NUM_DIGITS位数字
    secretNum=''
    for i in range (NUM_DIGITS):
        secretNum+=numbers[i]
    return secretNum

def getClues(guess, secretNum):
    '''返回一个由Pico、Fermi和Bagels组成的字符串，用于猜测一个三位数'''
    if guess==secretNum:
        return 'You got it!'

    clues=[]

    for i in range (len(guess)):
        if guess[i]==secretNum[i]:
            #正确的数字位于正确的位置
            clues.append('Fermi')
        elif guess[i] in secretNum:
            #正确的数字不在正确的位置
            clues.append('Pico')
    if len(clues)==0:
        return 'Bagels'     #没有正确的数字
    else:
        #将clues列表按字母顺序排序，使其不会泄露数字的信息
        clues.sort()
        #返回一个由clues列表中所有元素组成的字符串
        return ' '.join(clues)

if __name__ == '__main__':
    main()
