import string

# for string import string
# string.ascii_lowercase	all lowercase letters	'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase	all uppercase letters	'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters	all letters (lower + upper)	'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.digits	all digits	'0123456789'
# string.punctuation	all punctuation characters	'!"#$%&\'()*+,-./:;<=>?@[\\]^_{
# string.whitespace	all whitespace (space, tab, newline)	' \t\n\r\x0b\x0c'

def count_words(sentence):
    for ch in string.punctuation:
        sentence = sentence.replace(ch, "")
    return len(sentence.split())

sentence = input("Enter a sentence: ")

result = count_words(sentence)
print(f"The sentence contains {result} word(s).")