#16. Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
#В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X


n = int(input('Введите размер списка: '))
list_n = input('Введите элементы списка через пробел: ').split()
arr = list(map(int, list_n))
x = int (input('Введите число х: '))
count = 0
for i in range(n):
    if arr[i] == x:
        count += 1
print(f'Число {x} встречается в списке А {count} раз.')

#второй вариант
n = int(input('Введите размер списка: '))
list_n = input('Введите элементы списка через пробел: ').split()
arr = list(map(int, list_n))
x = int (input('Введите число х: '))
print(f'Число {x} встречается в списке А {arr.count(x)} раз.')




#18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

import random
n = int(input('Введите размер массива: '))
x = int(input('Введите искомое число x: '))
arr = []
for i in range(n):
    arr.append(random.randrange(n))
print(arr)
def nearval(arr, number):
    return min(arr, key=lambda x: abs(number - abs(x))) 
print(f'Ближайшее к {x} число в массиве: {nearval(arr, x)}')





#20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; 
# K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; 
# Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.


letters_english = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'D', 'G', 'B', 'C', 'M', 'P', 'F', 'H', 'V', 'W', 'Y', 'K', 'J', 'X', 'Q', 'Z']
points_english  = [ 1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   2,   2,   3,   3,   3,   3,   4,   4,   4,   4,   4,   5,   8,   8,   10,  10]
letters_russian = ['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т', 'Д', 'К', 'Л', 'М', 'П', 'У', 'Б', 'Г', 'Ё', 'Ь', 'Я', 'Й', 'Ы', 'Ж', 'З', 'Х', 'Ц', 'Ч', 'Ш', 'Э', 'Ю', 'Ф', 'Щ', 'Ъ']
points_russian  = [ 1,   1,   1,   1,   1,   1,   1,   1,   1,   2,   2,   2,   2,   2,   2,   3,   3,   3,   3,   3,   4,   4,   5,   5,   5,   5,   5,   8,   8,   8,   10,  10,  10]
letters = letters_english + letters_russian
points  = points_english  + points_russian
index = 0
sum = 0
word = input("Введите слово : ").upper()
output_word = list(word)
for char in letters:
    index += 1
    for i in range(len(output_word)):
        if output_word[i] == char:
            point_index = points[index-1]
            sum = sum + point_index
print(sum)


#второй вариант
import re
def isCyrillic(text):
	return bool(re.search('[а-яА-Я]', text))
points_en = {1:'AEIOULNSTR',
      	2:'DG',
      	3:'BCMP',
      	4:'FHVWY',
      	5:'K',
      	8:'JZ',
      	10:'QZ'}
points_ru = {1:'АВЕИНОРСТ',
      	2:'ДКЛМПУ',
      	3:'БГЁЬЯ',
      	4:'ЙЫ',
      	5:'ЖЗХЦЧ',
      	8:'ШЭЮ',
      	10:'ФЩЪ'}
text = input("Введите слово : ").upper()
if isCyrillic(text):
	print(sum([k for i in text for k, v in points_ru.items() if i in v]))
else:
	print(sum([k for i in text for k, v in points_en.items() if i in v]))