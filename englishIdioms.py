idioms = {
    "Penny": ["A", "penny", "for", "your", "thoughts"],
    "Injury": ["Add", "insult", "to", "injury"],
    "Moon": ["Once", "in", "a", "blue", "moon"],
    "Grape": ["I", "heard", "it", "through", "the", "grapevine"],
    "Murder": ["Kill", "two", "birds", "with", "one", "stone"],
    "Limbs": ["It", "costs", "an", "arm", "and", "a", "leg"],
    "Grain": ["Take", "what", "someone", "says", "with", "a", "grain", "of", "salt"],
    "Fences": ["I'm", "on", "the", "fence", "about", "it"],
    "Sheep": ["Pulled", "the", "wool", "over", "his", "eyes"],
    "Lucifer": ["Speak", "of", "the", "devil"],
}

# write a for in loop to join the strings.

# assign the values in the dictionary to a variable
listOfIdioms = idioms.values()

# loop over all of the idioms in the dictionary
for word, strings in idioms.items():
    # making a variable for what should be in between the joins
    s = " "
    # join the value side of things for the word in the Dictionary
    joined = s.join(strings)
    # printing the word (aka the Key) and then the joined string of values
    print(f"{word} :", joined)
