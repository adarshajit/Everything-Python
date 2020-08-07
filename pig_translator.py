sentence = input("Enter your sentence: ")
words = sentence.split(" ")
new_words =[]
for word in words:
    if word[0] in "aeiou":
        new_word = word + "yay"
        new_words.append(new_word)
    else:
        vowelpos = 0
        for letter in word:
            if letter not in "aeiou":
                vowelpos += 1
            else:
                break
        cons = word[:vowelpos]
        new_word = word[vowelpos:] + cons + "ay"
        new_words.append(new_word)

output = " ".join(new_words)
print(output)
