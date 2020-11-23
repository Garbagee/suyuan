
'''
项目名称:产品溯源系统
所属模块:防伪码管理/批量修改防伪码
日期:2020/11/10
作者:李锦龙
版本:version:1.0
'''
import time
import pyautogui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from public.common import loginTo

class Security_Edit():
	ms = loginTo.LoginTo()
	md = ms.driver

	def test_logistic(self):
		time.sleep(2)
		self.md.find_element_by_link_text("批量修改防伪码").click()
		time.sleep(1)
		self.md.find_element_by_id("txm").send_keys("53355")
		s1 = self.md.find_element_by_id("s000")
		self.md.execute_script("document.getElementById('s000').style.display='block';")
		Select(s1).select_by_visible_text("飞来峰")
		s2 = self.md.find_element_by_id("s001")
		self.md.execute_script("document.getElementById('s001').style.display='block';")
		Select(s2).select_by_visible_text("66")
		self.md.find_element_by_css_selector("div.row:nth-child(1) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(4) > div:nth-child(1) > button:nth-child(1)").click()
		time.sleep(1)

	def test_ID(self):
		time.sleep(2)
		self.md.find_element_by_css_selector("div.col-sm-2:nth-child(2) > input:nth-child(1)").send_keys("0000")
		self.md.find_element_by_css_selector("div.col-sm-2:nth-child(3) > input:nth-child(1)").send_keys("9999")
		s1 = self.md.find_element_by_id("s00")
		self.md.execute_script("document.getElementById('s00').style.display='block';")
		Select(s1).select_by_visible_text("飞来峰")
		s2 = self.md.find_element_by_id("s01")
		self.md.execute_script("document.getElementById('s01').style.display='block';")
		Select(s2).select_by_visible_text("66")
		self.md.find_element_by_css_selector("div.row:nth-child(2) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(4) > div:nth-child(1) > button:nth-child(1)").click()
		time.sleep(1)

	def test_Pc(self):
		time.sleep(2)
		ll = self.md.find_element_by_css_selector("div.row:nth-child(3) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(4) > div:nth-child(1) > button:nth-child(1)")
		self.md.execute_script("return arguments[0].scrollIntoView();",ll)
		time.sleep(1)
		s1 = self.md.find_element_by_id("s1")
		self.md.execute_script("document.getElementById('s1').style.display='block';")
		Select(s1).select_by_visible_text("202011201752087")
		time.sleep(1)
		s2 = self.md.find_element_by_id("s2")
		self.md.execute_script("document.getElementById('s2').style.display='block';")
		Select(s2).select_by_visible_text("飞来峰")
		time.sleep(1)
		s3 = self.md.find_element_by_id("s3")
		self.md.execute_script("document.getElementById('s3').style.display='block';")
		Select(s3).select_by_visible_text("66")
		self.md.find_element_by_css_selector("div.row:nth-child(3) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(4) > div:nth-child(1) > button:nth-child(1)").click()
		time.sleep(1)

	def test_product(self):
		time.sleep(2)
		ll = self.md.find_element_by_css_selector("div.row:nth-child(4) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(3) > div:nth-child(1) > button:nth-child(1)")
		self.md.execute_script("return arguments[0].scrollIntoView();",ll)
		time.sleep(1)
		s1 = self.md.find_element_by_id("cp")
		self.md.execute_script("document.getElementById('cp').style.display='block';")
		Select(s1).select_by_visible_text("飞来峰")
		time.sleep(1)
		s2 = self.md.find_element_by_id("s4")
		self.md.execute_script("document.getElementById('s4').style.display='block';")
		Select(s2).select_by_visible_text("66")
		time.sleep(1)
		self.md.find_element_by_css_selector("div.row:nth-child(4) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(3) > div:nth-child(1) > button:nth-child(1)").click()
		time.sleep(1)

	def test_date(self):
		time.sleep(2)
		ll = self.md.find_element_by_css_selector(
			"div.row:nth-child(5) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(4) > div:nth-child(1) > button:nth-child(1)")
		self.md.execute_script("return arguments[0].scrollIntoView();", ll)
		s1 = self.md.find_element_by_id("s5")
		self.md.execute_script("document.getElementById('s5').style.display='block';")
		Select(s1).select_by_visible_text("2020-11-22")
		time.sleep(1)
		s2 = self.md.find_element_by_id("s6")
		self.md.execute_script("document.getElementById('s6').style.display='block';")
		Select(s2).select_by_visible_text("飞来峰")
		time.sleep(1)
		s3 = self.md.find_element_by_id("s7")
		self.md.execute_script("document.getElementById('s7').style.display='block';")
		Select(s3).select_by_visible_text("66")
		time.sleep(1)
		self.md.find_element_by_css_selector("div.row:nth-child(5) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(4) > div:nth-child(1) > button:nth-child(1)").click()
		time.sleep(1)



