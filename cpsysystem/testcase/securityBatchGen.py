
'''
项目名称:产品溯源系统
所属模块:防伪码管理/批量生成防伪码
日期:2020/11/10
作者:李锦龙
版本:version:1.0
'''
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from public.common import loginTo

class SecurityBatchGen():
	ms = loginTo.LoginTo()
	md = ms.driver
	#溯源实例管理
	def test_01_add(self):
		self.md.find_element_by_link_text("防伪码管理").click()
		time.sleep(1)
		self.md.find_element_by_link_text("批量生成防伪码").click()
		time.sleep(1)
		self.md.find_element_by_css_selector("div.form-group:nth-child(2) > div:nth-child(2) > input:nth-child(1)").clear()
		self.md.find_element_by_css_selector("div.form-group:nth-child(2) > div:nth-child(2) > input:nth-child(1)").send_keys("8")
		self.md.find_element_by_css_selector("div.form-group:nth-child(3) > div:nth-child(2) > input:nth-child(1)").send_keys("WG")
		ct = self.md.find_element_by_id("code_type")
		Select(ct).select_by_visible_text("前缀+数字")
		time.sleep(1)
		tt = self.md.find_element_by_id("txm_type")
		Select(tt).select_by_visible_text("纯数字")
		time.sleep(1)
		self.md.find_element_by_css_selector("div.col-sm-2:nth-child(4) > input:nth-child(1)").send_keys("10")
		self.md.find_element_by_css_selector("div.form-group:nth-child(6) > div:nth-child(2) > input:nth-child(1)").send_keys("10")
		dd = self.md.find_element_by_id("s1")
		self.md.execute_script("document.getElementById('s1').style.display='block';")
		Select(dd).select_by_visible_text("ASD")
		time.sleep(1)
		d1 = self.md.find_element_by_id("s2")
		self.md.execute_script("document.getElementById('s2').style.display='block';")
		Select(d1).select_by_visible_text("66")
		d2 = self.md.find_element_by_id("qiyong")
		Select(d2).select_by_value("no")
		time.sleep(1)
		self.md.find_element_by_id("tj").click()
		time.sleep(2)



