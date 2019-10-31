#### Fisher判别分析

- 最基本的监督线性降维方法
- 使相同类别的样本尽量靠近
- 不同类别的样本尽量远离


$$
\begin{align*}
S^{{w}} &= \sum_{y=1}^c \sum_{i:y_i=y}(\boldsymbol{x_i-\mu_y})(\boldsymbol{x_i-\mu_y})^\top 
\in \R^{d\times d}
\\
S^{(b)} &= \sum_{y=1}^c n_y \boldsymbol{\mu_y \mu_y^\top} \in \R^{d \times d} 
\end{align*}
$$

$$
\boldsymbol{\mu_y} = \frac{1}{n_y}\sum_{i:y_i=y}\boldsymbol{x}_i
$$

$$
\max_{T\in \R^{m \times d}} \mathrm{tr}\left( (TS^{(w)} T^\top)^{-1}(TS^{(b)}T^\top) \right)
$$

$$
S^{(b)}\xi = \lambda S^{(w)} \xi \\
\hat{T} = (\xi_1, \cdots, \xi_m)^\top
$$

#### 局部Fisher判别分析

$$
S^{(w)} = \frac{1}{2}\sum_{i:i'=1}^n Q_{i:i'}^{w}(\boldsymbol{x}_i-\boldsymbol{x}_{i'})(\boldsymbol{x}_i-\boldsymbol{x}_{i'})^\top 
\\
S^{(b)} = \frac{1}{2}\sum_{i:i'=1}^n Q_{i:i'}^{b}(\boldsymbol{x}_i-\boldsymbol{x}_{i'})(\boldsymbol{x}_i-\boldsymbol{x}_{i'})^\top
$$

$$
\begin{align*}
&
Q_{i:i'}^{(w)} = 
\begin{cases}
\frac{1}{n_y} & (y_i = y_{i'}=y)\\
0							& (y_i \ne y_{i'})
\end{cases} \\
&
Q_{i:i'}^{(b)} = 
\begin{cases}
\frac{1}{n} - \frac{1}{n_y} & (y_i = y_{i'}=y)\\
\frac{1}{n} 							& (y_i \ne y_{i'})
\end{cases}
\end{align*}
$$

------

$$
S^{(lw)} = \frac{1}{2}\sum_{i:i'=1}^n Q_{i:i'}^{lw}(\boldsymbol{x}_i-\boldsymbol{x}_{i'})(\boldsymbol{x}_i-\boldsymbol{x}_{i'})^\top 
\\
S^{(lb)} = \frac{1}{2}\sum_{i:i'=1}^n Q_{i:i'}^{lb}(\boldsymbol{x}_i-\boldsymbol{x}_{i'})(\boldsymbol{x}_i-\boldsymbol{x}_{i'})^\top
$$

$$
\begin{align*}
&
Q_{i:i'}^{(w)} = 
\begin{cases}
\frac{W_{i,i'}}{n_y} & (y_i = y_{i'}=y)\\
0							& (y_i \ne y_{i'})
\end{cases} \\
&
Q_{i:i'}^{(b)} = 
\begin{cases}
W_{i,i'} (\frac{1}{n} - \frac{1}{n_y}) & (y_i = y_{i'}=y)\\
\frac{1}{n} 							& (y_i \ne y_{i'})
\end{cases}
\end{align*}
$$

$$
\max_{T\in \R^{m \times d}} \mathrm{tr}\left( (TS^{(lw)} T^\top)^{-1}(TS^{(lb)}T^\top) \right)
$$

$$
S^{(lb)}\xi = \lambda S^{(lw)} \xi \\
\hat{T} = (\xi_1, \cdots, \xi_m)^\top
$$

------

$$
S^{(t)} = 
$$

