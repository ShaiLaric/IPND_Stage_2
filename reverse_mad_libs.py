# Parts to fill in
fill_ins  = ["___1___","___2___","___3___","___4___","___5___","___6___","___7___","___8___"]

# Game paragraphs
easy_game = "Once upon a time, there was a "
medium_game = ""
hard_game = ""

# Answers
easy_answers = ["thing 1", "thing 2", "thing 3", "thing 4", "thing 5", "thing 6", "thing 7", "thing 8"]
medium_answers = ["thing 1", "thing 2", "thing 3", "thing 4", "thing 5", "thing 6", "thing 7", "thing 8"]
hard_answers = ["thing 1", "thing 2", "thing 3", "thing 4", "thing 5", "thing 6", "thing 7", "thing 8"]

# Check if a word in parts_of_speech is a substring of the word passed in.
def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None



# Everything below this is from the regular Mad Libs game
        
# Plays a full game of mad_libs. A player is prompted to replace words in ml_string, 
# which appear in parts_of_speech with their own words.  
def play_game(ml_string, parts_of_speech):    
    replaced = []
    ml_string = ml_string.split()
    for word in ml_string:
        replacement = word_in_pos(word, parts_of_speech)
        if replacement != None:
            user_input = raw_input("Type in a: " + replacement + " ")
            word = word.replace(replacement, user_input)
            replaced.append(word)
        else:
            replaced.append(word)
    replaced = " ".join(replaced)
    return replaced
    
print play_game(test_string1, parts_of_speech1) 