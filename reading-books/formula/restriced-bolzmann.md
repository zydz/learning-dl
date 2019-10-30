受限波尔兹曼机 = 波尔兹曼机+“层内单元之间无连接”
$$
E(v, h, \theta) = 
-\sum_{i=1}^n b_i v_i - \sum_{j=1}^m c_j h_j
-\sum_{i=1}^n\sum_{j=1}^m w_{ij}v_i h_j
$$

$$
\begin{align*}
\log L(\theta|v) &= \log{\frac{1}{Z}}\sum_h\exp\{-E(v,h,\theta)\}
\\
& = \log\sum_n\exp\{ -E(v,h,\theta) \}-
\log \sum_{v,h}\exp\{-E(v,h,\theta) \}

\end{align*}
$$

$$
\nabla \left( \log L(\theta|v)\right)= 
\begin{pmatrix}
\frac{\partial{\log L(\theta|v)} }{\partial \theta}
\\
\frac{\partial{\log L(\theta|v)} }{\partial w_{ij}}
\\
\frac{\partial{\log L(\theta|v)} }{\partial b_i}
\\
\frac{\partial{\log L(\theta|v)} }{\partial c_j}
\end{pmatrix}

=
\begin{pmatrix}
-\sum_h p(v|h)\frac{\partial E(v,h,\theta)}{\theta}+
\sum_{v,h}p(v,h)\frac{\partial E(v,h,\theta)}{\theta}
\\
p(H_j=1|v)v_i - \sum_v p(v)p(Hj=1|v)vi
\\
v_i - \sum_vp(v)v_i
\\
p(H_j=1|v)-\sum_vp(v)p(H_j=1|v)
\end{pmatrix}
$$

$$
\begin{align*}
w_{ij} & \leftarrow w_{ij} - \frac{\partial{\log L(\theta|v)} }{\partial w_{ij}}
\\
b_i & \leftarrow b_i - \frac{\partial{\log L(\theta|v)} }{\partial b_i}
\\
c_j & \leftarrow c_j - \frac{\partial{\log L(\theta|v)} }{\partial c_j}
\end{align*}
$$
