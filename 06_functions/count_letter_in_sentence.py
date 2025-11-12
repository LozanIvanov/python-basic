def count_letter(sentence, letter):
      return sentence.count(letter)

sentence = input("Enter sentence:")
letter = input("Enter letter: ")

result=count_letter(sentence,letter)
print(f"The letter '{letter}' appears {result} time(s) in the sentence: \"{sentence}\"")