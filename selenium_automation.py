from selenium import webdriver
import selenium
from selenium.webdriver.common import keys
import time

browser = webdriver.Chrome(r"C:\chromedriver.exe")
browser.get("https://www.seleniumeasy.com/test/table-sort-search-demo.html")
        
time.sleep(5)
browser.find_element_by_name('example_length').send_keys(100)

user_data_1 = browser.find_elements_by_class_name('odd')
user_data_2 = browser.find_elements_by_class_name('even')

all_users = user_data_1 + user_data_2

user_list = []
users_in_san_francisco = []

def get_user_data(user):
    for i in range(len(all_users)):
        users = all_users[i].text
        user_list.append(users)


    for i in user_list:
        if 'San Francisco' in i:
            # print('Found San Francisco')
            # print(i)
            users_in_san_francisco.append(i)

    for i in users_in_san_francisco:
        data = i.split(' ')
        users = " ".join(data[0:2])
        print(users)
    return users    

def get_all_user_age():
    for i in users_in_san_francisco:
        data = i.split(' ')
        age = data[7]
        print(age)
    return age

get_user_data(user_list)
#get_all_user_age()
time.sleep(5)
browser.close()






# user_list = []

# for i in range(len(user_data_1)):
#     user_in_sanfrancisco = user_data_1[i].text
#     user_list.append(user_in_sanfrancisco)
#     print(user_in_sanfrancisco)

# for i in range(len(user_data_2)):
#     user_in_sanfrancisco = user_data_2[i].text
#     user_list.append(user_in_sanfrancisco)
#     print(user_in_sanfrancisco)

# #print(user_list)

# sorted_list = []
# for i in user_list:
#     sorted_list.append(i.split(' '))

# print(sorted_list)


