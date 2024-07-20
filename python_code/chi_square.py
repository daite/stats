#카이제곱 통계량이 critical region 내에 위치하면 유의수준에서 귀무 가설을 기각하고, 그 반대의 경우 기각하지 않는 결론을 내릴 수 있습니다.

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

# 주사위 눈의 각 빈도
observed = np.array([5, 8, 10, 20, 7, 10])

# 기대되는 빈도: 모든 눈의 빈도가 동일할 경우
expected = np.ones(6) * np.sum(observed) / 6

# 카이제곱 검정 수행
chi2_stat, p_value = stats.chisquare(observed, f_exp=expected)

# 카이제곱 분포의 확률 밀도 함수를 그래프로 표시
df = len(observed) - 1  # 자유도
x = np.linspace(0, 20, 1000)
y = stats.chi2.pdf(x, df)

# 시각화
fig, ax = plt.subplots(figsize=(10, 6))

# 카이제곱 분포 그래프
ax.plot(x, y, 'b-', label=f'Chi-square Distribution (df={df})')

# 카이제곱 통계량 위치 표시
ax.axvline(x=chi2_stat, color='red', linestyle='--', label=f'Chi-square Statistic: {chi2_stat:.2f}')

# 카이제곱 분포의 치우침(유의수준) 표시
alpha = 0.05
chi2_critical = stats.chi2.ppf(1 - alpha, df)
ax.fill_between(x, 0, y, where=(x >= chi2_critical), color='red', alpha=0.3, label=f'Critical Region (alpha={alpha})')

# 축 및 레이블 설정
ax.set_xlim(0, 20)
ax.set_xlabel('Chi-square Value')
ax.set_ylabel('Probability Density')
ax.set_title(f'Chi-square Test: p-value={p_value:.4f}')
ax.legend()

plt.grid(True)
plt.show()

# 유의성 검정
if p_value < alpha:
    print(f"유의수준 {alpha:.2f}에서 귀무가설을 기각합니다: 주사위의 각 눈의 확률은 동일하지 않습니다.")
else:
    print(f"유의수준 {alpha:.2f}에서 귀무가설을 기각하지 않습니다: 주사위의 각 눈의 확률은 동일합니다.")
