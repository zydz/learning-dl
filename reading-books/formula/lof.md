### 局部异常因子

$$
{RD}_k(\boldsymbol{x},\boldsymbol{x'}) = \max\{\|x-x^{(k)}\|, \|x-x' \|\}
$$

$$
{LRD}_k(x) = \left( \frac{1}{k} \sum_{i=1}^k {RD}_k(x^{(i)}, x) \right)^{-1}
$$

$$
LOF(x) =  \frac{\frac{1}{k} \sum_{j=1}^k {LRD}_k(x^{(j)}) }
{{LRD}_k(\boldsymbol{x})}
$$

### 支持向量机的异常检验

$$
\min_{c,R,\xi} \left[ R^2 + C\sum_{i=1}^n \xi_i\right], \\
s.t.\: 
\|\boldsymbol{x}_i-\boldsymbol{c}\|^2 \le R^2+\xi_i, \xi_i \ge 0, 
for \: i=1,\cdots,n
$$

$$
L(\boldsymbol{c}, R, \boldsymbol{\xi}, \boldsymbol{\alpha},\boldsymbol{\beta})
= R^2+C\sum_{i=1}^n\xi_i -\sum_{i=1}^n\alpha_i\left(R^2+\xi_i-\|x_i-c\|^2 \right) -\sum_{i=1}^n {\beta_i\xi_i}
$$

$$
\begin{align*}
& 
\frac {\partial{L}}{\partial{\boldsymbol{c}}}= 0 
\Rightarrow 
\boldsymbol{c} = \frac{\sum_{i=1}^n \alpha_i\boldsymbol{x}_i }{\sum_{i=1}^n \alpha_i} 
\\
&
\frac {\partial{L}}{\partial{R}}= 0 
\Rightarrow
\sum_{i=1}^n\alpha_i = 1
\\
&
\frac {\partial{L}}{\xi_i}= 0 
\Rightarrow
\alpha_i + \beta_i = C, \forall i = 1,\cdots,n

\\
\end{align*}
$$

$$
\widehat{\boldsymbol{\alpha}} = \mathop{\arg\max}_\boldsymbol{\alpha} 
\left[ \sum_{i=1}^n \alpha_i\boldsymbol{x}_i^T\boldsymbol{x}_i 
- \sum_{i=1}^n\sum_{j=1}^n \alpha_i\alpha_j\boldsymbol{x}_i^T\boldsymbol{x}_i 
\right] \\
s.t. 0\le\alpha_i\le C, for \: i=1,\cdots,n.
$$

$$
\widehat{R}^2 = \left \|\boldsymbol{x}_i - \sum_{j=1}^n\widehat{\alpha}_j\boldsymbol{x}_j\right \|^2 \\
\widehat{\boldsymbol{c}} = \sum_{i=1}^n\widehat{\alpha}_i\boldsymbol{x}_i 
\\
\boldsymbol{x}
\\
$$

如果$\boldsymbol{x}$满足下面条件就是异常值
$$
\|\boldsymbol{x}-\widehat{\boldsymbol{c}}\|^2 \gt \widehat{R}^2
$$




### 基于密度比的异常检验

$$
w(\boldsymbol{x}) = \frac{p'(\boldsymbol{x})}{p(\boldsymbol{x})}
$$

**KL散度密度比估计法**
$$
w_{\alpha}(\boldsymbol{x}) = \sum_{j=1}^b \alpha_j \psi_j(\boldsymbol{x}) = 
\boldsymbol{\alpha}^\top \boldsymbol{\psi}(\boldsymbol{x})
$$

$$
w_\alpha(\boldsymbol{x})p(\boldsymbol{x})和p'(\boldsymbol{x})的相似度称为KL距离：\\
KL(p'\|w_\alpha P) = \int p'(\boldsymbol{x}) \log \frac{p'(\boldsymbol{x})}{w_\alpha(\boldsymbol{x})p(\boldsymbol{x})} \mathrm{d}x
$$


$$
s.t. \:
\int w_\alpha(\boldsymbol{x})p(\boldsymbol{x})dx = 1, \forall\boldsymbol{x},w_\alpha(\boldsymbol{x})p(\boldsymbol{x}) \ge 0
$$

$$
\max_\alpha \frac{1}{n'}\sum_{i'=1}^{n'}\log w_\alpha(x'_{i'}),\\
s.t. \frac{1}{n}\sum_{i=1}^nw_\alpha(\boldsymbol{x}_i) = 1, \alpha_i, \cdots, \alpha_{n'} \ge 0
$$



高斯核函数模型：
$$
w_{\alpha}(\boldsymbol{x}) = \sum_{j=1}^{n'}\alpha_j \exp\left( -\frac{\|x-x'_j\|^2}{2\kappa^2}
\right)
$$
