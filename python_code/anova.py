import numpy as np
import pandas as pd
from scipy.stats import f_oneway, f
import matplotlib.pyplot as plt
import seaborn as sns

# Seaborn 초기화
sns.set()

# 데이터 정의
fertilizer_a = [32.5, 34.2, 32.4, 33.3, 31.0, 31.5]
fertilizer_b = [35.1, 32.9, 34.4, 34.7, 33.0, 34.2]
fertilizer_c = [40.1, 39.6, 38.0, 38.1, 37.9, 38.9]

# 데이터를 DataFrame으로 변환
data = pd.DataFrame({
    'Fertilizer': np.repeat(['A', 'B', 'C'], 6),
    'StemLength': np.concatenate([fertilizer_a, fertilizer_b, fertilizer_c])
})

# Perform ANOVA
f_statistic, p_value = f_oneway(fertilizer_a, fertilizer_b, fertilizer_c)

# 시각화 설정
plt.figure(figsize=(12, 6))

# Boxplot과 Swarm plot 그리기 (왼쪽)
plt.subplot(1, 2, 1)
sns.boxplot(x='Fertilizer', y='StemLength', data=data)
sns.swarmplot(x='Fertilizer', y='StemLength', data=data, color='black', alpha=0.5)
plt.title('Stem Length by Fertilizer Type')
plt.xlabel('Fertilizer Type')
plt.ylabel('Stem Length')

# F-distribution plot 그리기 (오른쪽)
plt.subplot(1, 2, 2)
df_between = len(data['Fertilizer'].unique()) - 1
df_within = len(data) - len(data['Fertilizer'].unique())
x = np.linspace(0, 5, 500)
y = f.pdf(x, df_between, df_within)
plt.plot(x, y, label='F-distribution')
plt.axvline(x=f_statistic, color='red', linestyle='--', label=f'F-value: {f_statistic:.2f}')
plt.fill_between(x, 0, y, where=(x >= f_statistic), color='red', alpha=0.3)
plt.title('F-distribution')
plt.xlabel('F-value')
plt.ylabel('Density')
plt.legend()

# 그래프 레이아웃 조정 및 표시
plt.tight_layout()
plt.show()

# 출력 p-value 및 귀무가설 판정
alpha = 0.05

print(f'F-statistic: {f_statistic:.4f}')
print(f'p-value: {p_value:.4f}')

if p_value < alpha:
    print('\n귀무가설을 기각합니다: 적어도 하나의 비료 유형의 평균이 다릅니다.')
else:
    print('\n귀무가설을 기각하지 않습니다: 비료 유형 간의 평균 차이는 통계적으로 유의미하지 않습니다.')
