
'''
项目名称:产品溯源系统
所属模块:溯源实例管理/溯源实例管理
日期:2020/11/06
作者:李锦龙
版本:version:1.0
'''
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from public.common import loginTo

class SourceManage():
	ms = loginTo.LoginTo()
	md = ms.driver

	def test_02_search(self):
		# 搜索功能
		# time.sleep(1)
		# self.md.find_element_by_link_text("溯源实例管理").click()
		time.sleep(1)
		self.md.find_element_by_css_selector("li.sub-menu:nth-child(4) > ul:nth-child(2) > li:nth-child(2) > a:nth-child(1)").click()
		time.sleep(2)
		self.md.find_element_by_css_selector("input.form-control").send_keys("产品")
		time.sleep(2)
		self.md.find_element_by_css_selector(".btn-success").click()
		time.sleep(2)


	def test_03_edit(self):
		#编辑记录
		self.md.find_element_by_css_selector(".btn-default").click()
		time.sleep(1)
		self.md.find_element_by_css_selector(".table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(6) > a:nth-child(1)").click()
		time.sleep(2)
		self.md.find_element_by_css_selector(".form-control").clear()
		self.md.find_element_by_css_selector(".form-control").send_keys("产品状态异常")
		time.sleep(1)
		xx = self.md.find_element_by_class_name("ke-edit-iframe")
		self.md.switch_to.frame(xx)
		time.sleep(1)
		self.md.find_element_by_xpath("/html/body").send_keys(Keys.TAB)
		self.md.find_element_by_xpath("/html/body").clear()
		self.md.find_element_by_xpath("/html/body").send_keys("123564")
		self.md.switch_to.default_content()
		time.sleep(1)
		self.md.find_element_by_css_selector(".btn").click()
		time.sleep(1)

	def test_04_del(self):
		time.sleep(4)
		#刷新
		self.md.find_element_by_css_selector(".btn-default").click()
		time.sleep(1)
		#删除一条记录
		self.md.find_element_by_css_selector(".table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(6) > span:nth-child(2)").click()
		time.sleep(2)
		self.md.find_element_by_css_selector(".layui-layer-btn0").click()
		time.sleep(2)
		self.md.find_element_by_css_selector(".btn-default").click()
		# tx1 = self.md.find_element_by_css_selector(".table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(3)").text
		# self.assertNotEqual(tx,tx1,msg="删除失败")
		#批量删除
		self.md.find_element_by_css_selector(".table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(1) > input:nth-child(1)").click()
		target_elem = self.md.find_element_by_css_selector("#del")
		self.md.execute_script("return arguments[0].scrollIntoView();", target_elem)
		target_elem.click()
		time.sleep(1)
		alert = self.md.switch_to.alert
		alert.accept()
		time.sleep(2)
		xx =self.md.switch_to.alert.text
		ale = self.md.switch_to.alert
		time.sleep(2)
		ale.accept()
		return xx