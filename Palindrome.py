while True:
    word=input("Enter a word: ")
    print(f"You have entered the word:  {word}")
    new_word= word[::-1]
    if word.lower()== new_word.lower():
        print(f"The word {word} is a palindrome.")
    else:
        print(f"The word {word} is not a palindrome")