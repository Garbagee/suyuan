
'''
项目名称:产品溯源系统
所属模块:溯源实例管理/溯源操作记录
日期:2020/11/06
作者:李锦龙
版本:version:1.0
'''
import time
from public.common import loginTo

class SourceRecord():
	ms = loginTo.LoginTo()
	md = ms.driver

	def test_search(self):
		# 搜索功能
		# time.sleep(1)
		# self.md.find_element_by_link_text("溯源实例管理").click()
		time.sleep(1)
		self.md.find_element_by_link_text("溯源操作记录").click()
		time.sleep(2)
		self.md.find_element_by_css_selector("input.form-control").send_keys("2020")
		time.sleep(2)
		self.md.find_element_by_css_selector(".btn-success").click()
		time.sleep(2)


	def test_del(self):
		#刷新
		self.md.find_element_by_css_selector(".btn-default").click()
		time.sleep(1)
		#删除一条记录
		self.md.find_element_by_css_selector(".table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(3) > span:nth-child(1)").click()
		time.sleep(2)
		self.md.find_element_by_css_selector(".layui-layer-btn0").click()
		time.sleep(2)
		self.md.find_element_by_css_selector(".btn-default").click()
		# tx1 = self.md.find_element_by_css_selector(".table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(3)").text
		# self.assertNotEqual(tx,tx1,msg="删除失败")
		#批量删除
		self.md.find_element_by_css_selector(".table > tbody:nth-child(2) > tr:nth-child(25) > td:nth-child(1) > input:nth-child(1)").click()
		target_elem = self.md.find_element_by_css_selector("#del")
		self.md.execute_script("return arguments[0].scrollIntoView();", target_elem)
		target_elem.click()
		time.sleep(1)
		alert = self.md.switch_to.alert
		alert.accept()
		time.sleep(1)
		xx = self.md.switch_to.alert.text
		ale = self.md.switch_to.alert
		time.sleep(2)
		ale.accept()
		return xx