import requests
#Check for status code: 200:
def checkStatusCode(url):
    #Requests get URL:
    r = requests.get(url)
    status = r.status_code

    if status != 200:
        return False
    return True



# ---------------------------------------------------------------------------- #
if __name__ == "__main__":
    checkStatusCode()