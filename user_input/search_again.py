def searchAgain():
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print("Would you like to preview a different artists page?")
    proper_answer = False
    while proper_answer == False:
        answer = ""
        answer = input("Y for Yes/N for No: ")
        if answer.lower() == "y":
            proper_answer = True
            response = True
            return response
        elif answer.lower() == "n":
            proper_answer = True
            response = False
            return response
        else:
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print("That's not an option!")
            answer = input("Y for Yes/N for No: ")



if __name__ == "__main__":
    searchAgain()