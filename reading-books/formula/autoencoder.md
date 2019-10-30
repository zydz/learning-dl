$$
\begin{cases}
\boldsymbol{y} = f(\boldsymbol{W}\boldsymbol{x}+\boldsymbol{b}) 
\\
\widetilde{\boldsymbol{x}} = \widetilde{f}(\widetilde{\boldsymbol{W}}\boldsymbol{y}+\widetilde{b}) \\
\end{cases} 
\\
\Rightarrow 
\widetilde{\boldsymbol{x}} = \widetilde{f}(\widetilde{\boldsymbol{W}}\boldsymbol{f(\boldsymbol{W}\boldsymbol{x}+\boldsymbol{b}) }+\widetilde{b}) \\
$$

$$
E = \sum_{n=1}^N{\| x_n - \widetilde{x_n} \|^2 }
$$

$$
E = -\sum_{i=1}^N (x_i\log \widetilde{x_i})\log(1-\widetilde{x_i})
$$

------

$$
\widetilde{\boldsymbol{x}} = \boldsymbol{x}+v\boldsymbol{x} \\
v \sim \mathfrak{D}(0,\sigma^2)
$$

-------

$$
E = \sum_{i=1}^N\| x_n - \tilde{x}_n\|^2 + 
\beta\sum_{j=1}^M KL(\rho\|\hat{\rho}_j) 

\\
\hat{\rho}_j = \frac{1}{N}\sum_{n=1}^N f(W_j x_n+b_j)
\\
KL(\rho\|\hat{\rho}_j) = \rho\log\frac{\rho}{\hat{\rho}_j}+(1-\rho)\log{\frac{1-\rho}{1-\hat{\rho}_j}}
\\
$$

$$
\begin{align*}
\frac{\partial}{\partial u_j} \left( 
\beta\sum_{j=1}^M KL(\rho\|\hat{\rho}_j) 
\right)
&=
\beta \frac{\partial}{\partial \hat \rho_j}KL(\rho\|\hat{\rho}_j) \frac{\partial \hat{\rho}_j}{\partial u_j}
\\
&=\left( -\frac{\rho}{\hat \rho_j}+ \frac{1-\rho}{1-\hat \rho_j} \right) \frac{\partial \hat{\rho}_j}{\partial u_j}
\end{align*}
$$

$$
\frac{\partial}{\partial u_j} \left( 
\beta\sum_{j=1}^M KL(\rho\|\hat{\rho}_j) 
\right)
=\left( -\frac{\rho}{\hat \rho_j}+ \frac{1-\rho}{1-\hat \rho_j} \right) \frac{\partial \hat{\rho}_j}{\partial u_j}
f'(W_jx_n+b_j)
$$

$$
\hat{\rho}_j^{(t)}=\lambda \hat{\rho}_j^{(t-1)} + (1-\lambda)\hat{\rho}_j^{(t)}
$$



------

