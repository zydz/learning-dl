$$
B = Z^TZ \\

\begin{align*}
dist_{ij}^2 &= \|z_i\|^2 + \|z_j\|^2 -2z_i^Tz_j \\
&= b_{ij} + b_{jj} -2 b_{ij}
\end{align*}
$$

------

$$
\sum_{i+1}^m z_i = 0 \\
\sum_{i=1}^m b_{ij} = \sum_{j=1}^m b_{ij} = 0 \\
\sum_{i=1}^m dist_{ij}^2 = tr({B}) + m b_{jj} \\
\sum_{j=1}^m dist_{ij}^2 = tr({B}) + m b_{ii} \\
\sum_{i=1}^m \sum_{j=1}^m dist_{ij}^2 = 2m\: tr(B) \\
tr(B) = \sum_{i=1} ^m\|z_i\|
$$

$$
\forall \boldsymbol{x} \in X=\{\boldsymbol{x^{(1)},x^{(2)}, \cdots, x^{(m)}} \}, X \in \mathbb{R}^{d \times m} \\
\vec{x^{(i)}} = \{ x_1, x_2, \cdots, x_d \} ^{(i)} \\
\begin{align*}
& 数据空间： & X \in \mathbb{R}^{d \times m} \\
& 距离矩阵： & D \in \mathbb{R}^{m \times m}  \\
& 降维数据： & Z \in \mathbb{R}^{d' \times m}  \\
& 降维数据内积空间： &B = Z^TZ \\
& B的特征值矩阵、特征向量矩阵： &\Lambda, V 
\end{align*}
$$


$$
中心化：
\begin{cases}
dist_{i.}^2 = \frac{1}{m} \sum_{j=1}^m dist_{ij}^m \\
dist_{.j}^2 = \frac{1}{m} \sum_{i=1}^m dist_{ij}^m \\
dist_{ij}^2 = \frac{1}{m^2} \sum_{i=1}^m \sum_{j=1}^m dist_{ij}^m
\end{cases} \\
\Rightarrow b_{ij} = -\frac{1}{2}(dist_{ij}^2 -dist_{i.}^2 -dist_{.j}^2 + dist_{..}^2)
$$

$$
B = V\Lambda V^T, which \; \Lambda = diag(\lambda_1,\lambda_2,\cdots, \lambda_d) \\
Z = \tilde{\Lambda}_*^{\frac{1}{2}}\tilde{V}^T \in \mathbb{R}^{d^*\times m} \\
Z = \Lambda_*^{\frac{1}{2}}V^T \in \mathbb{R}^{d'\times m}
$$
