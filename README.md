# Youtube-Shorts-Blocker-Python

**_General Info_**

This is a uni assignment for a design course. I spend too much on Youtube. Over the last year I've spend too much time on Youtube shorts. I want to want to be more productive, so for the creative coding tutorial I coded a Python program that would help me spend less time on Youtube shorts.
 This is a simple Selenium project whose aim is to be a shorts blocker that rewinds the YouTube page when "/shorts/" is detected.


**_Dependencies_**

The coding environment used for this project is primarily through Python and the chrome web browser. All users who wants to run this program must have these 3 dependencies downloaded. To run this code, users must download 'selenium' through the following steps below.

_Installing Chrome_
https://www.google.com/intl/en_au/chrome/

_Installing Selenium_
(NOTE: Be sure to not include the "" in the terminal)
For Windows
1. Open cmd
2. Paste the following: "pip install selenium"
   
For Mac
1. Open Terminal
2. Paste the following: "pip3 install selenium"

**_Features_**
- Opens chrome web driver
- Redirects shorts URL to previous page. If more than 1 shorts have been watched this code will hard redirect users into [Youtube.com](https://www.youtube.com).

**__Additional Notes__**
- A limitation of Selenium is that it only monitors the single instance of the web driver and tab opened. If this tab or webdriver is closed, the program will crash, and users must manually close IDLE themselves.
