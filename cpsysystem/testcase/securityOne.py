
'''
项目名称:产品溯源系统
所属模块:防伪码管理/单个生成防伪码
日期:2020/11/10
作者:李锦龙
版本:version:1.0
'''
import time
import pyautogui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from public.common import loginTo

class SecurityOne():
	ms = loginTo.LoginTo()
	md = ms.driver

	def test_One(self):
		self.md.find_element_by_link_text("单个生成防伪码").click()
		time.sleep(1)
		self.md.find_element_by_css_selector(".col-sm-3 > input:nth-child(1)").clear()
		self.md.find_element_by_css_selector(".col-sm-3 > input:nth-child(1)").send_keys("11111111111")
		self.md.find_element_by_css_selector("div.form-group:nth-child(2) > div:nth-child(2) > input:nth-child(1)").clear()
		self.md.find_element_by_css_selector("div.form-group:nth-child(2) > div:nth-child(2) > input:nth-child(1)").send_keys("QWEQWEQWE")
		self.md.find_element_by_css_selector("div.form-group:nth-child(3) > div:nth-child(2) > input:nth-child(1)").clear()
		self.md.find_element_by_css_selector("div.form-group:nth-child(3) > div:nth-child(2) > input:nth-child(1)").send_keys("8888888888")
		time.sleep(1)
		s1 = self.md.find_element_by_id("s1")
		self.md.execute_script("document.getElementById('s1').style.display='block';")
		Select(s1).select_by_visible_text("飞来峰")
		time.sleep(1)
		s2 = self.md.find_element_by_id("s2")
		self.md.execute_script("document.getElementById('s2').style.display='block';")
		Select(s2).select_by_visible_text("katherine")
		time.sleep(1)
		Select(self.md.find_element_by_id("qiyong")).select_by_value("no")
		time.sleep(1)
		self.md.find_element_by_css_selector(".btn").click()
		time.sleep(1)






