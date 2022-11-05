from enum import unique
import requests
from requests.structures import CaseInsensitiveDict

url = "https://ngodarpan.gov.in/index.php/ajaxcontroller/show_ngo_info"

headers = CaseInsensitiveDict()
headers["Accept"] = "*/*"
headers["Accept-Language"] = "en-US,en;q=0.9"
headers["Cache-Control"] = "max-age=0"
headers["Connection"] = "keep-alive"
headers["Sec-Fetch-Dest"] = "empty"
headers["Sec-Fetch-Mode"] = "cors"
headers["Sec-Fetch-Site"] = "same-origin"
headers["Sec-Fetch-User"] = "?1"
headers["Upgrade-Insecure-Requests"] = "1"
headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
headers["sec-ch-ua"] = '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"'
headers["sec-ch-ua-mobile"] = "?0"
headers["sec-ch-ua-platform"] = "Windows"
headers["Referer"] = "https://ngodarpan.gov.in/index.php/home/statewise_ngo/8532/29/1"
headers["Cookie"] = "csrf_cookie_name=b4597e747a568f3bd6292ead0afe0942; ci_session=voksi8bqj7084hpqetdic1rrovdoj4q9"
headers["Origin"] = "https://ngodarpan.gov.in"
headers["X-Requested-With"] = "XMLHttpRequest"
headers["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
data = "id=311095&csrf_test_name=b4597e747a568f3bd6292ead0afe0942"
resp = requests.post(url, headers=headers, data=data)
unique_id=resp.json()['infor']['0']['UniqueID']
registered_with=resp.json()["registeration_info"]['reg_name']
type_of_ngo=resp.json()["registeration_info"]['TypeDescription']
reg_no=resp.json()["registeration_info"]['nr_regNo']
if reg_no:
    data_Copy_of_Registration_Certificate='Available'
    data_copy_of_pan_card='Available'
else:
    data_Copy_of_Registration_Certificate='Not Available'
    data_copy_of_pan_card='Not Available'
act_name_data=resp.json()["registeration_info"]['nr_actName']
data_city_of_reg=resp.json()["registeration_info"]['nr_city']
data_state_name=resp.json()["registeration_info"]['StateName']
data_reg_date=resp.json()["registeration_info"]['ngo_reg_date']
memeber_names_data=resp.json()["member_info"]['FName']
member_email_data=resp.json()["member_info"]['EmailId']
member_desg_data=resp.json()["member_info"]['DesigName']
member_mobile_data=resp.json()["member_info"]['MobileNo']
fcra_avai=resp.json()["registeration_info"]['nr_isFcra']
if fcra_avai=='N':
    fcra_avai='Not Available'
fcra_reg_no=resp.json()["registeration_info"]['fcrano']
address_data=resp.json()["registeration_info"]['nr_add']
MobileNo_data=resp.json()['infor']['0']['MobileNo']
url_data=(resp.json()['infor']['0']['ngo_url'])
email_data=resp.json()['infor']['0']['ngo_url']



# print(json_data['UniqueID'])


