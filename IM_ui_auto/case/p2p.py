# coding = utf-8

from IM_ui_auto.config import config
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class p2p():

    def __init__(self):
        self.option = webdriver.ChromeOptions()
        self.prefs = {
            'profile.default_content_setting_values.media_stream_camera': 1,  # 摄像头权限
            'profile.default_content_setting_values.media_stream_mic': 1,  # 麦克风权限
            'profile.default_content_setting_values.notifications': 1,  # 通知权限
            'profile.default_content_setting_values.geolocation': 1  # 定位权限
        }
        self.option.add_experimental_option('prefs', self.prefs)
        self.driver = webdriver.Chrome(options=self.option)
        self.path = config.path

    def sendMsg(self):
        self.driver.get(self.path)
        self.driver.maximize_window()
        sleep(1)
        self.driver.find_element(By.XPATH, config.demoEnter_xpath).click()
        sleep(1)
        self.driver.find_element(By.XPATH, config.username_xpath).send_keys(config.username1)
        self.driver.find_element(By.XPATH, config.password_xpath).send_keys(config.password)
        self.driver.find_element(By.XPATH, config.accountEnter_xpath).click()
        sleep(3)
        self.driver.find_element(By.XPATH, config.iconFriend_xpath).click()
        sleep(1)
        self.driver.find_element(By.XPATH, config.zzz3_xpath).click()
        sleep(1)

        self.driver.find_element(By.XPATH, config.input_xpath).send_keys('zzz')
        self.driver.find_element(By.XPATH, config.send_xpath).click()

        sleep(1)
        self.driver.find_element(By.XPATH, config.emoji_xpath).click()
        sleep(1)
        self.driver.find_element(By.XPATH, config.emoji_laugh_xpath).click()
        self.driver.find_element(By.XPATH, config.send_xpath).click()
        sleep(1)

        self.driver.find_element(By.XPATH, config.voice_xpath).click()
        sleep(5)

        self.driver.find_element(By.XPATH, config.send_xpath).click()

        sleep(1)

        self.driver.find_element(By.XPATH, config.audio_call_xpath).click()
        sleep(1)
        self.driver.find_element(By.XPATH, config.audio_call_cfm_xpath).click()
        sleep(3)
        self.driver.find_element(By.XPATH, config.netcall_button_red_xpath).click()
        sleep(1)
        self.driver.find_element(By.XPATH, config.video_xpath).click()
        sleep(1)
        self.driver.find_element(By.XPATH, config.audio_call_cfm_xpath).click()
        sleep(3)
        self.driver.find_element(By.XPATH, config.netcall_button_red_xpath).click()
        sleep(1)
        self.driver.find_element(By.XPATH, config.wtboard_xpath).click()
        sleep(1)
        self.driver.find_element(By.XPATH, config.pcAgent_xpath).click()
        self.driver.find_element(By.XPATH, config.audio_call_cfm_xpath).click()
        sleep(3)
        self.driver.find_element(By.XPATH, config.wtboard_red_button_xpath).click()
        sleep(2)

        return print('send successed')


if __name__ == '__main__':
    p2p().sendMsg()
