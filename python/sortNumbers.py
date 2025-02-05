
def bubble_sort(enter_numbers):
    
    size_list = len(enter_numbers)

    for pos_x in range(size_list - 1):
        for pos_y in range(size_list - 1 - pos_x):
            if enter_numbers[pos_y] > enter_numbers[pos_y+1]:
                aux = enter_numbers[pos_y]
                enter_numbers[pos_y] = enter_numbers[pos_y+1]
                enter_numbers[pos_y+1] = aux


    print("==================================")
    print("|         Numbers sorted         |")
    print("==================================")
    print(f'List ordened: {enter_numbers}\n\n')


def ordened_numbers():
    enter_numbers = input("Enter a sequence of numbers separated by spaces\n")
    list_numbers = enter_numbers.split(' ')
    list_numbers = list(map(int, list_numbers))
    
    bubble_sort(list_numbers)

