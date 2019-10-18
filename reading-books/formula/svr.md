$$
\min_{\boldsymbol{w},b} \frac{1}{2}\|\boldsymbol{w}\|^2 + C \sum_{i=1}^{m}\ell_{\epsilon}(f(x_i)-y_i)
$$

$$
\ell_{\epsilon}(z) = 
\begin{cases}
\begin{align*}
& 0, &if \: |z| \le \epsilon; \\
&|z| - \epsilon , &otherwise.
\end{align*}
\end{cases}
$$

$$
\min_{\boldsymbol{w},b,\xi_i,\hat{\xi}_i} \frac{1}{2} \|\boldsymbol{w} \|^2 + C \sum_{i=1}^{m}(\xi_i+\hat{\xi}_i) \\
s.t.
\begin{cases}
& f(\boldsymbol{x}_i) -y_i \le \epsilon + \xi_i ,\\
& y_i -f(\boldsymbol{x}_i) \le \epsilon + \hat{\xi}_i,  \\
& \xi_i \ge 0, \hat{\xi}_i \ge 0, i = 1,2,\cdots, m.
\end{cases}
$$

$$
\begin{align*}
& L(\boldsymbol{w},b,\boldsymbol{\alpha,\hat{\alpha},\xi,\hat{\xi},\mu,\hat{\mu}}) \\
& = \frac{1}{2}\| \boldsymbol{w}\| +C \sum_{i=1}^m{(\xi_i+ \hat{\xi}_i)} - \sum_{i=1}^m\mu_i\xi_i - \sum_{i=1}^m\hat{\mu}_i\hat{\xi}_i  \\
& + \sum_{i=1}^m \alpha_i\left(f(\boldsymbol{x}_i)- y_i - \epsilon - \xi_i\right) +\sum_{i=1}^m \hat{\alpha}_i\left(y_i - f(\boldsymbol{x}_i) - \epsilon - \hat{\xi}_i\right) \\
&
let \: \frac{\partial{L}}{\partial{\boldsymbol{w}}} = \frac{\partial{L}}{\partial{b}} =\frac{\partial{L}}{\partial{\xi_i}} = \frac{\partial{L}}{\partial{\hat{\xi}}_i} = 0, \\
&
\Rightarrow 
 
\begin{cases}
\boldsymbol{w} = \sum_{i=1}^m(\hat{\alpha}_i - \alpha_i)\boldsymbol{x}_i, \\
0 = \sum_{i=1}^m(\hat{\alpha}_i - \alpha_i) , \\
C = \alpha_i + \mu_i, \\
C = \hat{\alpha}_i + \hat{\mu}_i. \\
\end{cases}
\end{align*} \\
$$


$$
\begin{align*}
\max_{\boldsymbol{\alpha}, \boldsymbol{\hat{\alpha}}} 
& \sum_{i=1}^m y_i(\hat{\alpha}_i - \alpha_i) - \epsilon(\hat{\alpha}_i + \alpha_i) 
\\
& - \frac{1}{2} \sum_{i=1}^m \sum_{j=1}^m(\hat{\alpha}_i - \alpha_i)(\hat{\alpha}_j - \alpha_j)\boldsymbol{x}_i^T\boldsymbol{x}_j \\
s.t. 
&
\sum_{i=1}^m (\hat{\alpha}_i - \alpha_i) = 0, \\
&
0 \le \alpha_i, \hat{\alpha_i} \le C

\end{align*} \\
$$

$$
KKT: 
\begin{cases}
 \alpha_i\left(f(\boldsymbol{x}_i)- y_i - \epsilon - \xi_i\right) = 0, \\
\hat{\alpha}_i\left(y_i - f(\boldsymbol{x}_i) - \epsilon - \hat{\xi}_i\right) = 0, \\
\alpha_i \hat{\alpha}_i = 0, \xi \hat{\xi}_i=0, \\
(C-\alpha_i)\xi_i = 0, (C-\hat{\alpha}_i)\hat{\xi}_i = 0.
\end{cases}
$$

$$
f(x) =\sum_{i=1}^m(\hat{\alpha}_i - \alpha_i)\boldsymbol{x}_i^T \boldsymbol{x} +b \\
b = y_i + \epsilon - \sum_{i=1}^m{(\hat{\alpha}_i - \alpha_i)}\boldsymbol{x}_i^T \boldsymbol{x}
$$

$$
\boldsymbol{w} = \sum_{i=1}^m(\hat{\alpha}_i - \alpha_i)\phi(\boldsymbol{x}_i).
\\
f(\boldsymbol{x}) =\sum_{i=1}^m(\hat{\alpha}_i - \alpha_i)\kappa (\boldsymbol{x}_i^T, \boldsymbol{x}) +b
$$
