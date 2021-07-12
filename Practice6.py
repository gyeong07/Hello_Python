# def open_account():
#     print("새로운 계좌가 생성되었습니다.")


# def deposit(balance, money):
#     print(f"입금이 완료 되었습니다. 잔액은 {balance+money} 원 입니다.")
#     return balance+money


# def withdraw(balance, money):
#     if balance >= money:
#         print(f"출금이 완료되었습니다. 잔액은 {balance-money} 원 입니다.")
#         return balance-money
#     else:
#         print(f"출금이 완료되지 않았습니다. 잔액은 {balance} 원 입니다.")
#         return balance


# def withdraw_night(balance, money):
#     commission = 100  # 수수료 100원
#     return commission, balance-money-commission


# balance = 0  # 잔액
# balance = deposit(balance, 1000)
# # balance = withdraw(balance, 2000)
# # balance = withdraw(balance, 500)
# commission, balance = withdraw_night(balance, 500)
# print(f"수수료 {commission} 원이며, 잔액은 {balance} 원입니다.")

# def profile(name, age, main_lang):
#     print(f"이름: {name}\t나이: {age}\t주 사용 언어: {main_lang}")


# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

# 같은 학교 같은 학년 같은 반 같은 수업.

# def profile(name, age=17, main_lang="파이썬"):
#     print(f"이름: {name}\t나이: {age}\t주 사용 언어: {main_lang}")


# profile("유재석")
# profile("김태호")


# 키워드값

# def profile(name, age, main_lang):
#     print(name, age, main_lang)


# profile(name="유재석", main_lang="파이썬", age=20)
# profile(main_lang="자바", age=25, name="김태호")


# #가변인자
# def profile(name,age,lang1,lang2,lang3,lang4,lang5):
#     print("이름: {0}\t나이: {1}\t".format(name,age),end=" ")
#     print(lang1,lang2,lang3,lang4,lang5)


# def profile(name, age, *language):
#     print("이름: {0}\t나이: {1}\t".format(name, age), end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print()


# profile("유재석", 20, "python", "java", "C", "C++", "C#", "javascript")
# profile("김태호", 25, "kotlin", "swift")

gun = 10


def checkpoint(soldiers):
    global gun
    gun = gun-soldiers
    print("[함수 내] 남은 총: {0}", format(gun))


def checkpoint_ret(gun, soldiers):
    gun = gun-soldiers
    print("[함수 내] 남은 총: {0}".format(gun))
    return gun


print("전체 총: {0}".format(gun))
# checkpoint(2)
gun = checkpoint_ret(gun, 2)
print("남은 총: {0}".format(gun))
