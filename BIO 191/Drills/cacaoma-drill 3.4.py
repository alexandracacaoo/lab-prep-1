str = input("Enter a word: ")

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiouy"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("e") and word[-2] not in vowels:  # Check if the word ends with "e" and the previous character is not a vowel
        count -= 1
    if count == 0:
        count = 1
    return count

print("Syllables:", syllable_count(str))

#This code is a slightly modified version of the code from https://stackoverflow.com/questions/46759492/syllable-count-in-python