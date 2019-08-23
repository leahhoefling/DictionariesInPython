"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
and then Add several more words and their definitions

"""
word_definitions = {
    "happy": "a good feeling",
    "sad": "not feeling happy",
    "mad": "an angry feeling",
    "thankful": "feeling gratitude",
    "tired": "needing sleep"
}

"""
Use square bracket lookup to get the definition two
words and output them to the console with `print()`
"""
print(word_definitions["happy"])
print(word_definitions["sad"])


"""
Loop over dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""
print("------------")
for (word, defin) in word_definitions.items():
    print(f"The definition of {word} is {defin}")
