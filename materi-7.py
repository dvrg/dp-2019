colors=[9.1,8.8,7.8]
for color in colors:
    print(round(color))


colors=[11,34.1,98.2,43,45.1,54,54]

for color in colors:
    if type (color) is int and color > 50:
        print(color)


phones_numbers={"jonh smith":"+082268065911","marry simpons":"082165272149"}

for key,value in phones_numbers.items():
    print("{} has a phone number {}".format(key,value))


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

