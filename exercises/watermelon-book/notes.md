# 第7章 贝叶斯分类

## 贝叶斯决策论

### 问题空间

- $x \in  \mathcal{X} \in \R^d$  输入、样本**特征**空间

- $c \in \mathcal{Y}$  输出、分类空间



### 解释

$$
P(c|\boldsymbol{x}) = \frac{P(c)P(\boldsymbol{x}|c)}{P(\boldsymbol{x})} \\
$$

估计$P(c|\boldsymbol{x})$转化成了如何训练数据D来估计先验概率$P(c)$和似然$P(\boldsymbol{x}|c)$

- $P(c)$可以由大数定律得到

- $P(\boldsymbol x|c)$可能有困难，因为它涉及到x所有属性的联合概率

$$
%\begin{equation}
%\begin{split}
P(\boldsymbol x|c) \\
= P(X=\boldsymbol x|Y=c) \\
= P(X^{(1)}=x^{(1)}, \cdots, X^{(n)}=x^{(n)}| Y=c)
%\end{split}
%\end{equation}
$$

## 极大似然估计

估计条件概率的一种常见策略：

先假定其具有某种确定的概率分布形式，再基于样本对概率分布的参数进行估计。

概率模型的训练过程就是**参数估计**过程。

- 频率主义学派

- 贝叶斯学派

## 朴素贝叶斯分类器

朴素贝叶斯分类器采用了**属性条件独立性假设**。即： 每个属性独立地对分类结果发生影响。

$$
P(c|\boldsymbol{x}) = \frac{P(c)P(\boldsymbol x|c)}{P(\boldsymbol{x})} = 
\frac{P(c)}{P(\boldsymbol x)} \prod_{i=1}^mP(x_i|c)
$$

## 半朴素贝叶斯分类器

## 贝叶斯网

贝叶斯网也称为**信念网**(belief network)，它借助**有向无环图**来刻画属性之间的依赖关系，并使用**条件概率表**来描述属性的联合概率分布。



## EM算法


