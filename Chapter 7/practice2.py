# write a function thake takes a string and return the count of vowels and consonants separately.

def CountVowelsAndConsonants(userInput):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0

    for char in userInput:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count
userInput = input("Enter a string: ")
vowels, consonants = CountVowelsAndConsonants(userInput)
print(f"Vowels: {vowels}, Consonants: {consonants}")