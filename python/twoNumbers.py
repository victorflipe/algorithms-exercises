def two_numbers():
    print("======================================")
    print("|        Two numbers function        |")
    print("======================================")

    entry_list = input("Type list numbers with space between them\n")
    target_value = input("Type the target value for this list:\n")

    list_numbers = entry_list.split(' ')
    
    list_numbers = list(map(int, list_numbers))

    size_list = len(list_numbers)
    find_number = False
    positions = []

    for item_pre in range(size_list):
        #print("pre:",item_pre)
        if find_number:
            break

        for item_pos in range(size_list - 1):
            
            if list_numbers[item_pre] == list_numbers[item_pos]:
                break

            sum_numbers = list_numbers[item_pre] + list_numbers[item_pos]
            
            if sum_numbers == int(target_value) and not find_number:
                find_number = True
                
                positions.append(item_pre)
                positions.append(item_pos)
                
                break
    
    print("Equal numbers...")
    print("Positions: ", positions)
    print(f'Items: {list_numbers[positions[0]]} and {list_numbers[positions[1]]}')
        
        


two_numbers()
