import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binomtest, binom
import seaborn as sns

sns.set()

# 동전 던지기 시행 횟수(N)와 앞면이 나온 횟수(m)
N = 100
m = 60

# 귀무 가설: 동전의 앞면이 나올 확률은 0.5로 기대된다.
p_expected = 0.5

# 이항 검정 수행
p_value = binomtest(m, N, p_expected, alternative='two-sided')
p_value = p_value.pvalue

# 시각화
fig, ax = plt.subplots(figsize=(8, 6))

# 이항 분포 확률 질량 함수를 그래프로 표시
x = np.arange(0, N+1)
y = [binom.pmf(i, N, p_expected) for i in x]
ax.plot(x, y, label=f'Binomial Distribution (p={p_expected})', marker='o', linestyle='-', color='blue')

# 검정 결과를 표시하기 위해 수직선 그리기
ax.axvline(x=m, color='red', linestyle='--', label=f'Observed Heads: {m}')
ax.axhline(y=0, color='black', linewidth=0.5)
ax.set_xlabel('Number of Heads')
ax.set_ylabel('Probability Density')
ax.set_title(f'Binomial Test (N={N}, m={m}), p-value: {p_value:.4f}')
ax.legend()

plt.grid(True)
plt.show()

# 검정 결과 출력
alpha = 0.05
if p_value < alpha:
    print(f'유의수준 {alpha:.2f}에서 귀무가설을 기각합니다: 앞면이 나올 확률은 {p_expected}가 아닙니다.')
else:
    print(f'유의수준 {alpha:.2f}에서 귀무가설을 기각하지 않습니다: 앞면이 나올 확률은 {p_expected}와 유사합니다.')
