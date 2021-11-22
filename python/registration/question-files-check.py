# Сохраяем ИД пользователя/ИД ответа/значение ответа
# Собираем ответы - делаем словарь ответов и возвращаем
# Возвращаем список словарей-ответов   
import os

def start_file():
    f = open('users_data.csv','w')    
    f.close()

def insert_data(id,question_id,question_value):
    f = open('users_data.csv','a')
    file_out = f"{id};{question_id};{question_value};"
    f.write(file_out+'\n')
    f.close()
    print("Heelo")


# Собирем словарь
def check_questions():
    f = open('users_data.csv','r')
    # d = dict()
    key_list = []
    user_list = []
    for line in f:
        elements = line.split(';')
        elements.pop()
        key_list.append(elements[1])
        user_list.append(elements[0])
    f.close()
    key_set = set(key_list)
    user_set = set(user_list)
    user_lst = list(user_set) 
    key_lst = list(key_set)
    user_lst.sort()
    key_lst.sort()

    dict_list = []
    for usr in user_lst:

        data_list = ['user']
        data_list.extend(key_lst)
        total_dict = dict.fromkeys(data_list,None)
        total_dict.update({"user":usr})
        dict_list.append(total_dict)
    f = open('users_data.csv','r')
    for line in f:
        elements = line.split(';')
        elements.pop()
        indx = user_lst.index(elements[0])
        dict_list[indx].update({elements[1]:elements[2]})
    
    print(dict_list)
    return dict_list

# total_dict = dict.fromkeys(cat_list_value(),0)

# fin_list = []
# f = open('costs_list.txt','r')
# for line in f:
#     elements = line.split(' ')
#     lst = [elements[0][1:],int(elements[1])]
#     fin_list.append(lst)

# for lst in fin_list:
#     total_dict[lst[0]] = total_dict[lst[0]] + lst[1]

# print(total_dict)

# insert_data(222,"start","1")
# insert_data(222,"quiz","0")
# insert_data(222,"finish","1")
# insert_data(222,"go","1")

# check_questions()
f = open('users_data.csv','r')
# список участников

numbers = []
for line in f:
    elements = line.split(";")
    numbers.append(elements[0])
nums = set(numbers)
# print(nums)
numbers = list(nums)

lst = []

for n in numbers:
    lst.append([])

print(numbers)
f.close()
f = open('users_data.csv','r')
question_code = ["quest_start_video","quest_present_lesson","quest_present_teacher","quest_present_company","quest_student_meet","quest_about_IT","quest_about_sphere","quest_practic_block","quest_grow_stairs","quest_softs","quest_projects","quest_methodiks","quest_price","quest_discount","quest_year","quest_end_slide"]
id = '679521347'
reg_status = []
for i in range(len(question_code)):
    reg_status.append(0)
print(reg_status)
d = dict.fromkeys(question_code,None)
dd = {"id":"414514928","value":d}
listdd = []
listdd.append(dd)
listdd.append(dd)

# Функция получат id и возвращает строку reg_status

def id_reg_status(id):
    # Читаем список типов данных
    f = open('users_data_types.csv','r')
    for line in f:
        question_code = line.split(';')
    question_code.pop()
    f.close()
    # Читаем - есть ли элемент
    f = open('users_data.csv','r')
    reg_status = []
    for i in range(len(question_code)):
        reg_status.append(0)
    for line in f:
        elements = line.split(";")
        if elements[0] == id:
            for i in range(len(question_code)):
                if elements[1]==question_code[i]:
                    reg_status[i] = 1
    f.close()
    return reg_status

for line in f:
    elements = line.split(";")
    for i in range(len(numbers)): 
        if elements[0] ==numbers[i]:
            lst[i].append([elements[1],elements[2]])
print(id_reg_status('394735340'))
print(listdd[1])
f.close()
