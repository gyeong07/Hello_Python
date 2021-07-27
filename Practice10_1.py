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
import inspect
import random
from travel import *
print(inspect.getfile(random))
print(inspect.getfile(thailand))
