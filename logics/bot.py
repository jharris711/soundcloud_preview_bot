from selenium import webdriver
from .check_status import checkStatusCode
from fake_user.fake_user import fakeUserWait

def play_song(track_href):
    #Soundcloud base url:
    base_url = 'https://www.soundcloud.com'
    #Track url to play:
    track_url = f"{base_url}{track_href}"

    
    did_it_play = False
    while did_it_play == False:
        #Open window to track:
        #If status = 200:
        if checkStatusCode(track_url):
            try:
                #Set driver to the GeckoDriver:
                driver = webdriver.Firefox()
                #Open window to track:
                driver.get(track_url)
                driver.set_window_size(1120, 750)
                #Find play button and click
                driver.find_element_by_class_name('playButton').click()
                #Use fake user wait to simulate a "Listen" between 10-25 secs:
                fakeUserWait()
                #Close browser window:
                did_it_play = True
                driver.close()
            except:
                #Close browser window:
                print('Connection closed/Could not connect. Moving on...')
                driver.close()
    


if __name__ == "__main__":
    bot()