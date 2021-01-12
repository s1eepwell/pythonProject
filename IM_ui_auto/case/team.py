# coding=utf-8

from IM_ui_auto.config import config
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains as AC


class team():
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

    def createTeam(self):
        self.driver.get(self.path)
        self.driver.maximize_window()
        sleep(1)
        self.driver.find_element(By.XPATH, config.demoEnter_xpath).click()
        sleep(1)
        self.driver.find_element(By.XPATH, config.username_xpath).send_keys(config.username1)
        self.driver.find_element(By.XPATH, config.password_xpath).send_keys(config.password)
        self.driver.find_element(By.XPATH, config.accountEnter_xpath).click()
        sleep(3)
        self.driver.find_element(By.XPATH, config.iconteam_xpath).click()
        sleep(2)
        self.driver.find_element(By.XPATH, config.createTeam_xpath).click()
        sleep(3)
        self.driver.find_element(By.XPATH, config.friendzhenzhe2radio_xpath).click()
        self.driver.find_element(By.XPATH, config.friendzhenzhe3radio_xpath).click()
        sleep(1)
        self.driver.find_element(By.XPATH, config.teamboxConfirm_xpath).click()
        sleep(1)
        self.driver.find_element(By.XPATH, config.teamInfo_xpath).click()
        sleep(1)

        return print('create successed')

    def quitTeam(self):
        self.driver.get(self.path)
        self.driver.maximize_window()
        sleep(1)
        self.driver.find_element(By.XPATH, config.demoEnter_xpath).click()
        sleep(1)
        self.driver.find_element(By.XPATH, config.username_xpath).send_keys(config.username3)
        self.driver.find_element(By.XPATH, config.password_xpath).send_keys(config.password)
        self.driver.find_element(By.XPATH, config.accountEnter_xpath).click()
        sleep(3)
        self.driver.find_element(By.XPATH, config.notificationCenter_xpath).click()
        sleep(2)
        self.driver.find_element(By.XPATH, config.agreeEnterTeam_xpath).click()
        sleep(2)
        self.driver.find_element(By.XPATH, config.closentfctCenter_xpath).click()
        sleep(2)

        self.driver.find_element(By.XPATH, config.newTeam_xpath).click()
        sleep(1)

        self.driver.find_element(By.XPATH, config.teamInfo_xpath).click()
        sleep(3)

        self.driver.find_element(By.XPATH, config.quitTeam_xpath).click()
        sleep(2)
        return print('quit successed')

    def dismissTeam(self):
        self.driver.get(self.path)
        self.driver.maximize_window()
        sleep(1)
        self.driver.find_element(By.XPATH, config.demoEnter_xpath).click()
        sleep(1)
        self.driver.find_element(By.XPATH, config.username_xpath).send_keys(config.username1)
        self.driver.find_element(By.XPATH, config.password_xpath).send_keys(config.password)
        self.driver.find_element(By.XPATH, config.accountEnter_xpath).click()
        sleep(3)
        self.driver.find_element(By.XPATH, config.iconteam_xpath).click()
        self.driver.find_element(By.XPATH, config.createTeam_xpath).click()
        sleep(2)
        self.driver.find_element(By.XPATH, config.friendzhenzhe2radio_xpath).click()
        self.driver.find_element(By.XPATH, config.friendzhenzhe3radio_xpath).click()
        self.driver.find_element(By.XPATH, config.teamboxConfirm_xpath).click()
        sleep(1)
        self.driver.find_element(By.XPATH, config.teamInfo_xpath).click()
        sleep(1)
        self.driver.find_element(By.XPATH, config.dismissTeam_xpath).click()

        sleep(3)

        return print('dismiss successed')

    def teamSendMsg(self):
        self.driver.get(self.path)
        self.driver.maximize_window()
        sleep(1)
        self.driver.find_element(By.XPATH, config.demoEnter_xpath).click()
        sleep(1)
        self.driver.find_element(By.XPATH, config.username_xpath).send_keys(config.username1)
        self.driver.find_element(By.XPATH, config.password_xpath).send_keys(config.password)
        self.driver.find_element(By.XPATH, config.accountEnter_xpath).click()
        sleep(1)
        self.driver.find_element(By.XPATH, config.iconteam_xpath).click()
        sleep(2)
        self.driver.find_element(By.XPATH, config.createTeam_xpath).click()
        sleep(3)
        self.driver.find_element(By.XPATH, config.friendzhenzhe2radio_xpath).click()
        self.driver.find_element(By.XPATH, config.friendzhenzhe3radio_xpath).click()
        sleep(1)
        self.driver.find_element(By.XPATH, config.teamboxConfirm_xpath).click()
        sleep(1)

        self.driver.find_element(By.XPATH, config.input_xpath).send_keys('zzz')
        self.driver.find_element(By.XPATH, config.send_xpath).click()

        sleep(1)
        self.driver.find_element(By.XPATH, config.emoji_xpath).click()
        sleep(1)
        self.driver.find_element(By.XPATH, config.emoji_laugh_xpath).click()
        self.driver.find_element(By.XPATH, config.send_xpath).click()
        sleep(1)
        #
        self.driver.find_element(By.XPATH, config.voice_xpath).click()
        sleep(5)

        self.driver.find_element(By.XPATH, config.send_xpath).click()

        sleep(1)

        return print('send successed')

    def editTeam(self):
        self.driver.get(self.path)
        self.driver.maximize_window()
        sleep(1)
        self.driver.find_element(By.XPATH, config.demoEnter_xpath).click()
        sleep(1)
        self.driver.find_element(By.XPATH, config.username_xpath).send_keys(config.username1)
        self.driver.find_element(By.XPATH, config.password_xpath).send_keys(config.password)
        self.driver.find_element(By.XPATH, config.accountEnter_xpath).click()
        sleep(3)
        self.driver.find_element(By.XPATH, config.iconteam_xpath).click()
        self.driver.find_element(By.XPATH, config.createTeam_xpath).click()
        sleep(1)
        self.driver.find_element(By.XPATH, config.friendzhenzhe2radio_xpath).click()
        self.driver.find_element(By.XPATH, config.friendzhenzhe3radio_xpath).click()
        self.driver.find_element(By.XPATH, config.teamboxConfirm_xpath).click()
        sleep(1)
        self.driver.find_element(By.XPATH, config.teamInfo_xpath).click()
        sleep(1)

        self.driver.find_element(By.XPATH, config.teamName_xpath).click()
        sleep(1)
        self.driver.find_element(By.XPATH, config.teamName_edit_xpath).send_keys('zzz')
        sleep(2)
        self.driver.find_element(By.XPATH, config.teamIntro_xpath).click()
        sleep(1)
        self.driver.find_element(By.XPATH, config.teamIntro_edit_xpath).send_keys('good team')
        sleep(1)
        self.driver.find_element(By.XPATH, config.noVerify_xpath).click()
        sleep(1)
        self.driver.find_element(By.XPATH, config.needVerify_xpath).click()
        sleep(1)
        self.driver.find_element(By.XPATH, config.rejectAll_xpath).click()
        sleep(1)
        self.driver.find_element(By.XPATH, config.ivtOthers_manager_xpath).click()
        sleep(1)
        self.driver.find_element(By.XPATH, config.ivtOthers_all_xpath).click()
        sleep(1)
        self.driver.find_element(By.XPATH, config.updtIndo_manager_xpath).click()
        sleep(1)
        self.driver.find_element(By.XPATH, config.updtInfo_all_xpath).click()
        sleep(1)
        self.driver.find_element(By.XPATH, config.beInvite_needVerify_xpath).click()
        sleep(1)
        self.driver.find_element(By.XPATH, config.beInvite_noVerify_xpath).click()
        sleep(2)
        return print('edit successed')

    def recall(self):
        self.driver.get(self.path)
        self.driver.maximize_window()
        sleep(1)
        self.driver.find_element(By.XPATH, config.demoEnter_xpath).click()
        sleep(1)
        self.driver.find_element(By.XPATH, config.username_xpath).send_keys(config.username1)
        self.driver.find_element(By.XPATH, config.password_xpath).send_keys(config.password)
        self.driver.find_element(By.XPATH, config.accountEnter_xpath).click()
        sleep(1)
        self.driver.find_element(By.XPATH, config.iconteam_xpath).click()
        sleep(2)
        self.driver.find_element(By.XPATH, config.createTeam_xpath).click()
        sleep(3)
        self.driver.find_element(By.XPATH, config.friendzhenzhe2radio_xpath).click()
        self.driver.find_element(By.XPATH, config.friendzhenzhe3radio_xpath).click()
        sleep(1)
        self.driver.find_element(By.XPATH, config.teamboxConfirm_xpath).click()
        sleep(1)

        self.driver.find_element(By.XPATH, config.input_xpath).send_keys('zzz')
        self.driver.find_element(By.XPATH, config.send_xpath).click()
        sleep(3)
        AC(self.driver) \
            .context_click(self.driver.find_element(By.XPATH, config.lstmsg_xpath)) \
            .click(self.driver.find_element(By.XPATH, config.recall_xpath)) \
            .perform()
        sleep(1)

        return print('recall successed')


if __name__ == '__main__':
    team().createTeam()
    #
    team().quitTeam()
    team().dismissTeam()
    team().teamSendMsg()
    team().editTeam()
    team().recall()
