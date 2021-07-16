# import sys
# print("Python", "Java", "Javascript", sep=",", end="?")
# print("무엇이 더 재밌을까요?")

# print("Python", "Java", file=sys.stdout)
# print("Python", "Java", file=sys.stderr)  # 표준 에러

# scores = {"수학": 0, "영어": 50, "코딩": 100}
# for subject, score in scores.items():
#     print(subject.ljust(8), str(score).rjust(4), sep=":")


# for num in range(1, 21):
#     print("대기번호: "+str(num).zfill(3))


# # 표준 입력
# answer = input("아무 값이나 입력하세요: ")
# print("입력하신 값은 "+answer+"입니다.")


# # 다양한 출력 포맷
# print("{0: >10}".format(500))  # 빈 자리는 빈공간으로 두고, 오른쪽 정렬, 총 10자리 공간 확보
# print("{0: >+10}".format(500))  # 양수일 땐 +, 음수일 땐 -
# print("{0: >+10}".format(-500))
# print("{0:_<+10}".format(500))  # 왼쪽 정렬, 빈칸으로 _ 채움
# print("{0:+,}".format(-100000000000))  # 3자리마다 콤마를 찍어주기
# print("{0:+,}".format(100000000000))  # 3자리마다 콤마 찍기, +- 부호도 붙이기
# print("{0:^<+30,}".format(10000000000))  # 3자리마다 콤마, 부호, 자릿수 확보, 빈자리는 ^ 채워주기
# print("{0:f}".format(5/3))  # 소수점 출력
# print("{0:.2f}".format(5/3))  # 소수점 출력(소수점 3째자리에서 반올림)


# 파일입출력
# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학: 80")
# score_file.write("\n코딩: 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# # print(score_file.readline())  # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# # print(score_file.readline())
# # print(score_file.readline())
# # print(score_file.readline())
# # score_file.close()

# # while True:
# #     line = score_file.readline()
# #     if not line:
# #         break
# #     print(line, end="")
# # score_file.close()

# lines = score_file.readlines()  # list형태로 저장
# for line in lines:
#     print(line, end="")
# score_file.close()


# pickle : 데이터를 파일 형태로 저장. 피클을 이용해서 파일을 가져와 코드에서 쓸 수 있음.

# import pickle
# profile_file = open("profile.pickle", "wb")
# profile = {"이름": "박명수", "나이": 30, "취미": ["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file)  # profile에 있는 정보를 file에 저장
# profile_file.close()

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file)  # file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()


# with 사용
# import pickle

# with open("profile.pickle", "rb")as profile_file:
#     print(pickle.load(profile_file))
# with open("study.txt", "w", encoding="utf8")as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt", "r", encoding="utf8")as study_file:
    print(study_file.read())
