import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

TWITTER_ID = os.environ["TWITTER_ID"]
TWITTER_PASSWORD = os.environ["TWITTER_PASSWORD"]
PROMISED_DOWN = 250
PROMISED_UP = 250

class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.set_window_size(1200, 900)

        self.down = None
        self.up = None

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        start_button = self.driver.find_element(By.CLASS_NAME, "js-start-test")
        start_button.click()

        sleep(40)

        download_speed = self.driver.find_element(By.CLASS_NAME, "download-speed")
        self.down = float(download_speed.text)
        upload_speed = self.driver.find_element(By.CLASS_NAME, "upload-speed")
        self.up = float(upload_speed.text)

        print(f"{self.down} / {self.up}")

    def tweet_at_provider(self):
        self.driver.get("https://x.com/i/flow/login?input_flow_data=%7B%22requested_variant%22%3A%22eyJsYW5nIjoiamEifQ%3D%3D%22%7D")
        sleep(4)

        id_input = self.driver.find_element(By.NAME, "text")
        id_input.send_keys(TWITTER_ID)
        next_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]')
        next_button.click()
        sleep(1)

        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys(TWITTER_PASSWORD)
        login_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button')
        login_button.click()
        sleep(4)

        message_textarea = self.driver.find_element(By.CLASS_NAME, "public-DraftEditor-content")
        message_textarea.send_keys(f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?")
        sleep(1)

        post_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
        post_button.click()


