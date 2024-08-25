#Task

#Alphabet Class

#Create the Alphabet class

#Create the __init__() method, inside of which two attributes will be defined: 1) lang - language and 2) letters - list of letters. The initial values of the properties are taken from the method's input parameters.

#Create the printe(t) metod, which will print the alphabet letters to the console.

#Create the letters_num() method, which will return the number of letters in the alphabet.

#EngAlphabet Class

#Create the EngAlphabet class by inheriting from the Alphabet class.

#Create the __init__() method, inside of which the parent method __init__() will be called. The language designation (e.g., En) and a string consisting of all the letters of the alphabet will be passed to it as parameters.

#Add a private static attribute _letters_num, which will store the number of letters in the alphabet.

#Create the is_en_letter() method, which will take a letter as a parameter and determine whether this letter belongs to the English alphabet.

#Redefine the letters_num() method - let it return the value of the _letters_num attribute in the current class.

#Create a static method example(), which will return an example text in English.

#Tests (main)

#Create an object of the EngAlphabet class.

#Print the alphabet letters for this object.

#Output the number of letters in the alphabet.

#Check if the letter 'F' belongs to the English alphabet.

#Check if the letter 'Щ' belongs to the English alphabet.

#Output an example text in English. 

import random 
import time 



letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
ukr_lett = ["А", "Б", "В", "Г", "Ґ", "Д", "Е", "Є", "Ж", "З", "И", "І", "Ї", "Й", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т", "У", "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ь", "Ю", "Я"]





class Alphabet:

    def __init__(self,lang, letters):
        self.language = lang #language
        self.letters = letters #letters
    def print(self):
        print("".join(self.letters))

    def letters_num(self):
        return len(self.letters)
    

    def letters_num(self):
        return len(self.letters)

class EngAlphabet(Alphabet):
        def __init__(self):

            super().__init__("Eng", letters)

        def is_en_letter(self, letter):
            return letter.upper() in self.letters


        def example():
        
          return "If you need help, call me!."
class UkrAlphabet(Alphabet):
    def __init__(self):

        super().__init__("Ukr", ukr_lett)
    
    def is_en_letter(self, letter):
            return letter.upper() in self.letters

    
    def example():
        return "Якщо потрібна допомога, поклич мене!."
        
alphabet1 = Alphabet("English", letters)






def choose_language():
    while True:
        choose_alphabet = int(input("Choose language:\n1 - English\n2 - Ukrainian\n"))
        if choose_alphabet == 1:
            
            
            eng_alphabet = EngAlphabet()
            eng_alphabet.print()  
            print(eng_alphabet.letters_num())  
            print(eng_alphabet.is_en_letter('F'))  # True
            print(eng_alphabet.is_en_letter('Щ'))  # False
            print(EngAlphabet.example())   
            next_language = int(input("Would you like to check next language?\n1 - Yes\n2 - No\n"))
            if next_language == 1:
                choose_alphabet = 2
            else:
                print ("Thanks bye!")
                break
        elif choose_alphabet == 2:
            ukr_alphabet = UkrAlphabet()
            ukr_alphabet.print()
            print(ukr_alphabet.letters_num())  
            print(ukr_alphabet.is_en_letter('F'))  # False
            print(ukr_alphabet.is_en_letter('Щ'))  # True
            print(UkrAlphabet.example())
            next_language = int(input("Чи хочете ви подивитись на наступну мову?\n1 - Так\n2 - Ні\n"))
            if next_language == 1:
                choose_alphabet = 1
            else:
                print ("Thanks bye!")
                break   
choose_language()        