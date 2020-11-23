'''
项目名称:产品溯源系统
所属模块:流程记录管理/新增流程类别
日期:2020/11/03
作者:李锦龙
版本:version:1.0
'''
import time
from public.common import loginTo

# @ddt
class ProcessRecord():


	# @data(*ms)
	# @unpack
	mf = loginTo.LoginTo()
	md = mf.driver


	def test_02_pre(self):
		# 定位流程记录管理功能
		time.sleep(2)
		# self.driver.find_element_by_css_selector(".sub-menu:nth-child(3) span:nth-child(2)").click()
		self.md.find_element_by_link_text("流程记录管理").click()
		time.sleep(2)
		self.md.find_element_by_link_text("新增流程类别").click()

	def test_02_addRecord(self,p1,p2):

		time.sleep(2)
		self.md.find_element_by_css_selector(".col-sm-4 > input:nth-child(1)").send_keys(p1)
		self.md.find_element_by_css_selector("div.form-group:nth-child(2) > div:nth-child(2) > input:nth-child(1)").send_keys(p2)
		time.sleep(2)
		self.md.find_element_by_css_selector(".btn").click()
		time.sleep(0.5)

