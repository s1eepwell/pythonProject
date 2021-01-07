# coding=utf-8

from IM_ui_auto.config import config
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class account():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.path = config.path
        self.username = config.username1
        self.password = config.password

    def signin(self):
        self.driver.get(self.path)
        self.driver.maximize_window()
        sleep(1)
        self.driver.find_element(By.XPATH, config.demoEnter_xpath).click()
        sleep(1)
        self.driver.find_element(By.XPATH, config.username_xpath).send_keys(config.username1)
        self.driver.find_element(By.XPATH, config.password_xpath).send_keys(config.password)
        self.driver.find_element(By.XPATH, config.accountEnter_xpath).click()
        sleep(2)
        self.driver.find_element(By.XPATH, config.quit_xpath).click()

        return print('quit succ')

    def register(self):
        self.driver.get(self.path)
        self.driver.maximize_window()
        sleep(1)
        self.driver.find_element(By.XPATH, config.demoEnter_xpath).click()
        sleep(1)
        self.driver.find_element(By.XPATH, config.rgsApply_xpath).click()
        sleep(1)
        self.driver.find_element(By.XPATH, config.userName_xpath).send_keys(config.userName)
        self.driver.find_element(By.XPATH, config.nick_xpath).send_keys(config.nick)
        self.driver.find_element(By.XPATH, config.passWord_xpath).send_keys(config.password)
        self.driver.find_element(By.XPATH, config.rgsbutton_xpath).click()
        sleep(5)


if __name__ == '__main__':
    account().register()
    account().signin()
