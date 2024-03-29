#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
    for i in range(list_length):
        try:
            ans = (my_list_1[i] / my_list_2[i])
        except (TypeError, FloatingPointError):
            ans = 0
            print("wrong type")
        except ZeroDivisionError:
            ans = 0
            print("division by 0")
        except IndexError:
            ans = 0
            print("out of range")
        finally:
            new.append(ans)
    return (new)
