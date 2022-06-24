def check_letter(letter):
    if letter.lower() == 'y':
        return "letter is not vowel or consonant"
    elif letter.lower() == 'a' or letter.lower() == 'e' or letter.lower(
    ) == 'i' or letter.lower() == 'o' or letter.lower() == 'u':
        return "letter is vowel"
    else:
        return "letter is consonant"


letter = input("enter a letter: ")
print(check_letter(letter))