# #university = r"Inha\nUniversity" # r : 보이는 그대로 찍는
# university = "Inha\nUniversity"
# #print(university)
#
# print(university[:-11])
# print(university[::2])
#
# subjects = ["python", "c++", "database"]
# subjects_string = " / ".join(subjects)
# print(subjects_string)

# course = "* KEB 2024# KEB !Bootcamp KEB...*!#"
# print(course.find('KEB'))
# print(course.rfind('KEB')) # 뒤에서 찾는거
# print(course.index('KEB'))
# print(course.rindex('KEB'))
# print(course.find('Inha'))  # -1 find 와 index의 차이 : find는 없으면 -1 return, index는 없으면 에러
# #print(course.index('Inha'))  # ValueError: substring not found
# print(course)
# course = course.replace('KEB', 'Inha', 3)
# print(course)
# print(course.strip())
# print(course.strip("!#.*"))
# print(course.lstrip("!#*.")) # 혹은 rstrip

# print(course)
# print(course.replace('KEB', 'Inha'))
# print(course)
# course = course.replace('KEB', 'Inha')
# print(course)

# preview
subjects = "python c++ database linux"
print('%e' % 0.7045)
print(subjects.isalnum()) # al : alphabet
subject = input("수강신청과목 입력 : ")
try:
    print(f"해당 과목이 존재합니다. 위치는 {subjects.index(subject)}번 인덱스입니다.")
except ValueError:
    print('해당과목이 존재하지 않습니다')