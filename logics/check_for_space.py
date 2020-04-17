from user_input.join_or_dash import joinOrDash

def checkForSpaceAndRemove(string):
    #If string has a space in it:
    if " " in string:
        #Ask user whether to join with dash or not:
        joinIt = int(joinOrDash())
        #If yes:
        if joinIt == 1:
            string = string.replace(" ", "-")
        #If no, replace space with no space (join strings):
        elif joinIt == 0:
            string = string.replace(" ", "")
    #Return string
    return string



if __name__ == "__main__":
    checkForSpace()