import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 1에서 10 사이의 무작위 정수 1000개 생성
data = np.random.randint(1, 1000, size=1000)

# 상자수염 그림과 스웜 플롯 함께 그리기
plt.figure(figsize=(8, 6))
sns.boxplot(data=data, color='lightblue', width=0.3)
sns.swarmplot(data=data, color='orange', alpha=0.7)

# 최솟값, 최댓값, 사분위수 계산
min_val = np.min(data)
max_val = np.max(data)
q1, q2, q3 = np.percentile(data, [25, 50, 75])

# 최솟값, 최댓값, 사분위수 텍스트로 추가
plt.text(0.1, min_val, f'Min: {min_val}', ha='left', va='center', color='blue', fontsize=10)
plt.text(0.1, max_val, f'Max: {max_val}', ha='left', va='center', color='blue', fontsize=10)
plt.text(0.1, q1, f'Q1: {q1}', ha='left', va='center', color='red', fontsize=10)
plt.text(0.1, q2, f'Median: {q2}', ha='left', va='center', color='red', fontsize=10)
plt.text(0.1, q3, f'Q3: {q3}', ha='left', va='center', color='red', fontsize=10)

# 그래프 제목 추가
plt.title('Boxplot with Swarmplot of 1000 Random Numbers between 1 and 1000')
plt.tight_layout()
plt.show()
