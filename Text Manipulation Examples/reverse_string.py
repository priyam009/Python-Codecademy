#Write a function named reverse_string that has a string named word as a parameter. The function should return word in reverse.


def reverse_string(word):
  word_reverse = []
  for letter in word:
    word_reverse.append(letter)
    
  word_reverse.reverse()
  word_reverse = ''.join(word_reverse)
  return word_reverse
  

print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print