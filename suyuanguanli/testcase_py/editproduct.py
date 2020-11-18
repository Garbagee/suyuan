import requests
from requests_toolbelt.multipart import MultipartEncoder
from testcase_py.common import login

class AddProduct():
	lg = login.Login()
	ck = lg.lg()
	cookie = 'PHPSESSID='+ck
	def addProduct(self):

		url = "http://123.57.140.190/manage/edit_cp.php?act=save_edit_pro"
		payload=MultipartEncoder( {
				'id':'300',
				'pro_name':'wghjk',
				'cpbh': 'sadfasdf',
				'cptxm':'3525558f5522',
				'cpms':'1115ss5511'
		})
		headers = {'Content-Type': payload.content_type,
				   'Cookie':self.cookie}
		r = requests.post(url,headers=headers,data=payload)
		print(r.text)
