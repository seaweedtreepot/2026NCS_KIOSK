import numpy as np
scores = np.array([
    #국영수
    [80,100,90],#A학생
    [100,86,66],#B
    [33,54,77] #C
])

print(f"전체평균 {np.mean(scores)}")

#국어 평균
#=> 이걸위해 열(축:axis)연산을 함

print(f"국 영 수 과목별 평균: {np.mean(scores,axis=0)}")
print(f"학생별 최고점수: {np.max(scores,axis=1)}")