book_path = "books/frankenstein.txt"
with open(book_path) as f:
    file_text = f.read()

#returns the frankenstein text
def main(): 
    num_words = get_word_count()
    character_dict = get_character_count()
    

#returns the word count
def get_word_count():
    return len(file_text.split())

#returns the number of each character 
def get_character_count():
    lowercase_text = file_text.lower()
    character_count = {
    "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0,
    "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0,
    "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0,
    "y": 0, "z": 0
}
    for character in lowercase_text:
        if character in character_count:
            character_count[character] += 1
    return character_count
