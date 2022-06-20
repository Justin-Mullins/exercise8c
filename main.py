'''

Exercise 8c:

Which is the longest word in a text file?

'''

file = open("text.txt","r")
text = file.read().split(' ')
longest = 0 
index = 0
counter = 0
for word in text:
    if longest < len(word):
        longest = len(word)
        index = counter
    counter += 1
print(f'Longest Word: {text[index]}')