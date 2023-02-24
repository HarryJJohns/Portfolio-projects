# set up spacy

import spacy
nlp = spacy.load('en_core_web_md')

# read movies from txt file into a dictionary

# Create blank dictionary to fill
movies = {}

# Open the file and readlines to get lines to split in a for loop
file = open('movies.txt','r')
file_lines = file.readlines()

# For loop to add file line by line to a dictionary
for line in file_lines:
    line = line.split(":")
    movies[line[0]] = nlp(line[1])

# Close the file (best practice)
file.close()

# Create a comparison movie to compare to the values from the dictionary

planet_hulk = nlp('''
Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, 
the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator''')

# Iterate tyhrough dictionary and compare descriptions to planet hulk, save in three variables to display at the end
score = 0
winner = ""
for key in movies:
    description = nlp(movies[key])
    similar = description.similarity(planet_hulk)

    if similar > score:
        score = similar
        winner = description
        winner_title = key

# Output results
output =  "---------------\n"
output += f"The most similar movie is: {winner_title}\n"
output += f"With a score of: {score}\n"
output += f"Description of the most similar movie:\n{winner}"
output +=  "---------------"

print(output)