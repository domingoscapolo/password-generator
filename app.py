import random

chars = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 
'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 
'z', '-', '+', '_', '#', '$']

password = ''

for x in range(0, 7):
    index =  random.randint(0, len (chars) - 1)
    password += chars[index]


print('A senha gerada é: '+ password)



