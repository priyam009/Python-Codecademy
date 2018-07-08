#Write a function named substring_between_letters that takes a string named word, a single character named start, and another character named end. This function should return the substring between the first occurrence of start and end in word. If start or end are not in word, the function should return word.
#For example, substring_between_letters("apple", "p", "e") should return "pl".


def substring_between_letters(word, start, end):
  new = []
  if word.find(start) != -1 and word.find(end) != -1:
    index = 0
    for index in range(word.find(start) + 1, word.find(end)):
      new.append(word[index])
    new = ''.join(new)
    return new
  else:
    return word


print(substring_between_letters("apple", "p", "e"))

print(substring_between_letters("apple", "p", "c"))
