def emojimaker(txt):
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
    return output


txt = input("> ")
print(emojimaker(txt))

