#A word, number, or sequence that reads the same forward and backward.
#Ex: Madam, 121, MOM, DAD, LEVEL

text = input("Enter a word: ")

reverse_word = text[::-1]

if text == reverse_word:
    print("The entered word is a palindrome")
else:
    print("The entered word is not a palindrome")
