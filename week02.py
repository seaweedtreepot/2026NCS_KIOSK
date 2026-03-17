# data = [10,20,30,40]
# hap, count = 0, 0

# for i in data:
#     hap += i
#     count += 1 //기초적인 버전

# print(hap, count)
# print(hap/count)
data = 0
data = [10,20,30,40]
# hap, count = 0, 0

# average = sum(data) / len(data)
# print(average) 빌트인 함수 적용해서 아주 효율적

import statistics
print(statistics.mean(data)) #가독성 좋음

# 집가고 싶은 마음
aura = 0
aura += 999999999
print(aura)