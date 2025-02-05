from palindrome import check_palindrome
from sortNumbers import ordened_numbers

def main():
    option_selected = ""
    while option_selected != "0":
        print("--------------------------------------")
        print("|        Exercises in Python         |")
        print("--------------------------------------")
        
        print("Select an option:")
        print("     1- Palindrome Exercise")
        print("     2- Order numbers without sort function")
        print("     0- Exit")
        print("\n")

        option_selected = input("Enter an option or type 0 to exit: ")

        if option_selected == "0":
            print("Exiting the program...")
            break

        if option_selected == "1":
            check_palindrome()
        
        if option_selected == "2":
            ordened_numbers()
        

if __name__ == "__main__":
    main()