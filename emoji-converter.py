txt = input("> ")
sentence = txt.split(" ")
emoji = {
    ":)" : "😀",
    ":(" : "🥲",
    ">_<" : "😣",
    ":P" : "😋"
}

output = ""

for word in sentence:
    output += emoji.get(word, word) + " "
print(output)