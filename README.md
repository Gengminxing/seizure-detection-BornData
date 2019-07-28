# seizure-detection-BornData
### Abstract
  A code package of the classification with Born Seizure Data (5 classes), using various machine learning.
  
  关于波恩大学癫痫数据的特征提取方法,使用多种机器学习方法进行分类

### Feature Extraction Method
* 功率谱密度
* 时频统计特征 (Mean / Std / Skewness / Kurtosis)
* 小波系数的统计特征
* 短时傅里叶变换 + 奇异值分解 (STFT + SVD)

### Classification
* SVM
* Logistic Regerssion
* Random Forest
* Xgboost

### References
* [我的机器学习之旅](https://blog.csdn.net/AndrewMX/article/details/94444188)
* [主成分分析的实现(Python源代码)](https://blog.csdn.net/AndrewMX/article/details/94161223)