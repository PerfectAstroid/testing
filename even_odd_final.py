def iq_test(numbers):
    list_of_numbers = numbers.split(" ")
    #print(list_of_numbers)
    if int(list_of_numbers[0]) % 2 != 0 and int(list_of_numbers[1]) % 2 == 0:
        if int(list_of_numbers[2]) % 2 == 0:
            return 1
        else:
            return 2
    elif int(list_of_numbers[0]) % 2 == 0 and int(list_of_numbers[1]) % 2 != 0:
        if int(list_of_numbers[2]) % 2 == 0:
            return 2
        else:
            return 1

    elif int(list_of_numbers[0]) % 2 == 0 and int(list_of_numbers[1]) % 2 == 0:
        count = 0
        for items in list_of_numbers:
            count += 1
            if int(items) % 2 != 0:
                return count
            else: pass

    else:
        count = 0
        for items in list_of_numbers:
            count += 1
            if int(items) % 2 == 0:
                return count
            else: pass

print(iq_test("15 20 30 "))
