# 문자열
sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)


# 슬라이싱
jumin = '210707-1234567'

print("성별: " + jumin[7])
print("연: " + jumin[0:2])  # 0부터 2 직전까지
print("월: " + jumin[2:4])
print("일: " + jumin[4:6])

print("생년월일: " + jumin[:6])  # 처음부터 6 직전까지
print("뒤 7자리: " + jumin[7:])  # 7번부터 끝까지
print("뒤 7자리 (뒤부터): " + jumin[-7:])  # -7번째부터 끝까지


# 문자열 처리 함수
python = "Python is Amazing"
print(python.lower())  # 전부 소문자로
print(python.upper())  # 전부 대문자로
print(python[0].isupper())  # 0번째 글자가 대문자인지
print(len(python))  # 문자열의 길이
print(python.replace("Python", "Java"))  # 문자열 변경

index = python.index("n")
print(index)  # n의 위치 반환
index = python.index("n", index+1)  # 첫번째 n 자리에서 1을 더한 6부터 n의 위치 탐색

print(python.find("Java"))  # 없는 문자일 경우 -1반환
# print(python.index("Jave")) # 없는 문자일 경우 신택스 오류

print(python.count("n"))  # n이 몇개인지 센다.


# 문자열 포맷
# 방법 1
print("나는 %d살입니다." % 20)
print("나는 %s을 좋아해요." % "파이썬")
print("Apple은 %c로 시작해요." % "A")
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# 방법 2
print("나는 {}살입니다.".format(20))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨간"))

# 방법 4(v3.6 이상~)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")


# 탈출문자
print("백문이 불여일견\n백견이 불여일행")
print("저는 \"푸들\"입니다.")
print("Red Apple\rPine")  # \r: 커서를 맨 앞으로 이동
print("Redd\bApple")  # \b: 백스페이스
print("Red\tApple")  # \t: tab을 누른 만큼의 띄어쓰기 (4칸 혹은 8칸)
