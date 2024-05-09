import numpy as np

# Create a dictionary to store the lexicon
lexicon = {}

# Function to update the lexicon with word transitions
def update_lexicon(current: str, next_word: str) -> None:
    # If the current word is not in the lexicon, add it with the next word
    if current not in lexicon:
        lexicon[current] = {next_word: 1}
        return  # Early return to avoid further processing

    # Get the probabilities for the current word
    options = lexicon[current]

    # Check if the next word is in the list of probabilities
    if next_word not in options:
        # Add the next word with a count of 1
        options[next_word] = 1
    else:
        # Increase the count of the existing next word
        options[next_word] += 1
    
    # Update the lexicon with the modified options
    lexicon[current] = options

# Populate the lexicon from a dataset
with open('dataset.txt', 'r') as dataset:
    for line in dataset:
        words = line.strip().split(' ')
        # Iterate over the words except for the last one
        for i in range(len(words) - 1):
            # Update lexicon with the current and next word
            update_lexicon(words[i], words[i + 1])

# Adjust probabilities in the lexicon
for word, transition in lexicon.items():
    # Normalize the probabilities to sum up to 1
    total = sum(transition.values())
    lexicon[word] = {key: value / total for key, value in transition.items()}

# Predict the next word based on user input
line = input('> ')
word = line.strip().split(' ')[-1]

# Check if the input word is in the lexicon
if word not in lexicon:
    print('Word not found')
else:
    # Get the transition probabilities for the input word
    options = lexicon[word]
    
    # Predict the next word based on probabilities
    predicted = np.random.choice(list(options.keys()), p=list(options.values()))
    
    print(f"{line} {predicted}")
