import random
import string



class SecretCode():
    #text = input(str(f"enter the text"))

    
    def __init__(self,text): 
        # self.words = text.split(" ")
        self.words = text.split(" ")
        self.code=[]
        try:  
            word = self.words
            print(word)
            # word = word.split("")
            for word in self.words:
                if len(word) > (3) :
                    FirstAlphabet=word[0]
                    word=word[1:]+FirstAlphabet 
                    #self.words[0]="".join(word)      
                    random_prefix = ''.join(random.choice(string.ascii_letters) for _ in range(3))
                    random_suffix = ''.join(random.choice(string.ascii_letters) for _ in range(3))
                    word = random_prefix + word + random_suffix
                    print(word)

                else :
                    word=word[::-1]
                    random_prefix = ''.join(random.choice(string.ascii_letters) for _ in range(3))
                    random_suffix = ''.join(random.choice(string.ascii_letters) for _ in range(3))
                    word = random_prefix + word + random_suffix
                    print (word)                  
        except:
            print("error")

        self.code = " ".join(self.words)
        print(self.code) #return code
        

    def output_code(self):
        # modified_string = " ".join(self.words)
        print(f"{self.code} ")

# text = input(str(f"enter the text\n"))
text = input(f"enter the text\n")
OutputCode = SecretCode(text)
OutputCode.output_code()
