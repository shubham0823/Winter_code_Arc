import random
import string
text = input(str(f"enter the text"))

class SecretCode():
    
    def __init__(self) -> None:   
        word = text.split(" ")
        if (len > 3):
            FirstAlphabet=[0]
            word.append(FirstAlphabet[0])        
            word.remove(FirstAlphabet[0])

            return word
            
    #def LeftRandom():
        word.join(random.choice(string.ascii_letters) for x in range(0))
        word.random_char(5)
            
    #def RightRandom():
        word.join(random.choice(string.ascii_letters) for x in range(-1))
        word.random_char(5) 

print(text)
