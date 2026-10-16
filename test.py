from selenium import webdriver
import time

# Go to Chrome
driver = webdriver.Chrome()

# Go to Youtube
driver.get("https://www.youtube.com")

#Timer
SECONDS = 10

try:
    while True:
        for remaining in range(SECONDS, 0, -1):
            print(f"\r{remaining:2d} seconds left", end="", flush=True)
            time.sleep(1)

        print("Checking URL...")

        print(driver.current_url)

        text = driver.current_url
        print(text)

        if "/shorts/" in text:
            driver.back()
            print ("HOLY SHIT IT WORKS?!")
except KeyboardInterrupt:
    print("\nStopped.")
