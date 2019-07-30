# seizure-detection-BornData
### 更新日志
* 2019-7-30  上传数据,分类方法
* 2019-6-5   上传分类方法和测试比较
* 2019-3-4   数据提取模块上传
* 2018-12-29 开始试验,整理数据

### Abstract
  A code package of the classification with Born Seizure Data (5 classes), using various machine learning.
  
  关于波恩大学癫痫数据的特征提取方法,使用多种机器学习方法进行分类

### Author Information 
  Geng Minxing, now studying in The Institute of Microelectronic in Shandong University, major in machine learning and biomedical signal processing.
  
  Email: gengminxing1995@163.com 
  
  **If you have any question in this program, do not hesitate to contact me.**
    
### Database
* A.npz 采集自五位正常的志愿者, 清醒状态睁眼下的脑电信号 (Z)
* B.npz 采集自五位正常的志愿者, 放松状态闭眼下的脑电信号 (O)
* C.npz 采集自癫痫患者的发作间期信号, 采集位置为颅内海马区, 发作对半球 (N)
* D.npz 采集自癫痫患者的发作间期信号, 采集位置为颅内海马区, 发作半球 (F)
* E.npz 采集自癫痫患者的发作信号, 采集自发作区域 (S)

### Mission
1. AB vs CD vs E **三分类 (正常 vs 间期 vs 发作)**
2. ABCD vs E **二分类 (非发作 vs 发作)**
3. AB vs CD **二分类 (正常 vs 间期)**

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