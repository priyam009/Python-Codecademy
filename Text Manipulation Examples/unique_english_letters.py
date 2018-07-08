#Write a function called unique_english_letters that takes the string word as a parameter. The function should return the total number of unique letters in the string. Uppercase and lowercase letters should be counted as different letters.
#We've given you a list of every uppercase and lower case letter in the English alphabet. It will be helpful to include that list in your function.

def unique_english_letters(word):
  temp_lst = ""
  letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
  count = 0
  #letters = letters.split()
  
  for letter in word:
    if letters.find(letter) != -1and temp_lst.find(letter) == -1:
      temp_lst += letter
      count += 1
     
  return count
      
  
print(unique_english_letters("mississippi"))

print(unique_english_letters("Apple"))