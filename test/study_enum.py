from  enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov,Dec'))

print(Month.Jan.value)
print(Month.Jan)

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

from enum import Enum, unique


@unique
class weekday(Enum):
    # sun = 0
    mon = 1
    tue = 2
    wed = 3
    thu = 4
    fri = 5
    sat = 6
    leo = 0


day1 = weekday.leo
print(day1)
print(weekday['thu'])
print(weekday.thu.value)
print(weekday(1))
for name, member in weekday.__members__.items():
    print(name, '=>', member, ',', member.value)
