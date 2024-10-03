import random
dict={
    "hello": ["a","b","c","d"],
    "bye": ["a","b","c","d"],
    "wef": ["a","b","c","d"],
    "aweg": ["a","b","c","d"],
    "aewrg": ["a","b","c","d"],
    "sdrthj": ["a","b","c","d"],
    "ryj": ["a","b","c","d"],
    "aerh": ["a","b","c","d"],


}


dictANS = {
    "hello": "a",
    "bye": "b",
    "wef": "d",
    "aweg": "d",
    "aewrg": "c",
    "sdrthj": "a",
    "ryj": "c",
    "aerh": "d",

}


# Question = dict.popitem()
Question = random.choice(list(dict.items()))
# options = random.choice(list(dict.values()))
print(type(Question))
print("1" + str(Question))

answer = (Question[0])

correct_answer = dictANS.get(Question[0])
print (x)
input_answer = str(input("enter the right option "))
if correct_answer == input_answer:
    print("correct answer")
else:
    print ("wrong answer")















