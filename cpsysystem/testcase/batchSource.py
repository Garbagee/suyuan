
'''
项目名称:产品溯源系统
所属模块:溯源实例管理/批量溯源操作
日期:2020/11/06
作者:李锦龙
版本:version:1.0
'''
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from public.common import loginTo

class BatchSource():
	ms = loginTo.LoginTo()
	md = ms.driver

	def batch_Logistic(self):
		time.sleep(2)
		self.md.find_element_by_link_text("批量溯源操作").click()
		self.md.find_element_by_id("txm").send_keys("53355")
		self.md.find_element_by_id("txm").send_keys(Keys.ENTER)
		self.md.find_element_by_id("txm").send_keys("45453")
		self.md.execute_script("document.getElementById('s001').style.display='block';")
		Select(self.md.find_element_by_id("s001")).select_by_visible_text("产品质量不合格")
		time.sleep(1)
		self.md.find_element_by_css_selector("div.row:nth-child(1) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(5) > div:nth-child(1) > button:nth-child(1)").click()
		time.sleep(1)

	def batch_Id(self):
		self.md.find_element_by_css_selector("div.col-sm-2:nth-child(2) > input:nth-child(1)").send_keys("0000")
		time.sleep(1)
		self.md.find_element_by_css_selector("div.col-sm-2:nth-child(3) > input:nth-child(1)").send_keys("9999")
		time.sleep(2)
		self.md.execute_script("document.getElementById('s00').style.display='block';")
		Select(self.md.find_element_by_id("s00")).select_by_visible_text("产品质量不合格")
		time.sleep(1)
		self.md.find_element_by_xpath("/html/body/section/section/section/div[2]/div/section/div/form/div[3]/div/button").click()
		time.sleep(1)

	def batch_Pc(self):
		tar_element = self.md.find_element_by_css_selector("div.row:nth-child(3) > div:nth-child(1) > section:nth-child(1) > header:nth-child(1) > h3:nth-child(1)")
		self.md.execute_script("return arguments[0].scrollIntoView();", tar_element)
		time.sleep(1)
		self.md.execute_script("document.getElementById('s1').style.display='block';")
		Select(self.md.find_element_by_id("s1")).select_by_visible_text("202010121")
		time.sleep(1)
		self.md.execute_script("document.getElementById('s01').style.display='block';")
		Select(self.md.find_element_by_id("s01")).select_by_visible_text("ASD")
		time.sleep(1)
		self.md.find_element_by_css_selector("div.row:nth-child(3) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(5) > div:nth-child(1) > button:nth-child(1)").click()
		time.sleep(1)

	def batch_name(self):
		tar_element = self.md.find_element_by_css_selector(
			"div.row:nth-child(4) > div:nth-child(1) > section:nth-child(1) > header:nth-child(1) > h3:nth-child(1)")
		self.md.execute_script("return arguments[0].scrollIntoView();", tar_element)
		time.sleep(1)
		self.md.execute_script("document.getElementById('cp').style.display='block';")
		Select(self.md.find_element_by_id("cp")).select_by_visible_text("ASD")
		time.sleep(1)
		self.md.execute_script("document.getElementById('s03').style.display='block';")
		Select(self.md.find_element_by_id("s03")).select_by_visible_text("1")
		time.sleep(1)
		self.md.find_element_by_css_selector(
			"div.row:nth-child(4) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(5) > div:nth-child(1) > button:nth-child(1)").click()
		time.sleep(1)

	def batch_date(self):
		tar_element = self.md.find_element_by_css_selector(
			"div.row:nth-child(5) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(5) > div:nth-child(1) > button:nth-child(1)")
		self.md.execute_script("return arguments[0].scrollIntoView();", tar_element)
		time.sleep(1)
		self.md.execute_script("document.getElementById('s5').style.display='block';")
		Select(self.md.find_element_by_id("s5")).select_by_visible_text("2020-10-23")
		time.sleep(1)

		self.md.execute_script("document.getElementById('s04').style.display='block';")
		Select(self.md.find_element_by_id("s04")).select_by_visible_text("品质")
		self.md.find_element_by_id("s04").send_keys(Keys.END)
		time.sleep(1)
		self.md.find_element_by_css_selector(
			"div.row:nth-child(5) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(5) > div:nth-child(1) > button:nth-child(1)").click()
		time.sleep(1)
