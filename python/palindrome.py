# Make a program to make a palindrome

def is_palindrome(word):
    transformed_word = word.replace(" ", "").lower()
    return word == transformed_word[::-1]
    
def check_palindrome():
 
    print("-------------------")
    print("Palindrome Checker")
    print("-------------------")

    word = ""
 
    while word != "0":
        print("Insert a word (or type 0 to quit the program)...")
        word = input()

        if word == "0":
            print("Exiting the solution...")
            break

        if is_palindrome(word):
            print("Very goood!! It's a palindrome\n")
        else:
            print("Not is a palindrome\n")