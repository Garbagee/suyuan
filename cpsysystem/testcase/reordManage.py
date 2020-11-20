'''
项目名称:产品溯源系统
所属模块:流程记录管理
日期:2020/11/05
作者:李锦龙
版本:version:1.0
'''
'''
项目名称:产品溯源系统
所属模块:流程记录管理/流程类别管理
日期:2020/11/06
作者:李锦龙
版本:version:1.0
'''
import time
from public.common import loginTo

from selenium.webdriver.support.select import Select


class RecordManage():
	ms = loginTo.LoginTo()
	md = ms.driver
	# def __init__(self):
	# 	lt = loginTo.LoginTo().login()

	def test_02_searchRecord(self):
		#搜索功能
		# time.sleep(1)
		# self.md.find_element_by_link_text("流程记录管理").click()
		time.sleep(3)
		self.md.find_element_by_link_text("流程类别管理").click()
		time.sleep(2)
		self.md.find_element_by_css_selector(".form-control").send_keys("取消")
		time.sleep(2)
		self.md.find_element_by_css_selector(".btn-success").click()
		time.sleep(2)
		#断言
		# a = self.md.find_element_by_css_selector(".table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(3)").text
		#
		# self.unittest.assertIn("取消",a,msg="搜索失败")

	def test_03_editRecord(self):
		#编辑记录
		self.md.find_element_by_css_selector(".btn-default").click()
		time.sleep(1)
		self.md.find_element_by_css_selector(".table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(7) > a:nth-child(1)").click()
		time.sleep(2)
		self.md.find_element_by_css_selector(".col-sm-3 > input:nth-child(1)").clear()
		self.md.find_element_by_css_selector(".col-sm-3 > input:nth-child(1)").send_keys("testmessage")
		time.sleep(1)
		self.md.find_element_by_css_selector("div.form-group:nth-child(3) > div:nth-child(2) > input:nth-child(1)").clear()
		self.md.find_element_by_css_selector("div.form-group:nth-child(3) > div:nth-child(2) > input:nth-child(1)").send_keys("121")
		Select(self.md.find_element_by_name("zt")).select_by_value("no")
		time.sleep(1)
		self.md.find_element_by_css_selector(".btn").click()
		time.sleep(0.5)

	def test_04_delRecord(self):
		#刷新
		time.sleep(2)
		self.md.find_element_by_css_selector(".btn-default").click()
		time.sleep(1)
		#删除一条记录
		# tx = self.md.find_element_by_css_selector(".table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(3)").text
		self.md.find_element_by_css_selector(".table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(7) > span:nth-child(2)").click()
		time.sleep(2)
		self.md.find_element_by_css_selector(".layui-layer-btn0").click()
		time.sleep(1)
		# self.md.find_element_by_css_selector(".btn-default").click()
		# tx1 = self.md.find_element_by_css_selector(".table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(3)").text
		# self.assertNotEqual(tx,tx1,msg="删除失败")
		#批量删除
		self.md.find_element_by_css_selector(".table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(1) > input:nth-child(1)").click()
		self.md.find_element_by_css_selector(".table > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(1) > input:nth-child(1)").click()
		target_elem = self.md.find_element_by_css_selector("#del")
		self.md.execute_script("return arguments[0].scrollIntoView();", target_elem)
		target_elem.click()
		time.sleep(1)
		alert = self.md.switch_to.alert
		alert.accept()
		time.sleep(1)
		a = self.md.switch_to.alert.text
		print(a)
		self.md.switch_to.alert.accept()
		return a