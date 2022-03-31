from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

from time import sleep

class MeroShare:

    def __init__(self) -> None:
        s = Service('/home/voidarchive/chromedriver_linux64/chromedriver')
        self.driver = webdriver.Chrome(service=s)
        self.driver.maximize_window()
    
    def login(self, dp_name, user_name, password):
        self.driver.get("https://meroshare.cdsc.com.np/#/login")
        sleep(1)
        self.driver.find_element(By.CLASS_NAME,'select2-selection__placeholder').click()
        # Depository Participant
        depository_Participant = self.driver.find_element(By.XPATH,'/html/body/span/span/span[1]/input')
        depository_Participant.send_keys(dp_name, Keys.ENTER)
        # Username
        username = self.driver.find_element(By.ID,'username')
        username.send_keys(user_name)
        # Password
        user_password = self.driver.find_element(By.ID,'password')
        user_password.send_keys(password,Keys.ENTER)

    def find_ipo(self):
        sleep(1)
        self.driver.get('https://meroshare.cdsc.com.np/#/asba')
        sleep(1)
        self.driver.find_element(By.CLASS_NAME,'btn-issue').click()
    
    def apply_ipo(self, applied_unit, crn):
        sleep(1)
        # Select Bank
        bank = self.driver.find_element(By.ID, 'selectBank')
        bank.click()
        bank.send_keys(Keys.ARROW_DOWN)
        bank.send_keys(Keys.ARROW_DOWN)
        bank.send_keys(Keys.ENTER)


        applied_kitta = self.driver.find_element(By.ID, 'appliedKitta')
        applied_kitta.clear()
        applied_kitta.send_keys(applied_unit)

        self.driver.find_element(By.ID, 'crnNumber').send_keys(crn)

        self.driver.find_element(By.ID, 'disclaimer').click()

        self.driver.find_element(By.XPATH, '//*[@id="main"]/div/app-edit/div/div/wizard/div/wizard-step[1]/form/div[2]/div/div[4]/div[2]/div/button[1]/span').click()

    def enter_pin(self, transaction_password):
        sleep(1)
        self.driver.find_element(By.ID, 'transactionPIN').send_keys(transaction_password)
        self.driver.find_element(By.XPATH, '//*[@id="main"]/div/app-issue/div/wizard/div/wizard-step[2]/div[2]/div/form/div[2]/div/div/div/button[1]/span').click()

    def logout(self):
        sleep(1)
        self.driver.find_element(By.XPATH, '/html/body/app-dashboard/header/div[2]/div/div/div/ul/li[1]/a/i').click()

