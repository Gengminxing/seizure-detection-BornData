# seizure-detection-BornData
### Abstract
  A code package of the classification with Born Seizure Data (5 classes), using various machine learning.
  
  关于波恩大学癫痫数据的特征提取方法,使用多种机器学习方法进行分类

### Database
* A.npz 采集自五位正常的志愿者, 清醒状态睁眼下的脑电信号 (Z)
* B.npz 采集自五位正常的志愿者, 放松状态闭眼下的脑电信号 (O)
* C.npz 采集自癫痫患者的发作间期信号, 采集位置为颅内海马区, 发作对半球 (N)
* D.npz 采集自癫痫患者的发作间期信号, 采集位置为颅内海马区, 发作半球 (F)
* E.npz 采集自癫痫患者的发作信号, 采集自发作区域

### Mission
1. AB vs CD vs E *三分类* (正常 vs 间期 vs 发作)
2. ABCD vs E *二分类* (非发作 vs 发作)
3. AB vs CD *二分类* (正常 vs 间期) 

### Feature Extraction Method
* 功率谱密度
* 时频统计特征 (Mean / Std / Skewness / Kurtosis)
* 小波系数的统计特征
* 短时傅里叶变换 + 奇异值分解 (STFT + SVD)

### Classifier
* SVM
* Logistic Regerssion
* Random Forest
* Xgboost

### References
* [我的机器学习之旅](https://blog.csdn.net/AndrewMX/article/details/94444188)
* [主成分分析的实现(Python源代码)](https://blog.csdn.net/AndrewMX/article/details/94161223)