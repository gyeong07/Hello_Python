# # if

# weather = input("오늘 날씨는 어때요? ")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요.")

# temp = int(input("기온은 어때요?"))
# if 30 <= temp:
#     print("너무 더워요. 나가지 마세요")
# elif 10 <= temp < 30:
#     print("괜찮은 날씨에요")
# elif 0 <= temp < 10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요. 나가지 마세요")


# 반복문 for

# for waiting_no in range(5):
#     print(f"대기번호: {waiting_no}")

# starbucks = ["아이언맨", "토르", "아이엠 그루트"]
# for customer in starbucks:
#     print(f"{customer}, 커피가 준비 되었습니다.")


# 반복문 while

# customer = "토르"
# index = 5
# while index >= 1:
#     print(f"{customer}, 커피가 준비 되었습니다. {index} 번 남았어요.")
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분 되었습니다.")

# customer="아이언맨"
# index=1
# while True:
#     print(f"{customer}, 커피가 준비 되었습니다. 호출 {index} 회.")

# customer="토르"
# person="Unknown"

# while person != customer:
#     print(f"{customer}, 커피가 준비 되었습니다.")
#     person=input("이름이 어떻게 되세요?")


# continue, break
absent = [2, 5]
no_book = [7]
for student in range(1, 11):  # 1,2,3,4,5,6,7,8,9,10
    if student in absent:
        continue
    elif student in no_book:
        print(f"오늘 수업 여기까지. {student}는 교무실로 따라와.")
        break
    print(f"{student}, 책을 읽어봐")


# 한줄 for문
student = [1, 2, 3, 4, 5]
print(student)
student = [i+100 for i in student]
print(student)

student = ["Iron man", "Thor", "I am groot"]
student = [len(i) for i in student]
print(student)

student = ["Iron man", "Thor", "I am groot"]
student = [i.upper() for i in student]
print(student)
