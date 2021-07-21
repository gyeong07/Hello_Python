from random import *

# 일반 유닛


class Unit:
    def __init__(self, name, hp, speed):  # __init__ : 생성자, #self는 항상 적어야하고, 자기 자신의 변수에 접근이 가능
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))

    def move(self, location):
        print(f"{self.name} : {location} 방향으로 이동합니다. [속도 {self.speed}]")

    def damaged(self, damage):
        print(f"{self.name} : {damage} 데미지를 입었습니다.")
        self.hp -= damage
        print(f"{self.name}: 현재 체력은 {self.hp} 입니다.")
        if self.hp <= 0:
            print(f"{self.name} 이 파괴되었습니다.")


# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# marine3 = Unit("탱크", 150, 35)

# # 레이스: 공중 유닛 = 비행기, 클로킹 (상대방에게 보이지 않음)
# wraith1 = Unit("레이스", 80, 5)
# print(f"유닛 이름: {wraith1.name}, 공격력: {wraith1.damage}")

# # 마인드 컨트롤: 상대방 유닛을 내 것으로 만드는 것(빼앗음)
# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.clocking = True

# if wraith2.clocking == True:
#     print(f"{wraith2.name} 는 현재 클로킹 상태입니다.")


# 공격유닛
class AttcakUnit(Unit):
    def __init__(self, name, hp, speed, damage):  # __init__ : 초기화
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print(f"{self.name} : {location} 방향으로 적군을 공격합니다. [공격력 {self.damage}]")


# 마린
class Marine(AttcakUnit):
    def __init__(self):
        AttcakUnit.__init__(self, "마린", 40, 1, 5)

        # 스팀팩: 일정시간 동안 이동 및 공격 속도를 증가, 체력 10 감소
        def stimpack(self):
            if self.hp > 10:
                self.hp -= 10
                print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
            else:
                print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))


# 탱크
class Tank(AttcakUnit):
    # 시즈모드: 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능, 이동 불가.
    seize_developed = False  # 시즈모드 개발여부

    def __init__(self):
        AttcakUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return

        # 현재 시즈모드가 아닐 때 -> 시즈모드
        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        # 현재 시즈모드일 때 -> 시즈모드 해제
        else:
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False


# 드랍쉽: 공중 유닛 = 수송기. 마린 / 파이어뱃 / 탱크 등을 수송. 공격X
# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print(f"{name}: {location} 방향으로 날아갑니다. [속도 {self.flying_speed}]")


# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttcakUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttcakUnit.__init__(self, name, hp, 0, damage)  # 지상 speed = 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        self.fly(self.name, location)


# 레이스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False

    def clocking(self):
        if self.clocked == True:
            print("{0} : 클로킹 모드 해제합니다.".format(self.name))
            self.clocked = False
        else:
            print("{0} : 클로킹 모드 설정합니다.".format(self.name))
            self.clocked = True


# 발키리: 공중 공격 유닛, 한번에 14발 미사일 발사
# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")

# 벌쳐: 지상유닛, 기동성이 좋음
# vulture = AttcakUnit("벌쳐", 80, 10, 20)

# 배틀크루저: 공중유닛, 체력 굉장히 좋음, 공격력도 굿.
# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# battlecruiser.fly(battlecruiser.name, "9시")
# battlecruiser.move("9시")


# 건물
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         super().__init__(name, hp, 0)
#         self.location = location


# 서플라이 디폿: 건물, 1개 건물 = 8 유닛.
# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")


def game_start():
    print("[알림] 새로운 게임을 시작합니다.")


def game_over():
    print("Palyer: gg")
    print("[Player] 님이 게임에서 퇴장하셨습니다.")


# 실제 게임 시작
game_start()

# 마린 3기 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()

# 탱크 2기 생성
t1 = Tank()
t2 = Tank()

# 레이스 1기 생성
w1 = Wraith()

# 유닛 일괄 관리
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전군 이동
for unit in attack_units:
    unit.move("1시")

# 탱크 시즈모드 개발
Tank.seize_developed = True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

# 공격 모드 준비 (마린: 스팀팩, 탱크: 시즈모드, 레이스: 클로킹)
for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()


# 전군 공격
for unit in attack_units:
    unit.attack("1시")

# 전군 피해
for unit in attack_units:
    unit.damaged(randint(5, 21))

# 게임 종료
game_over()
