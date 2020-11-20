
'''
项目名称:产品溯源系统
所属模块:溯源实例管理/新增溯源实例
日期:2020/11/06
作者:李锦龙
版本:version:1.0
'''
import time

from selenium.webdriver.common.keys import Keys

from public.common import loginTo

class AddSource():
	ms = loginTo.LoginTo()
	md = ms.driver

	def test_01_pre(self):
		self.md.find_element_by_link_text("溯源实例管理").click()
		time.sleep(1)
		# self.md.find_element_by_link_text("新增溯源实例").click()
		# time.sleep(1)

	#溯源实例管理
	def test_02_add(self,a,b):

		self.md.find_element_by_css_selector(".form-control").send_keys(a)
		f1 = self.md.find_element_by_css_selector(".ke-edit-iframe")
		xx = self.md.switch_to.frame(self.md.find_element_by_class_name("ke-edit-iframe"))
		time.sleep(1)
		self.md.find_element_by_xpath("/html/body").send_keys(Keys.TAB)
		self.md.find_element_by_xpath("/html/body").send_keys(b)
		time.sleep(1)
		self.md.switch_to.default_content()
		self.md.find_element_by_css_selector(".btn").click()
		time.sleep(1)



