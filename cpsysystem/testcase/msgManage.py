
'''
项目名称:产品溯源系统
所属模块:流程记录管理/流程记录管理
日期:2020/11/06
作者:李锦龙
版本:version:1.0
'''
import time
from public.common import loginTo

from selenium.webdriver.support.select import Select


class MsgManage():
	ms = loginTo.LoginTo()
	md = ms.driver

	def test_02_searchMsg(self):
		# 搜索功能
		# time.sleep(1)
		# self.md.find_element_by_link_text("流程记录管理").click()
		time.sleep(3)
		self.md.find_element_by_css_selector(".sub-menu:nth-child(3) li:nth-child(4) > a").click()
		time.sleep(2)
		self.md.find_element_by_css_selector("input.form-control").send_keys("5")
		time.sleep(2)
		self.md.find_element_by_css_selector(".btn-success").click()
		time.sleep(2)
		# 断言

	def test_03_editMsg(self):
		#编辑记录
		self.md.find_element_by_css_selector(".btn-default").click()
		time.sleep(1)
		self.md.find_element_by_css_selector(".table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(9) > a:nth-child(1)").click()
		time.sleep(2)
		self.md.execute_script("document.getElementById('s001').style.display='block';")
		Select(self.md.find_element_by_id("s001")).select_by_visible_text("发货/出库")
		time.sleep(1)
		self.md.find_element_by_css_selector("div.col-sm-4:nth-child(2) > input:nth-child(1)").clear()
		self.md.find_element_by_css_selector("div.col-sm-4:nth-child(2) > input:nth-child(1)").send_keys("61695154")
		time.sleep(1)
		self.md.find_element_by_css_selector("div.form-group:nth-child(6) > div:nth-child(2) > input:nth-child(1)").clear()
		self.md.find_element_by_css_selector("div.form-group:nth-child(6) > div:nth-child(2) > input:nth-child(1)").send_keys("666")
		Select(self.md.find_element_by_name("zt")).select_by_value("no")
		time.sleep(1)
		self.md.find_element_by_css_selector(".btn").click()
		time.sleep(0.5)

	def test_04_delMsg(self):
		#刷新
		time.sleep(1)
		# self.md.find_element_by_css_selector(".btn-default").click()
		# time.sleep(1)
		#删除一条记录
		# tx = self.md.find_element_by_css_selector(".table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(3)").text
		self.md.find_element_by_css_selector(".table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(9) > span:nth-child(2)").click()
		time.sleep(2)
		self.md.find_element_by_css_selector(".layui-layer-btn0").click()
		time.sleep(2)
		self.md.find_element_by_css_selector(".btn-default").click()

		self.md.find_element_by_css_selector(".table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(1) > input:nth-child(1)").click()
		target_elem = self.md.find_element_by_css_selector("#del")
		self.md.execute_script("return arguments[0].scrollIntoView();", target_elem)
		target_elem.click()
		time.sleep(1)
		alert = self.md.switch_to.alert
		alert.accept()
		time.sleep(0.2)

