# from theater_module import price, price_morning
# from theater_module import *
# import theater_module as mv
# import theater_module
# theater_module.price(3)  # 3명이서 영화보러 갔을 때 가격
# theater_module.price_morning(4)  # 4명이서 조조할인
# theater_module.price_soldier(5)  # 5명의 군인

# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)


# price(3)
# price_morning(4)
# price_soldier(5)

# price(5)
# price_morning(6)


# from travel import vietnam
# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# from travel import *
# trip_to = vietnam.VietnamPackage()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()


# 모듈, 패키지 위치
# import inspect
# import random
# from travel import *
# print(inspect.getfile(random))
# print(inspect.getfile(thailand))


# 내장함수
# list of python builtins
# input: 사용자 입력을 받는 함수
# dir: 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# import random  # 외장함수
# print(dir())

# print(dir(random))
# lst = [1, 2, 3]
# [print(dir(lst))]
# name = "Jim"
# print(dir(name))


# 외장함수
# list of python modules
# glob: 경로 내의 폴더 / 파일목록 조회 (윈도우dir)
# import os
# import glob
# print(glob.glob("*.py"))

# # os: 운영체제에서 제공하는 기본 기능
# print(os.getcwd())  # 현재 디렉토리 표시

# folder = "sample_dir"

# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder)  # 폴더 생성
#     print(folder, "폴더를 생성합니다.")


# time: 시간관련 함수

# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
print("오늘 날짜는 ", datetime.date.today())
# timedelta: 두 날짜 사이의 간격
today = datetime.date.today()  # 오늘 날짜 저장
td = datetime.timedelta(days=100)  # 100일 저장
print("우리가 만난지 100일은", today+td)  # 오늘부터 100일 후
