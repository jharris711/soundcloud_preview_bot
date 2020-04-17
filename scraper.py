import requests
from bs4 import BeautifulSoup
from time import sleep
from logics.check_status import checkStatusCode
from logics.bot import play_song
from logics.check_for_space import checkForSpaceAndRemove
from user_input.get_artist import getArtist
from user_input.join_or_dash import joinOrDash
from user_input.search_again import searchAgain


def scrapeAndPlay():
    #Start program loop:
    the_program_is_running = True
    while the_program_is_running:
        #Get desired artist from user:
        artist = getArtist().lower()
        #Join for url:
        artist = checkForSpaceAndRemove(artist)
        #Set headers:
        headers = {'User-Agent': 'Mozilla/5.0'}
        #Set url of artist's Soundcloud page:
        url = f'https://soundcloud.com/{artist}'
        #Make http request to artist's Soundcloud with Requests package:
        response = requests.request("GET", url, headers=headers)
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(f"Now scraping: {url}")
        print(" ")
        #Send response's text through Beautiful Soup:
        soup = BeautifulSoup(response.text, "html.parser")
        #Save the name of all visible list items to results:
        track_names = soup.find_all("h2", {'itemprop': "name"})
        #Set list as count for while loop:
        count = len(track_names)
        while count > 0:
            #Iterate the track names list:
            for t in track_names:
                track_href = t.find('a')['href']
                url = f"https://www.soundcloud.com{track_href}"
                #Check url for status = 200:
                if checkStatusCode(url):
                    try:
                        play_song(track_href)
                    #Pass key errors:
                    except KeyError:
                        pass
                count -= 1
                #Count messages:
                if count == 1:
                    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                    print("Playing the last song on the page.")
                elif count == 0:
                    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                    print("Done playing songs on this page.")
                else:
                    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                    print(f"{count} songs left.")
            #Sleep some between requests:
            sleep(10)
        
        #When the list is finished:
        if count == 0:
            #Ask user if they want to search again:
            search_again = searchAgain()
            #If user answers no:
            if search_again == False:
                #Stop program:
                the_program_is_running = False
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                print("See Ya!")





if __name__ == "__main__":
    scrapeAndPlay()