



def remove_duplicates(input_list):
    return list(dict.fromkeys(input_list))


if __name__ == "__main__":
    my_list = [1, 2, 3, 2, 1, 4, 5, 4]
    print("Original list:", my_list)
    print("List after removing duplicates:", remove_duplicates(my_list))