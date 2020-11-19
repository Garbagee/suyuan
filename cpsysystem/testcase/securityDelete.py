
'''
项目名称:产品溯源系统
所属模块:防伪码管理/批量删除防伪码
日期:2020/11/10
作者:李锦龙
版本:version:1.0
'''
import time
import pyautogui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from public.common import loginTo

class Security_Del():
	ms = loginTo.LoginTo()
	md = ms.driver

	def test_del_Pc(self):
		time.sleep(2)
		self.md.find_element_by_link_text("批量删除防伪码").click()
		time.sleep(1)
		s1 = self.md.find_element_by_id("s1")
		self.md.execute_script("document.getElementById('s1').style.display='block';")
		Select(s1).select_by_visible_text("202011101006575")
		self.md.find_element_by_css_selector("div.row:nth-child(1) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)").click()
		time.sleep(1)

	def test_del_Product(self):
		time.sleep(2)
		s1 = self.md.find_element_by_id("cp")
		self.md.execute_script("document.getElementById('cp').style.display='block';")
		Select(s1).select_by_visible_text("ASD")
		self.md.find_element_by_css_selector(
			"div.row:nth-child(2) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)").click()
		time.sleep(1)

	def test_del_Date(self):
		time.sleep(2)
		s1 = self.md.find_element_by_id("s5")
		self.md.execute_script("document.getElementById('s5').style.display='block';")
		Select(s1).select_by_visible_text("2020-10-23")
		self.md.find_element_by_css_selector(
			"div.row:nth-child(3) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)").click()
		time.sleep(1)

	def test_del_Num(self):
		time.sleep(2)
		self.md.find_element_by_css_selector(".form-control").clear()
		self.md.find_element_by_css_selector(".form-control").send_keys("10000")
		self.md.find_element_by_css_selector(
			"div.row:nth-child(4) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)").click()
		time.sleep(1)

	def test_del_All(self):
		time.sleep(2)
		ll = self.md.find_element_by_css_selector(
			"div.form-group:nth-child(3) > div:nth-child(1) > button:nth-child(1)")
		self.md.execute_script("return arguments[0].scrollIntoView();", ll)
		self.md.find_element_by_css_selector(
			"div.form-group:nth-child(3) > div:nth-child(1) > button:nth-child(1)").click()
		time.sleep(1)



