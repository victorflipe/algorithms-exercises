
def fizzbuzz():
    print("==========================")
    print("|        Fiz Buzz        |")
    print("==========================")

    array_number = list(range(1, 101))
    

    for num in array_number:
        if num % 3 == 0 and num % 5 ==0:
            print(f'{num}: Fizz Buzz')
        elif num % 3 == 0:
            print(f'{num}: Fizz')
        elif num % 5 == 0:
            print(f'{num}: Buzz')
        else:
            print(num)


fizzbuzz()