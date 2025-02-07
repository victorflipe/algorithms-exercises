def two_numbers():
    print("======================================")
    print("|        Two numbers function        |")
    print("======================================")

    entry_list = input("Type list numbers with space between them\n")
    target_value = input("Type the target value for this list:\n")

    list_numbers = entry_list.split(' ')
    
    print(list_numbers)
    print(f'Target value: {target_value}')

    list_numbers = list(map(int, list_numbers))
    print(list_numbers)

    size_list = len(list_numbers)
    find_number = False

    for item_pre in range(size_list - 1):
        #print("pre:",item_pre)
        if find_number:
            break

        for item_pos in range(size_list - 1):
            
            if item_pos == item_pre:
                break

            sum_numbers = list_numbers[item_pre] + list_numbers[item_pos]
            
            if sum_numbers == int(target_value) and not find_number:
                find_number = True
                print("Equal numbers...")
                print(f'Sum numbers of positions: {item_pre, item_pos}')
                break
            else:
                pass
        
        


two_numbers()
