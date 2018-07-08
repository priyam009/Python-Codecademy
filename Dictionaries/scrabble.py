#In this project, you will process some data from a group of friends playing scrabble. You will use dictionaries to organize players, words, and points.

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#Creating dictionary from letters and points
letter_to_points = {key:value for key, value in zip(letters, points)}
print(letter_to_points)
print('\n')

#Adding blank tile with value 0
letter_to_points[" "]= 0
print(letter_to_points)
print('\n')

#Defined a function to calculate total points for a word and can accomodate all upper and lower case values
def score_word(word):
  point_total= 0
  for letter in word:
    point_total += letter_to_points.get(letter.upper(), 0)
  return point_total

#Testing function score_word
brownie_points = score_word("BROWNIE")
print(brownie_points)
print('\n')

#Preparing dictonary of players and their words
player_to_words = {"player1": ["blue", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}
print(player_to_words)
print('\n')

#Iteration through the dictonary to calculate each player score

def update_points_totals():
  player_to_points = {}
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
    player_to_points[player] = player_points
  return player_to_points

  
print(update_points_totals())
print('\n')

#Adding a new word to a player
def play_word(player, word):
  new_word = []
  new_word = player_to_words.get(player)
  new_word.append(word)
  player_to_words[player]= new_word
  return player_to_words[player]

#Testing adding a new word to a player
play_word("player1", "AWESOME")
print(player_to_words)
print('\n')

#Testing updated points for each player, after adding new value
print(update_points_totals())
print('\n')
