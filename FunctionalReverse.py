import copy


def reverse(list):

    # print(list)
    new_list = copy.deepcopy(list)
    if len(new_list) == 0 or len(new_list) == 1:
        print('new list is ', new_list)
        return new_list
    else:
        first_elem = new_list.pop(0)
        print(first_elem, " of type ", type (first_elem))
        print(new_list, " of type ", type(new_list))
        rev = reverse(new_list)
        print ("reverse is ", rev, " of type ", type (rev))

        answer_list = reverse(new_list)

        answer_list.append(first_elem)

        return answer_list


my_list = list('abcd')



print(reverse(my_list))