from os import startfile
import pyautogui as p
import time


start = time.time()
end = (start + 60)


def click():
    # find the cookie and get its location
    # click that location 100 time
    location = p.locateCenterOnScreen('assets/cookie.png')
    print("locateCenterOnScreen:",location)
    p.moveTo(location)
    p.click()
    pass

def upgrades():
    # find the upgrades and get all of there locations 
    #click the location by one click, starting from the lowest, then move up

    location = p.locateCenterOnScreen('assets/wizardtower.png')
    print("locateCenterOnScreen:",location)
    p.moveTo(location)
    p.click()


    location = p.locateCenterOnScreen('asset/wizardtower.png')
    print("locateCenterOnScreen:",location)
    p.moveTo(location)
    p.click()

    location = p.locateCenterOnScreen('assets/temple.png')
    print("locateCenterOnScreen:",location)
    p.moveTo(location)
    p.click()

    location = p.locateCenterOnScreen('assets/bank.png')
    print("locateCenterOnScreen:",location)
    p.moveTo(location)
    p.click()

    location = p.locateCenterOnScreen('assets/factory.png')
    print("locateCenterOnScreen:",location)
    p.moveTo(location)
    p.click()
    
    location = p.locateCenterOnScreen('assets/mine.png')
    print("locateCenterOnscreen:",location)
    p.moveTo(location)
    p.click()

    location = p.locateCenterOnScreen('assets/farm.png')
    print("locateCenterOnscreen:",location)
    p.moveTo(location)
    p.click()

    location = p.locateCenterOnScreen('assets/grandma.png')
    print("locateCenterOnscreen:",location)
    p.moveTo(location)
    p.click()

    location = p.locateCenterOnScreen('assets/cursor.png')
    print("locateCenterOnscreen:",location)
    p.moveTo(location)
    p.click()
    pass

def store():
    # find the store's first 5 upgrades
    #click each of them once, move from left store upgrade to 5th upgrade on right
    location = p.locateCenterOnScreen('assets/reinforcedindexfinger.png')
    print("locateCenterOnScreen:",location)
    p.moveTo(location)
    p.click()

    location = p.locateCenterOnScreen('assets/carpaltunnelpreventioncream.png')
    p.moveTo(location)
    p.click()

    location = p.locateCenterOnScreen('assets/coconutcookies.png')
    print("locateCenterOnscreen:",location)
    p.moveTo(location)
    p.click()

    location = p.locateCenterOnScreen('assets/almondcookies.png')
    print("locateCenterOnScreen:",location)
    p.moveTo(location)
    p.click()

    location = p.locateCenterOnScreen('assets/hazelnutcookies.png')
    print("locateCenterOnscreen:",location)
    p.moveTo(location)
    p.click()

    location = p.locateCenterOnScreen('assets/walnutcookies.png')
    print("locateCenterOnscreen:",location)
    p.moveTo(location)
    p.click()

    location = p.locateCenterOnScreen('assets/goldenidols.png')
    print("locateCenterOnscreen:",location)
    p.moveTo(location)
    p.click()
    pass


def main():
    p.confirm('run')
    while True:
        
        click()
        upgrades()
        store()







main()
