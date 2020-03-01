contoh 
1. 

colors=[9.1,8.8,7.8]
for color in colors:
    print(round(color))

2.loop over conditional

colors=[11,34.1,98.2,43,45.1,54,54]

for color in colors:
    if type (color) is int and color > 50:
        print(color)

3. loop over dictionary

phones_numbers={"jonh smith":"+082268065911","marry simpons":"082165272149"}

for key,value in phones_numbers.items():
    print("{} has a phone number {}".format(key,value))

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for key,value in phone_numbers.items():
    print(value.replace("+","00"))
4. 

def sentence_maker(phrase):
    interrogative = ("how","what","why")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogative):
        return "{}?".format(capitalized)
    else:
        return "{},".format(capitalized)

print(sentence_maker("how are you"))


results=[]
while True:
    user_input = input ("say something : ")
    if user_input == "\end":
        break
    else:
        results.append(sentence_maker(user_input))

print(results)
