# OLS 회귀 분석 결과 해석

## Sample code
<details>
<summary>Click to toggle contents of `code`</summary>

```python
import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 시드 설정
np.random.seed(0)

# 데이터 생성
n = 100  # 데이터 포인트 수
x1 = np.random.normal(170, 10, n)  # 키 (cm)
x2 = np.random.normal(85, 10, n)   # 허리둘레 (cm)
beta_0 = 50
beta_1 = 0.5
beta_2 = 0.3
epsilon = np.random.normal(0, 5, n)  # 오차

# 몸무게 계산
y = beta_0 + beta_1 * x1 + beta_2 * x2 + epsilon

# 데이터프레임 생성
data = pd.DataFrame({'Height': x1, 'Waist': x2, 'Weight': y})

# 회귀 모델 적합
X = data[['Height', 'Waist']]
X = sm.add_constant(X)  # 상수 항 추가
model = sm.OLS(data['Weight'], X).fit()

# 결과 출력
print(model.summary())

# 회귀 평면 시각화
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# 데이터 포인트
ax.scatter(data['Height'], data['Waist'], data['Weight'], c='blue', marker='o', label='Data')

# 회귀 평면 생성
height_range = np.linspace(data['Height'].min(), data['Height'].max(), 10)
waist_range = np.linspace(data['Waist'].min(), data['Waist'].max(), 10)
height_mesh, waist_mesh = np.meshgrid(height_range, waist_range)
weight_pred = model.predict(sm.add_constant(pd.DataFrame({'Height': height_mesh.ravel(), 'Waist': waist_mesh.ravel()})))
weight_mesh = weight_pred.values.reshape(height_mesh.shape)

# 회귀 평면
ax.plot_surface(height_mesh, waist_mesh, weight_mesh, color='red', alpha=0.5)

ax.set_xlabel('Height')
ax.set_ylabel('Waist')
ax.set_zlabel('Weight')
plt.title('Regression Plane')
plt.legend()
plt.show()

```
</details>

## OLS 회귀 분석 결과
<details>
<summary>Click to toggle contents of `Result`</summary>

```bash
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                 Weight   R-squared:                       0.662
Model:                            OLS   Adj. R-squared:                  0.655
Method:                 Least Squares   F-statistic:                     94.99
Date:                Sat, 20 Jul 2024   Prob (F-statistic):           1.42e-23
Time:                        21:00:48   Log-Likelihood:                -297.51
No. Observations:                 100   AIC:                             601.0
Df Residuals:                      97   BIC:                             608.8
Df Model:                           2                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         42.1042      8.731      4.822      0.000      24.775      59.433
Height         0.5334      0.048     11.099      0.000       0.438       0.629
Waist          0.3221      0.047      6.881      0.000       0.229       0.415
==============================================================================
Omnibus:                        0.808   Durbin-Watson:                   2.386
Prob(Omnibus):                  0.668   Jarque-Bera (JB):                0.362
Skew:                          -0.044   Prob(JB):                        0.834
Kurtosis:                       3.281   Cond. No.                     3.47e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 3.47e+03. This might indicate that there are
strong multicollinearity or other numerical problems.

```
</details>

## 모델 적합도 (Model Fit)
- **R-squared**: 0.662  
  - **해석**: 설명변수들이 반응변수의 변동성을 설명하는 비율입니다. 66.2%의 변동성이 설명변수들로 설명됩니다. 이는 모델이 상당한 예측력을 가지고 있음을 의미합니다.

- **Adj. R-squared**: 0.655  
  - **해석**: 조정된 결정계수는 모델의 설명력이 얼마나 일반화되었는지를 보여줍니다. 설명변수가 많아지면 자연스럽게 R-squared가 증가할 수 있기 때문에, 이를 보정하여 모델의 실제 설명력을 평가합니다. 조정된 R-squared가 0.655는 모델이 설명변수들을 적절히 사용하고 있음을 나타냅니다.

- **F-statistic**: 94.99  
  - **해석**: 모델 전체의 유의성을 검정합니다. F-statistic이 크면 설명변수들이 모델에 유의미하게 기여하고 있음을 의미합니다.

- **Prob (F-statistic)**: 1.42e-23  
  - **해석**: F-statistic의 p-값이 매우 작으므로, 모델이 유의미하다는 것을 나타냅니다. 모델이 우연에 의한 것이 아니라 실제로 유의미한 예측력을 가지고 있다고 결론지을 수 있습니다.

## 회귀계수 (Regression Coefficients)
- **const (Intercept)**: 42.1042  
  - **해석**: 모든 설명변수가 0일 때, 몸무게의 예상 값은 42.1042입니다. 이 값은 실제 상황에서는 해석이 어려울 수 있지만, 이론적 기준점으로 이해할 수 있습니다.

- **Height**: 0.5334  
  - **해석**: 키가 1cm 증가할 때, 몸무게는 평균적으로 0.5334kg 증가한다고 해석합니다. 이 계수는 키와 몸무게 사이의 관계를 나타냅니다.

- **Waist**: 0.3221  
  - **해석**: 허리둘레가 1cm 증가할 때, 몸무게는 평균적으로 0.3221kg 증가한다고 해석합니다. 이 계수는 허리둘레와 몸무게 사이의 관계를 나타냅니다.

## 통계적 유의성 (Statistical Significance)
- **t-값 (t)** 및 **p-값 (P>|t|)**  
  - **const**: t=4.822, p<0.001  
  - **Height**: t=11.099, p<0.001  
  - **Waist**: t=6.881, p<0.001  
  - **해석**: 각 변수의 p-값이 0.05 이하이므로, 각 설명변수가 통계적으로 유의미하다고 판단할 수 있습니다. 즉, 키와 허리둘레는 몸무게에 유의미한 영향을 미친다고 볼 수 있습니다.

## 모델 진단 (Model Diagnostics)
- **Omnibus**: 0.808, **Prob(Omnibus)**: 0.668  
  - **해석**: 잔차의 정규성을 검정합니다. p-값이 0.05보다 크므로 잔차가 정규 분포를 따른다는 가정을 기각할 수 없습니다.

- **Durbin-Watson**: 2.386  
  - **해석**: 잔차의 자기상관을 검정합니다. 값이 2에 가까우면 자기상관이 없다는 의미입니다. 이 경우 값이 2.386으로, 잔차 간 자기상관이 없음을 나타냅니다.

- **Jarque-Bera (JB)**: 0.362, **Prob(JB)**: 0.834  
  - **해석**: 잔차의 왜도 및 첨도를 검정합니다. p-값이 0.05보다 크므로 잔차가 정규 분포를 따른다는 가정을 기각할 수 없습니다.

- **Condition Number**: 3.47e+03  
  - **해석**: 수치적 안정성을 평가합니다. 값이 크면 다중공선성(설명변수들 간의 높은 상관관계) 문제가 있을 수 있음을 시사합니다.

## 결론
- **모델의 적합도**: 설명변수들이 반응변수의 변동성을 상당히 잘 설명합니다 (R-squared = 0.662).
- **편회귀계수**: 키와 허리둘레가 몸무게에 미치는 영향을 각각 0.5334kg/cm, 0.3221kg/cm로 추정합니다.
- **유의성**: 모든 변수의 p-값이 0.05보다 작아 통계적으로 유의미합니다.
- **모델 진단**: 잔차는 정규성을 띠며 자기상관이 없지만, 높은 조건 번호는 다중공선성 문제의 가능성을 시사합니다.

이러한 분석을 통해 모델의 적합성과 변수의 중요성을 평가하고, 실제 데이터에 대한 예측력을 이해할 수 있습니다.
