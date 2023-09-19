from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import config
import time
class InternetSpeedTwitterBot:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        go_button = self.driver.find_element(By.CLASS_NAME, "start-text")
        go_button.click()
        time.sleep(60) # Adjust based on how long it takes to do the test
        self.down = self.driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span").text
        self.up = self.driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span").text

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/")
        time.sleep(2)

        # First page - clicking sign in
        signin_button = self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a/div/span/span")
        signin_button.click()
        time.sleep(2)

        # Second page - entering username and clicking next
        username = self.driver.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
        username.send_keys(config.email)
        username.send_keys(Keys.ENTER)
        time.sleep(2)

        # Third page - entering username because unusual activity
        unusual_login = self.driver.find_element(By.NAME, "text")
        unusual_login.send_keys(config.username)
        unusual_login.send_keys(Keys.ENTER)
        time.sleep(2)

        # Fourth page - entering password and clicking login
        password = self.driver.find_element(By.NAME, 'password')
        password.send_keys(config.password)
        password.send_keys(Keys.ENTER)
        time.sleep(5)

        # Writing tweet
        write_tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        write_tweet.send_keys(f"Hey Internet provider, my internet speed is {self.down} down/{self.up} up? This isn't near the 500/20 I was promised...")
        post_tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/span/span')
        post_tweet.click()


