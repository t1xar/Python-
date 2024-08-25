#Використовуючи функцію, напишіть програму на Python. (ready)
#Функція має приймати дані від користувача. (ready)
#Програма повинна генерувати випадкове число від 1 до 100 і зберігати його в змінній. (ready)
#Користувачеві пропонується вгадати число. Якщо припущення користувача правильне, програма повинна надрукувати «Вітаємо! Ви вгадали правильне число». і вихід. (ready)
#Якщо припущення користувача неправильне, програма має надати зворотний зв’язок, як-от «Занадто високо» або «Занадто низько», і дозволити користувачеві вгадати ще раз. (ready)
#Користувач повинен мати максимум 5 спроб, щоб вгадати правильне число.(ready)
#Після 5 невдалих спроб програма повинна надрукувати «Вибачте, у вас закінчилися спроби. (ready)
# Правильний номер був [правильний номер]» і вийти.(ready)

import random 



def check_input():
    if name != str("") and name != 1:
        print ("Почнемо: ",name)
        list_of_players()
        randomaizer(name)
def list_of_players(): # безкорисна функція яка вводить кожного юзера хто грав в гру !
    content = "names.txt"
    with open("names.txt", 'r',encoding='utf-8') as file:
        content = file.read().splitlines()        
    if name not in content:
        with open("names.txt", 'a',encoding='utf-8') as file:
            file.write( '\n' + name + '\n')        
def randomaizer(name):
    number = random.randint (1,100)
    tryes = 0
    
    while tryes != 5  :
        tryes = tryes + 1 
        print (f"Ваша {tryes}, спроба ")
        if tryes == 5 :
            print ("!!!! Ваша остання спроба !!!!")
            
        player_check_number = int(input ("Вгадайте число від 1 - 100: "))
        if player_check_number == number:
            print(f"Правильне число було: |{number}| == |{player_check_number}| ")
            print ("Ви відповіли правильно вітаємо з перемогою!!!")
            if tryes == 5 and player_check_number != number or tryes == 5 and player_check_number == number :
                next_try_for_player = int(input("Чи бажаєте ви зіграти ще раз ?\n1 = Так\n2 = Ні\n"))
                print ("\n\n\n")    
                if next_try_for_player == 1:
                    print ("\n\n\n")  
                    check_input()
                elif next_try_for_player == 2:
                    print ("\n\n\n\n\n\n\n\n")
                    print("Дякуємо за час проведений разом !")
                    
                    break
            
            
        elif player_check_number > number: 
            print (f"|Ваше число занадно високе| {player_check_number} > ?")
        elif player_check_number < number: 
            print (f"|Ваше число занадно низьке| {player_check_number} < ?")
        else :
            print("|ПОМИЛКА|")
        if tryes == 5 and player_check_number != number:
            print ("Вибачте, у вас закінчилися спроби")
            print(f"Правильне число було: |{number}| не дорівнює |{player_check_number}| ")
        if tryes == 5 and player_check_number != number or tryes == 5 and player_check_number == number or tryes == 4 and player_check_number == number or tryes == 3 and player_check_number == number or tryes == 2 and player_check_number == number or tryes == 1 and player_check_number == number :
            next_try_for_player = int(input("Чи бажаєте ви зіграти ще раз ?\n1 = Так\n2 = Ні\n"))
            print ("\n\n\n")    
            if next_try_for_player == 1:
                print ("\n\n\n")  
                check_input()
            if next_try_for_player == 2:
                print ("\n\n\n\n\n\n\n\n\n\n\n\n")
                
                print("Дякуємо за час проведений разом !")
            break
        
name = input ("Введіть ваше ім'я: ")
check_input()


