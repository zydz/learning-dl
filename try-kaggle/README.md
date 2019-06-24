[Kaggle大神经验分享丨如何用15个月冲到排行榜的首位](https://baijiahao.baidu.com/s?id=1625877833345139745&wfr=spider&for=pc)

TODO:
Use shell-script or python-function get datasets

Inspirition
按照字母表记忆单词的方法，也可以用在总结kaggle的常用调用。





## 机器学习算法

> 常用算法选择

[![img](https://github.com/apachecn/kaggle/raw/master/static/images/docs/kaggle-%E5%B8%B8%E7%94%A8%E7%AE%97%E6%B3%95%E9%80%89%E6%8B%A9.png)](https://github.com/apachecn/kaggle/blob/master/static/images/docs/kaggle-常用算法选择.png)

> 常用工具选择

[![img](https://github.com/apachecn/kaggle/raw/master/static/images/docs/kaggle-%E5%B8%B8%E7%94%A8%E5%B7%A5%E5%85%B7%E9%80%89%E6%8B%A9.png)](https://github.com/apachecn/kaggle/blob/master/static/images/docs/kaggle-常用工具选择.png)

> 解决问题的流程

1. 链接场景和目标
2. 链接评估准则
3. 认识数据
4. 数据预处理（清洗、调权）
5. 特征工程
6. 模型调参
7. 模型状态分析
8. 模型融合

> 数据预处理

- 数据清洗
  - 去掉样本数据的异常数据。（比如连续型数据中的离群点）
  - 去除缺失大量特征的数据
- 数据采样
  - 下/上采样（假设正负样本比例1:100，把正样本的数量重复100次，这就叫上采样，也就是把比例小的样本放大。下采样同理，把比例大的数据抽取一部分，从而使比例变得接近于1；1）
  - 保证样本均衡
- 工具 sql、pandas等

> 特征工程

[![img](https://github.com/apachecn/kaggle/raw/master/static/images/docs/kaggle-%E7%89%B9%E5%BE%81%E5%B7%A5%E7%A8%8B.png)](https://github.com/apachecn/kaggle/blob/master/static/images/docs/kaggle-特征工程.png)

> 特征处理

- 数值型：连续型数据离散化或者归一化、数据变化（log、指数、box-cox）
- 类别型：做编码，eg：one-hot编码，如果类别数据有缺失，把缺失也作为一个类别即可。
- 时间类：间隔化（距离某个节日多少天）、与其他特征（eg：次数）融合，变成一周登陆几次、离散化（eg：外卖，把时间分为【饭店、非饭店】）
- 文本类：N-gram、Bag-of-words、TF-IDF
- 统计型：与业务强关联
- 组合特征


## BLOG
[Approaching (Almost) Any Machine Learning Problem | Abhishek Thakur](http://blog.kaggle.com/2016/07/21/approaching-almost-any-machine-learning-problem-abhishek-thakur/)
[为什么Kaggle数据分析竞赛者偏爱XGBoost](https://yq.aliyun.com/articles/70770)

[1st PLACE - WINNER SOLUTION - Gilberto Titericz & Stanislav Semenov](https://www.kaggle.com/c/otto-group-product-classification-challenge/discussion/14335)

