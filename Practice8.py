# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):  # __init__ : 생성자, #self는 항상 적어야하고, 자기 자신의 변수에 접근이 가능
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print(f"{self.name} : {location} 방향으로 이동합니다. [속도 {self.speed}]")

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

    def damaged(self, damage):
        print(f"{self.name} : {damage} 데미지를 입었습니다.")
        self.hp -= damage
        print(f"{self.name}: 현재 체력은 {self.hp} 입니다.")
        if self.hp <= 0:
            print(f"{self.name} 이 파괴되었습니다.")

# 드랍쉽: 공즁 유닛 = 수송기. 마린 / 파이어뱃 / 탱크 등을 수송. 공격X

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
        print("[공중 유닛 이동]")
        self.fly(self.name, location)


# 발키리: 공중 공격 유닛, 한번에 14발 미사일 발사
# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")

# 벌쳐: 지상유닛, 기동성이 좋음
vulture = AttcakUnit("벌쳐", 80, 10, 20)

# 배틀크루저: 공중유닛, 체력 굉장히 좋음, 공격력도 굿.
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
# battlecruiser.fly(battlecruiser.name, "9시")
battlecruiser.move("9시")

# 건물


class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        super().__init__(name, hp, 0)
        self.location = location


# 서플라이 디폿: 건물, 1개 건물 = 8 유닛.
# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")


# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")


# def game_over():
#     pass


# game_start()
# game_over()
