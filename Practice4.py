# 리스트[]

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

print(subway.index("조세호"))  # 위치

subway.append("하하")  # 맨 뒤에 삽입
print(subway)

subway.insert(1, "정형돈")  # 원하는 자리에 삽입
print(subway)

print(subway.pop())  # 맨 뒤의 값을 뺀다.
print(subway)

subway.append("유재석")
print(subway)
print(subway.count("유재석"))  # 원하는 값을 카운트

num_list = [5, 2, 4, 3, 1]
num_list.sort()
print(num_list)  # 정렬

num_list.reverse()
print(num_list)  # 역순 정렬

num_list.clear()
print(num_list)  # 모두 지우기

num_list = [5, 2, 4, 3, 1]
mix_list = ["조세호", 20, True]  # 다양한 자료형도 가능

num_list.extend(mix_list)  # 리스트 합치기도 가능
print(num_list)


# 사전(딕셔너리)
cabinet = {3: "유재석", 100: "김태호"}
print(cabinet[3])  # 값이 없을 경우 오류
print(cabinet.get(3))  # 값이 없을 경우 None
print(cabinet.get(5, "사용 가능"))

print(3 in cabinet)  # True
print(5 in cabinet)  # False

cabinet[3] = "김종국"
cabinet[4] = "조세호"
print(cabinet)

del cabinet[3]
print(cabinet)

print(cabinet.keys())  # key 만 출력
print(cabinet.values())  # value 만 출력
print(cabinet.items())  # key, value 쌍으로 출력

cabinet.clear()  # 전부 비움
print(cabinet)


# 튜플
menu = ("돈까스", "치즈까스")  # 값 추가나 변경은 불가능.
print(menu[0])
print(menu[1])

# 튜플 활용
(name, age, hobby) = ("김종국", 20, "코딩")


# 집합 (set)
# 중복 안됨, 순서 없음
my_set = {1, 2, 3, 3, 3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])
print(java & python)  # 교집합
print(java.intersection(python))

print(java | python)  # 합집합
print(java.union(python))

print(java-python)  # 차집합
print(java.difference(python))

python.add("김태호")  # 추가
print(python)

java.remove("김태호")  # 삭제
print(java)


# 자료구조의 변경
menu2 = {"커피", "우유", "주스"}
print(menu2, type(menu2))

menu2 = list(menu2)
print(menu2, type(menu2))

menu2 = tuple(menu2)
print(menu2, type(menu2))
