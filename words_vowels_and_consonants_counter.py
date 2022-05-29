#Word, Vowels and Consonants Counter
user_input = input ("Type a sentence: ")
vowel_count = 0
consonant_count = 0
words = user_input.split ()
vowels = ["a","e","i","o","u"]
consonants = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
for letter in user_input.lower ():
    if letter in vowels:
        vowel_count +=1
    elif letter in consonants:
        consonant_count +=1
print (f"Vowels: {vowel_count}")
print (f"Consonants: {consonant_count}")
print (f"Words:", len(words))
