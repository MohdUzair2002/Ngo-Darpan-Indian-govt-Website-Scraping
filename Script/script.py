from time import sleep
import requests
from bs4 import BeautifulSoup
from enum import unique
import requests
from requests.structures import CaseInsensitiveDict
import csv
main_data=[]
length=int (input("Enter the total no of  of the pages in this state"))
s=requests.Session()

i=77
unique_id_list=[]
req_with_list=[]
type_of_ngo_list=[]
reg_no_list=[]
data_Copy_of_Registration_Certificate_list=[]
act_name_data_list=[]
data_city_of_reg_list=[]
data_state_name_list=[]
data_reg_date_list=[]
memeber_names_data_list=[]
member_email_data_list=[]
member_desg_data_list=[]
member_mobile_data_list=[]
fcra_avai_list=[]
data_copy_of_pan_card_list=[]
fcra_reg_no_list=[]
address_data_list=[]
MobileNo_data_list=[]
url_data_list=[]
email_data_list=[]
Telephone_data_list=[]
name=[]
reg=[]
add=[]
sector=[]
length_IDS=[]
file_name='West Bengal3'
id_123='11243/19'
try:
    while(i<length):
        
        print(i+1)
        r=s.get(f"https://ngodarpan.gov.in/index.php/home/statewise_ngo/{id_123}/{i+1}?per_page=100")

        soup = BeautifulSoup(r.content,"html.parser")

        rows=soup.find("table",{"class":"Tax"}).find("tbody").findAll("tr")
        
        IDS=[]

        for row in rows:
            ID=row.findAll("td")[1].find("a")["onclick"].split('"')[1]
            name_data=str(row.findAll("td")[1].find("a")).split('>')[1].split('<')[0]
            name.append(name_data)
            reg1=str(row.findAll("td")[2]).replace('<td>',"").replace('</td>',"")
            reg.append(reg1)
            address=str(row.findAll("td")[3]).replace('<td>',"").replace('</td>',"")
            add.append(address)
            sector_data=str(row.findAll("td")[4]).replace('<td>',"").replace('</td>',"")
            sector.append(sector_data)
            IDS.append(ID)
        print(name)
        print(add)
        print(sector)
        print(IDS)
        print(len(IDS))
        length_IDS.append(len(IDS))
        
        url = "https://ngodarpan.gov.in/index.php/ajaxcontroller/show_ngo_info"
        # cookies=str(t.cookies)
        # cookies=cookies[44:80].split('for')[0]
        t=s.get("https://ngodarpan.gov.in/index.php/ajaxcontroller/get_csrf")
        csrf=t.json()['csrf_token']
        headers = CaseInsensitiveDict()
        headers["Accept"] = "*/*"
        headers["Accept-Language"] = "en-US,en;q=0.9"
        headers["Cache-Control"] = "max-age=0"
        headers["Connection"] = "keep-alive"
        # headers["Cookie"] = f"ci_session=4ajakmgo76c7tukn5ue9p0t8rk3nralm; csrf_cookie_name={csrf}"
        headers["Cookie"] = f"csrf_cookie_name={csrf}"
        headers["Sec-Fetch-Dest"] = "empty"
        headers["Sec-Fetch-Mode"] = "cors"
        headers["Sec-Fetch-Site"] = "same-origin"
        headers["Sec-Fetch-User"] = "?1"
        headers["Upgrade-Insecure-Requests"] = "1"
        headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
        headers["sec-ch-ua"] = "Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"
        headers["sec-ch-ua-mobile"] = "?0"
        headers["sec-ch-ua-platform"] = "Windows"
        headers["Referer"] = f"https://ngodarpan.gov.in/index.php/home/statewise_ngo/{id_123}/1?per_page=100"
        headers["Origin"] = "https://ngodarpan.gov.in"
        headers["X-Requested-With"] = "XMLHttpRequest"
        headers["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
        g=0
        while(g <len(IDS)):
                try:
            
                    data = f"id={IDS[g]}&csrf_test_name={csrf}"
                
                    resp = s.post(url, headers=headers, data=data)
                except:
                    t=s.get("https://ngodarpan.gov.in/index.php/ajaxcontroller/get_csrf")
                    csrf=t.json()['csrf_token']
                    headers = CaseInsensitiveDict()
                    headers["Accept"] = "*/*"
                    headers["Accept-Language"] = "en-US,en;q=0.9"
                    headers["Cache-Control"] = "max-age=0"
                    headers["Connection"] = "keep-alive"
                    headers["Cookie"] = f"ci_session=4ajakmgo76c7tukn5ue9p0t8rk3nralm; csrf_cookie_name={csrf}"
                    headers["Sec-Fetch-Dest"] = "empty"
                    headers["Sec-Fetch-Mode"] = "cors"
                    headers["Sec-Fetch-Site"] = "same-origin"
                    headers["Sec-Fetch-User"] = "?1"
                    headers["Upgrade-Insecure-Requests"] = "1"
                    headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
                    headers["sec-ch-ua"] = "Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"
                    headers["sec-ch-ua-mobile"] = "?0"
                    headers["sec-ch-ua-platform"] = "Windows"
                    headers["Referer"] = f"https://ngodarpan.gov.in/index.php/home/statewise_ngo/{id_123}?per_page=100"
                    headers["Origin"] = "https://ngodarpan.gov.in"
                    headers["X-Requested-With"] = "XMLHttpRequest"
                    headers["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
                    data = f"id={IDS[g]}&csrf_test_name={csrf}"
                    resp = requests.post(url, headers=headers, data=data)     
            
                unique_id=resp.json()['infor']['0']['UniqueID']
                unique_id_list.append(unique_id)
                registered_with=resp.json()["registeration_info"][0]['nr_regNo']
                print(registered_with)
                req_with_list.append(registered_with)
                type_of_ngo=resp.json()['registeration_info'][0]['TypeDescription']
                type_of_ngo_list.append(type_of_ngo)
                reg_no=resp.json()['registeration_info'][0]['nr_regNo']
                reg_no_list.append(reg_no)
                if reg_no:
                    data_Copy_of_Registration_Certificate='Available'
                    data_copy_of_pan_card='Available'
                    data_Copy_of_Registration_Certificate_list.append(data_Copy_of_Registration_Certificate)
                    data_copy_of_pan_card_list.append(data_copy_of_pan_card)
                else:
                    data_Copy_of_Registration_Certificate='Not Available'
                    data_copy_of_pan_card='Not Available'
                    data_Copy_of_Registration_Certificate_list.append(data_Copy_of_Registration_Certificate)
                    data_copy_of_pan_card_list.append(data_copy_of_pan_card)
                act_name_data=resp.json()['registeration_info'][0]['nr_actName']
                act_name_data_list.append(act_name_data)
                data_city_of_reg=resp.json()["registeration_info"][0]['nr_city']
                data_city_of_reg_list.append(data_city_of_reg)
                data_state_name=resp.json()["registeration_info"][0]['StateName']
                data_state_name_list.append(data_state_name)
                data_reg_date=resp.json()["registeration_info"][0]['ngo_reg_date']
                data_reg_date_list.append(data_reg_date)
                members_name_lis=[]
                members_email_lis=[]
                members_mobileno_lis=[]
                members_desg_lis=[]
                
                try:
                    memeber_names_data0=resp.json()["member_info"][0]['FName']
                    member_email_data0=resp.json()["member_info"][0]['EmailId']
                    member_desg_data1=resp.json()["member_info"][0]['DesigName']
                    member_mobile_data0=resp.json()["member_info"][0]['MobileNo']
                    members_mobileno_lis.append(member_mobile_data0)

                    members_desg_lis.append(member_desg_data1)
                    members_name_lis.append(memeber_names_data0)
                    members_email_lis.append(member_email_data0)
                except:
                    pass
                try:
                    memeber_names_data1=resp.json()["member_info"][1]['FName']
                    member_email_data1=resp.json()["member_info"][1]['EmailId']
                    member_desg_data2=resp.json()["member_info"][1]['DesigName']
                    member_mobile_data1=resp.json()["member_info"][0]['MobileNo']
                    members_name_lis.append(memeber_names_data1)
                    members_email_lis.append(member_email_data1)
                    members_mobileno_lis.append(member_mobile_data1)
                    members_desg_lis.append(member_desg_data2)
                except:
                    pass
                try:
                    member_email_data2=resp.json()["member_info"][2]['EmailId']
                    members_email_lis.append(member_email_data2)
                    member_mobile_data2=resp.json()["member_info"][0]['MobileNo']
                    members_mobileno_lis.append(member_mobile_data2)
                    member_desg_data3=resp.json()["member_info"][2]['DesigName']
                    members_desg_lis.append(member_desg_data3)
                    memeber_names_data2=resp.json()["member_info"][2]['FName']
                    members_name_lis.append(memeber_names_data2)
                except:
                    pass
                
                member_email_data_list.append(members_email_lis)
                
                memeber_names_data_list.append(members_name_lis)

                member_desg_data_list.append(members_desg_lis)
                
                
                member_mobile_data_list.append(members_mobileno_lis)
                fcra_avai=resp.json()["registeration_info"][0]['nr_isFcra']
                if fcra_avai=='N':
                    fcra_avai='Not Available'
                    fcra_avai_list.append(fcra_avai)
                else:
                    fcra_avai='Available'
                    fcra_avai_list.append(fcra_avai)
                fcra_reg_no=str(resp.json()["registeration_info"][0]['fcrano']).replace('""',"Not AVailable")
                fcra_reg_no_list.append(fcra_reg_no)
                address_data=resp.json()["registeration_info"][0]['nr_add']
                address_data_list.append(address_data)
                MobileNo_data=resp.json()['infor']['0']['Mobile']
                MobileNo_data_list.append(MobileNo_data)
                url_data=(resp.json()['infor']['0']['ngo_url'])
                url_data_list.append(url_data)
                email_data=resp.json()['infor']['0']['Email']
                email_data_list.append(email_data)
                print(g+1)
                try:
                    Telephone=resp.json()['infor']['0']['Telephone']
                    Telephone_data_list.append(Telephone)
                except:
                    Telephone='Not Available'
                    Telephone_data_list.append(Telephone)
                g+=1

        i+=1

    j=0

    while(j<len(unique_id_list)):
            data1=[]
            data1.append(name[j])
            data1.append(reg[j])
            data1.append(add[j])
            data1.append(sector[j])
            data1.append(unique_id_list[j])
            data1.append(req_with_list[j])
            data1.append(type_of_ngo_list[j])
            data1.append(reg_no_list[j])

            data1.append(data_Copy_of_Registration_Certificate_list[j])
            data1.append(data_copy_of_pan_card_list[j])
            data1.append(act_name_data_list[j])
            data1.append(data_city_of_reg_list[j])
            data1.append(data_state_name_list[j])
            data1.append(data_reg_date_list[j])
            data1.append(memeber_names_data_list[j])
            data1.append(member_mobile_data_list[j])
            data1.append(member_email_data_list[j])
            data1.append(member_desg_data_list[j])
            data1.append(fcra_avai_list[j])
            data1.append(fcra_reg_no_list[j])
            data1.append(address_data_list[j])
            data1.append(data_city_of_reg_list[j])
            data1.append(data_state_name_list[j])
            data1.append(Telephone_data_list[j])
            data1.append(MobileNo_data_list[j])
            data1.append(url_data_list[j])
            data1.append(email_data_list[j])



            main_data.append(data1)
            j=j+1
    header = ['Name of VO/NGO','Registration No.,City & State','Address','Sectors working in','Unique ID of VO/ NGO','Registered With','Type of NGO','Registration No','Copy of Registration Certificate','Copy of Pan Card','Act name','City of Registration','State of Registration','Date of Registration','Name','Mobile Number','Email ID','Designation','FCRA Available','FCRA Registration no.','Address','City','State','Telephone','Mobile No','Website Url','E-mail']
    with open(f'{file_name}.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write multiple rows
        writer.writerows(main_data)   
except:
    
    j=0

    while(j<len(unique_id_list)):
            data1=[]
            data1.append(name[j])
            data1.append(reg[j])
            data1.append(add[j])
            data1.append(sector[j])
            data1.append(unique_id_list[j])
            data1.append(req_with_list[j])
            data1.append(type_of_ngo_list[j])
            data1.append(reg_no_list[j])

            data1.append(data_Copy_of_Registration_Certificate_list[j])
            data1.append(data_copy_of_pan_card_list[j])
            data1.append(act_name_data_list[j])
            data1.append(data_city_of_reg_list[j])
            data1.append(data_state_name_list[j])
            data1.append(data_reg_date_list[j])
            data1.append(memeber_names_data_list[j])
            data1.append(member_mobile_data_list[j])
            data1.append(member_email_data_list[j])
            data1.append(member_desg_data_list[j])
            data1.append(fcra_avai_list[j])
            data1.append(fcra_reg_no_list[j])
            data1.append(address_data_list[j])
            data1.append(data_city_of_reg_list[j])
            data1.append(data_state_name_list[j])
            data1.append(Telephone_data_list[j])
            data1.append(MobileNo_data_list[j])
            data1.append(url_data_list[j])
            data1.append(email_data_list[j])



            main_data.append(data1)
            j=j+1
    header = ['Name of VO/NGO','Registration No.,City & State','Address','Sectors working in','Unique ID of VO/ NGO','Registered With','Type of NGO','Registration No','Copy of Registration Certificate','Copy of Pan Card','Act name','City of Registration','State of Registration','Date of Registration','Name','Mobile Number','Email ID','Designation','FCRA Available','FCRA Registration no.','Address','City','State','Telephone','Mobile No','Website Url','E-mail']
    with open(f'{file_name} .csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write multiple rows
        writer.writerows(main_data)   