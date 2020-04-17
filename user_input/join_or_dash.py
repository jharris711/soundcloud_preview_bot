def joinOrDash():
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print("Join name with or without dash in url?")
    res = input("'1 for dash/0 for no dash': ")
    proper_answer = False
    while proper_answer:
        if res == "1" or res == "0":
            proper_answer = True
            return res
        else:
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print("That's not an option, fam...")


if __name__ == "__main__":
    joinOrDash()