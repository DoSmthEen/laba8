'''
виведіть на екран елементи лінійного масиву (заданий користувачем) у
зворотному порядку;
Васильченко Даниїл Назарович 122 А
'''
import numpy as np

while True:
    try:
        print((np.array([int(input('Введіть елемент: ')) for i in range(int(input('Довжина массиву: ')))]))[::-1])
        #проходимо по массиву з кроком -1, тобто з кінця до початку і виводимо результат
        break
    except ValueError:
        print("Введіть число!")

