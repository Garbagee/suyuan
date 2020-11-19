import xlrd
'''
项目名称:产品溯源系统
所属模块:公共（获取excel书库）
日期:2020/11/03
作者:李锦龙
版本:version:1.0
'''
class GetData():
	def __init__(self,filepath,name ="sheet1"):
		self.data = xlrd.open_workbook(filepath)

		self.table = self.data.sheet_by_index(0)
		self.table = self.data.sheet_by_name(name)
		self.keys = self.table.row_values(0)
		self.rowNUM = self.table.nrows

	def login_data(self):
		if self.rowNUM < 1:
			print("总行数小于1")
		else:
			result = []
        # 按行读取表格内容添加到result列表中，方便调用
			for line in range(self.rowNUM):
				shuju = self.table.row_values(line)
				result.append(shuju)
			# print(result)
			return result



# if __name__ == '__main__':
# 	xx = GetData("D:\\pycharm\\产品溯源系统测试\\data\\testdata\\data.xlsx")
# 	xx.login_data()

