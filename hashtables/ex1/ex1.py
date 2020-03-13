#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    
    
    for i in range(len(weights)):
        hash_table_insert(ht, weights[i], i)
        check_val = hash_table_retrieve(ht, limit - weights[i])
        # print('checkval', check_val)
        if check_val is not None:
            
            dbl_check = hash_table_retrieve(ht, limit - weights[check_val])
            # print(dbl_check)
            if dbl_check is not None:
                if check_val > dbl_check:
                    return (check_val, dbl_check)
                elif check_val < dbl_check:
                    return (dbl_check, check_val)
                elif check_val == dbl_check:
                    return (dbl_check + 1, check_val)

    
    
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
