
'''
项目名称:产品溯源系统
所属模块:流程记录管理/录入流程记录
日期:2020/11/06
作者:李锦龙
版本:version:1.0
'''
import time
from public.common import loginTo

from selenium.webdriver.support.select import Select

class AddRecord():
	ms = loginTo.LoginTo()
	md = ms.driver

	def test_01_add(self,wlh):
		# self.md.find_element_by_link_text("流程记录管理").click()
		time.sleep(1)
		self.md.find_element_by_link_text("录入流程记录").click()
		time.sleep(2)
		# self.md.execute_script("document.getElementById('s001').removeAttribute('style')")
		self.md.execute_script("document.getElementById('s001').style.display='block';")
		time.sleep(3)
		Select(self.md.find_element_by_id("s001")).select_by_visible_text("装箱/打包")
		time.sleep(2)
		self.md.find_element_by_css_selector("textarea.form-control").send_keys(wlh)
		self.md.find_element_by_css_selector("div.col-sm-6:nth-child(2) > input:nth-child(1)").send_keys("testmessage")
		self.md.find_element_by_css_selector("div.form-group:nth-child(5) > div:nth-child(2) > input:nth-child(1)").clear()
		self.md.find_element_by_css_selector("div.form-group:nth-child(5) > div:nth-child(2) > input:nth-child(1)").send_keys("wcg")
		time.sleep(1)
		self.md.find_element_by_css_selector(".btn").click()
		time.sleep(1)

