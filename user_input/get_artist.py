def getArtist():
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print("What artist's page would you like to preview?")
    #Ask user for artist:
    artist_check_stop = False
    while artist_check_stop == False:
        artist = ""
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        artist = input("Enter Artist's Name: ")
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        #Conduct check:
        print(f"You entered: {artist}...")
        print("Is that correct?")
        check = input("Y for Yes/N for No: ")
        if check.lower() == 'y':
            #Exit loop:
            artist_check_stop = True
            return artist
        elif check.lower() == 'n':
            artist_check_stop = False
        else:
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print("That's not an option, fam...")
            artist = input("Enter Artist's Name: ")



if __name__ == "__main__":
    getArtist()
