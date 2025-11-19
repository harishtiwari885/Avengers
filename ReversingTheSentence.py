def roggers(s):
    word = s.split()
    reversed_words = word[::-1]
    reversed_String = " ".join(reversed_words)
    return reversed_String

s = input("Enter the Sentence")
result = roggers(s);
print(result)