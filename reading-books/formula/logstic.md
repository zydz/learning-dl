$$
f(x) = \boldsymbol{w}^T \boldsymbol{x} + \gamma \\
g(f(x)) = \boldsymbol{w}^T \boldsymbol{x} + \gamma\\
$$

单调可微 $g(\cdot)$,使得线性模型推广到广义线性模型。

而应用$\sigma$函数：
$$
z = \boldsymbol{w}^T \boldsymbol{x} + \gamma \\
\sigma(z) = \frac{1}{1+e^{-z}} \\
y = \sigma(z) = \frac{1}{1+e^{-(\boldsymbol{w}^T \boldsymbol{x} + \gamma)}}
$$

$$
y = P(\boldsymbol{x} \in D^+), 
1-y = P(\boldsymbol{x} \in D^-) \\
\ln{\frac{y}{1-y}} = \boldsymbol{w}^T \boldsymbol{x} + \gamma  \\
\left( \sigma(z) = \frac{1}{1+e^{-z}},  \sigma^{-1}(y) = \ln{\frac{y}{1-y}}  \right)
$$






$$
\begin{split}
d(y,x) &=\sum_{j=1}^b \theta_i^{(y)} \phi_i(x) \\
       &= \boldsymbol{\theta^{(y)^T}\phi} 
\end{split}
\\

q(y|\boldsymbol{x:\theta}) 
= \frac{\exp(d(y,x))}
{\sum_{y'=1}^c\exp(d(y',x))} \\
$$

$$
\Theta =
\begin{bmatrix}
&\theta_1^{(1)} & \theta_2^{(1)} &\cdots &\theta_b^{(1)}\\
&\theta_1^{(2)} & \theta_2^{(2)} &\cdots &\theta_b^{(2)}\\
& \vdots & \vdots & \ddots & \vdots \\
&\theta_1^{(c)} & \theta_2^{(c)} &\cdots &\theta_b^{(c)}\\
\end{bmatrix}_{c \times b} 
\\

\min_{\boldsymbol{\theta}} \prod_{i=1}^n q(\cdot)_i \\
J(\boldsymbol{\theta})=\min_{\boldsymbol{\theta}} \sum_{i=1}^n \log q(\cdot)_i
$$





-----

$$
q(y|\boldsymbol{x:\theta}) \propto \exp\left({\sum_{j=1}^n {\theta_j K(\boldsymbol{x},\boldsymbol{x_j})}}\right),\\
K(\boldsymbol{x},\boldsymbol{c}) 
	= exp\left( 
	-\frac{\| \boldsymbol{x}-\boldsymbol{c}\|^2}{2h^2} 
	\right)
$$

$$
\nabla_y{J_i(\boldsymbol{\theta})} 
= \frac{ \boldsymbol{\theta^{(y)^T}\phi(x_i)}\phi(x_i)}
{\sum_{y'=1}^c\exp( \boldsymbol{\theta^{(y')^T}\phi(x_i)})} +
\begin{cases}
\phi(x_i) & (y=y_i) \\
0 & (y \ne y_i)
\end{cases}
$$





