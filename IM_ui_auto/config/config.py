# coding=utf-8

import time

path = "https://app.yunxin.163.com/webdemo/im/index.html"

# 登录账号
username1 = "zhenzhe1"

username2 = 'zhenzhe2'

username3 = 'zhenzhe3'

password = "123456"

username_xpath = '/html/body/div[2]/form/div[1]/input'

password_xpath = '/html/body/div[2]/form/div[2]/input'

# IM即时通讯按钮
demoEnter_xpath = '/html/body/div[2]/div[1]/a/button'

# 登录按钮
accountEnter_xpath = '/html/body/div[2]/form/div[4]/button'

# 注册账号

userName = str(time.time())

userName_xpath = '/html/body/div[1]/form/div[1]/input'

nick_xpath = '//*[@id="nickname"]'

nick = '201sjoa'

passWord_xpath = '/html/body/div[1]/form/div[3]/input'

# 申请注册按钮

rgsApply_xpath = '/html/body/div[2]/div/a'

# 注册账号提交按钮

rgsbutton_xpath = '/html/body/div[1]/form/div[5]/button'

# 注销

quit_xpath = '/html/body/div[2]/div[1]/div[1]/div[2]/span[3]'

# 获取好友列表

iconFriend_xpath = '/html/body/div[2]/div[1]/div[1]/div[4]/a[2]/span'

zhenzhe2_xpath = '/html/body/div[2]/div[1]/div[1]/div[6]/div/div[2]/ul/li[3]'

# 末位好友

zzz3_xpath = '/html/body/div[2]/div[1]/div[1]/div[6]/div/div[2]/ul/li[12]'

# 获取群列表
iconteam_xpath = '/html/body/div[2]/div[1]/div[1]/div[4]/a[3]/span'

# 创建高级群

createTeam_xpath = '//*[@id="createAdvanceTeam"]/div[2]/p'
# 勾选好友radio框
friendzhenzhe3radio_xpath = '/html/body/div[2]/div[6]/div/div[2]/div[2]/ul/li[12]/i'

friendzhenzhe2radio_xpath = '/html/body/div[2]/div[6]/div/div[2]/div[2]/ul/li[11]/i'

friendradio_selector = '#addUserList > ul > li:nth-child(1)'
# 输入框

input_xpath = '/html/body/div[2]/div[1]/div[3]/div/div[7]/textarea'

# 发送按钮

send_xpath = '/html/body/div[2]/div[1]/div[3]/div/div[7]/a[5]'
# teambox定位

# teambox“确定按钮”

teamboxConfirm_xpath = '/html/body/div[2]/div[6]/div/div[3]/button[2]'

# team资料框

teamInfo_xpath = '/html/body/div[2]/div[1]/div[3]/div/div[1]/div[2]'

addFriend_xpath = '/html/body/div[2]/div[3]/div/div[2]/ul/li[1]'

teamName_xpath = '/html/body/div[2]/div[3]/div/div[3]/div[2]/div[2]/span'

teamName_edit_xpath = '/html/body/div[2]/div[3]/div/div[3]/div[2]/div[2]/span/input'

teamIntro_xpath = '/html/body/div[2]/div[3]/div/div[3]/div[3]/div[2]/span'

teamIntro_edit_xpath = '/html/body/div[2]/div[3]/div/div[3]/div[3]/div[2]/span/input'

noVerify_xpath = '/html/body/div[2]/div[3]/div/div[3]/div[4]/div[2]/input[1]'

needVerify_xpath = '/html/body/div[2]/div[3]/div/div[3]/div[4]/div[2]/input[2]'

rejectAll_xpath = '/html/body/div[2]/div[3]/div/div[3]/div[4]/div[2]/input[3]'

ivtOthers_manager_xpath = '/html/body/div[2]/div[3]/div/div[3]/div[5]/div[2]/input[1]'

ivtOthers_all_xpath = '/html/body/div[2]/div[3]/div/div[3]/div[5]/div[2]/input[2]'

updtIndo_manager_xpath = '/html/body/div[2]/div[3]/div/div[3]/div[6]/div[2]/input[1]'

updtInfo_all_xpath = '/html/body/div[2]/div[3]/div/div[3]/div[6]/div[2]/input[2]'

beInvite_needVerify_xpath = '/html/body/div[2]/div[3]/div/div[3]/div[7]/div[2]/input[1]'

beInvite_noVerify_xpath = '/html/body/div[2]/div[3]/div/div[3]/div[7]/div[2]/input[2]'

# 解散群

dismissTeam_xpath = '/html/body/div[2]/div[3]/div/div[3]/div[8]/a[2]'

# 退出群

quitTeam_xpath = '/html/body/div[2]/div[3]/div/div[3]/div[8]/a[1]'

# 消息中心

notificationCenter_xpath = '/html/body/div[2]/div[1]/div[1]/div[5]/div/div[1]/div/div[2]/p'

# 同意入群

agreeEnterTeam_xpath = '/html/body/div[2]/div[9]/div[2]/div[1]/div/p[2]/b/a[1]'

# 关闭消息中心

closentfctCenter_xpath = '/html/body/div[2]/div[9]/div[1]/i'

# 获取新群

newTeam_xpath = '/html/body/div[2]/div[1]/div[1]/div[5]/div/div[2]/ul/li[1]'

# 最近一条会话

lastSession_xpath = '/html/body/div[2]/div[1]/div[1]/div[5]/div/div[2]/ul/li[1]'

emoji_xpath = '/html/body/div[2]/div[1]/div[3]/div/div[7]/a[1]'

emoji_laugh_xpath = '/html/body/div[2]/div[1]/div[3]/div/div[7]/div[1]/div/div[1]/ul/span[1]/img'

voice_xpath = '/html/body/div[2]/div[1]/div[3]/div/div[7]/div[2]/a'

video_xpath = '/html/body/div[2]/div[1]/div[3]/div/div[7]/a[3]'

wtboard_xpath = '/html/body/div[2]/div[1]/div[3]/div/div[7]/a[4]'

audio_call_xpath = '/html/body/div[2]/div[1]/div[3]/div/div[7]/a[2]'

audio_call_cfm_xpath = '/html/body/div[2]/div[7]/div/div[3]/button'

# 选择PcAgent

pcAgent_xpath = '/html/body/div[2]/div[7]/div/div[2]/div[2]/p'

# 挂断语音呼叫

netcall_button_red_xpath = '/html/body/div[2]/div[1]/div[3]/div/div[2]/div[3]/div[3]/button'

# 挂断白板

wtboard_red_button_xpath = '/html/body/div[2]/div[1]/div[3]/div/div[3]/div[1]/div[3]/button'
# 撤回

recall_xpath = '/html/body/ul/li'

lstmsg_xpath = '/html/body/div[2]/div[1]/div[3]/div/div[4]/div/div/div/div/div'
