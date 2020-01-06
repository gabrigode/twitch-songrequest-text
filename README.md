# Twitch Song Request Text
Shows NightBot's playing song on the streamer's screen via OBS.

## Tools needed
[**OBS**](https://obsproject.com/pt-br)

[**Python**](https://www.python.org/)

[**Geckodriver**](https://heroku.com/)

[**Firefox**](https://www.mozilla.org)

## Local Setup

1. Clone project repository
2. Navigate into project repository i.e `cd twitch-songrequest-txt`
3. Change the following variables with your data:
  ```
  driver = webdriver.Firefox(executable_path=r'PATH WHERE YOU PUT GECKODRIVER.EXE')
  driver.get ('YOUR SONG REQUEST URL')
  ```
 4. Install the requirements using pip: 
    `$ pip install -r requirements.txt`
  5. Run the script on your terminal or CMD: 
    `$ python twitch-songrequest-text.py`
    
## Contact

If you have any questions, something went wrong or just want to talk, feel free contact me at [**Twitter**](https://twitter.com/gabrigodes).
