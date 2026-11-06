from selenium import webdriver
import time

# Go to Chrome
driver = webdriver.Chrome()

# Go to Youtube
driver.get("https://www.youtube.com")

#Timer
SECONDS = 10

while True:
        for remaining in range(SECONDS, 0, -1):
            print(f"\r{remaining:2d} seconds left",flush=True)
            time.sleep(1)
#This part is just aesthetic, but doesn't look that good on the console.
        print("Checking URL...")

        print(driver.current_url)
#Assign current URL as a variable, and then print. 
        text = driver.current_url
        print(text)
#Find specific words or segements in the specific variable, and then rewind the code
        if "/shorts/" in text:
            driver.back()
            time.sleep (3)
        if "/shorts/" in text:
                driver.get("https://www.youtube.com")
                print ("HOLY SHIT IT WORKS?!")    
