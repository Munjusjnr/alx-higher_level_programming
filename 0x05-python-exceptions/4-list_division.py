#!/usr/bin/python3
# This function divides element by element 2 lists
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                print("out of range")
                new_list.append(0)
            else:
                val = my_list_1[i]
                hal = my_list_2[i]

                if not isinstance(val, (int, float)) or \
                        not isinstance(hal, (int, float)):
                    print("wrong type")
                    new_list.append(0)
                elif hal == 0:
                    print("division by 0")
                    new_list.append(0)
                else:
                    result = val / hal
                    new_list.append(result)
        except Exception:
            new_list.append(0)
        finally:
            pass
    return new_list
