
'''
项目名称:产品溯源系统
所属模块:防伪码管理/批量导入防伪码
日期:2020/11/10
作者:李锦龙
版本:version:1.0
'''
import os
import time
import pyautogui
from idna import unicode
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from public.common import loginTo
import sys
class SecurityImp():
	ms = loginTo.LoginTo()
	md = ms.driver

	def test_Imp(self):
		self.md.find_element_by_link_text("批量导入防伪码").click()
		time.sleep(1)
		xx = self.md.find_element_by_css_selector(".form-control")
		Select(xx).select_by_value("gbk")
		time.sleep(1)
		pyautogui.click(x=553, y=612, clicks=1, interval=0.0, button='left', duration=0.0, tween=pyautogui.linear)
		time.sleep(2)

		path = os.path.abspath(r"../data/testdata/code.txt")
		# path1 = unicode(path, 'utf8')
		# print(path1)
		pyautogui.write(path)
		time.sleep(2)
		# pyautogui.click(x=801, y=510, clicks=1, interval=0.0, button='left', duration=0.0, tween=pyautogui.linear)
		pyautogui.press('enter', presses=1)
		time.sleep(2)
		self.md.find_element_by_css_selector(".btn").click()
		time.sleep(2)


