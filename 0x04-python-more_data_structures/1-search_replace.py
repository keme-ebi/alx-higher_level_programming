#!/usr/bin/python3
def search_replace(my_list, search, replace):
    #create a new list to copy original list
    #check for the element in the list
    #if it's there, replace it, else return old list
    new_list = my_list.copy()

    if search in new_list:
        for i in range(len(new_list)):
            if new_list[i] == search:
                new_list[i] = replace
        return new_list
    else:
        return my_list
