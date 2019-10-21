$$
R(c_i | \boldsymbol{x}) = \sum _{j=1} ^N \lambda_{ij}P({c_j | \boldsymbol{x}}) \\
\mathcal{X}: \{\boldsymbol{x}_1,\boldsymbol{x}_2,\cdots, \boldsymbol{x}_m\},  \\
\mathcal{Y}: \{c_1, c_2,\cdots, c_N\}, \\
h: \mathcal{X} \to \mathcal{Y} \\
R(h) = \mathbb{E}_\boldsymbol{x}[R(h(\boldsymbol{x}) | \boldsymbol{x})] \\
\begin{align*}
h^*(\boldsymbol{x}) &= \arg \min_{ c \in \mathcal{Y}}R(c|\boldsymbol{x}) \\
\end{align*}
$$

-----

$$
\lambda _{ij} = 
\begin {cases}
0 , if \:    i=j;\\
1 , otherwise
\end{cases} \\

R(c|\boldsymbol{x}) = 1 - P(c|\boldsymbol{x} ) \\
h^* = \arg \max _{c \in \mathcal{Y}} P(c|\boldsymbol{x})
$$

----

$$
P(D_c|\boldsymbol{\theta}_c) = \prod _{x \in D_c} P(\boldsymbol{x} | \boldsymbol{\theta}_c) \\
LL(\boldsymbol{\theta}_c) = \log P(D_c| \boldsymbol{\theta}_c) \\
= \sum _{\boldsymbol{x} \in D_c} \log P(\boldsymbol{x}| \boldsymbol{\theta}_c) \\
\hat{\boldsymbol{\theta}} _c  = \arg \max_{\boldsymbol{\theta}_c} LL(\boldsymbol{\theta}_c)
$$

----

$$
h_{nb} (\boldsymbol{x} ) = \arg \max _{c \in \mathcal{Y}} P(c) \prod _{i=1} ^d {P(x_i | c)}
$$

