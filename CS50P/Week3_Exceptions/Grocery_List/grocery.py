def main():
    my_list = {}
    while True:
        try:
            item = input("").upper()
            if item in my_list:
                my_list[item] += 1
            else:
                my_list [item] = 1
        except EOFError:
            print()
            break

    sorted_dict = dict(sorted(my_list.items()))
    for s in sorted_dict:
        print(sorted_dict[s], s)


main()
