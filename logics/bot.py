from selenium import webdriver
from .check_status import checkStatusCode
from fake_user.fake_user import fakeUserWait

def play_song(track_href):
    #Set driver to the GeckoDriver:
    driver = webdriver.Firefox()
    #Soundcloud base url:
    base_url = 'https://www.soundcloud.com'
    #Track url to play:
    track_url = f"{base_url}{track_href}"

    #If status = 200:
    if checkStatusCode(track_url):
        #Open window to track:
        driver.get(track_url)
        driver.set_window_size(1120, 750)
        #Find play button and click
        driver.find_element_by_class_name('playButton').click()
        #Use fake user wait to simulate a "Listen" between 10-25 secs:
        fakeUserWait()
        #Close browser window:
        driver.close()
    


if __name__ == "__main__":
    bot()