



#### Linear Regression Loss

$$
\ell = |\hat{y} - y|^2
$$



#### Cross Entropy Loss

$$
y\log{\hat{y}} + \dot{y}\log{\hat{\dot{y}}} \\
\dot{y} = 1-y \\
\sum_{n=1}^{N} - \frac{1}{N}\left( y_n\log{\hat{y}_n} + \dot{y}_n\log{\hat{\dot{y}}_n} \right) \\
\sum_{n=1}^{N} - \frac{1}{N}\left( y_n\log{\hat{y}_n} + (1-y_n)\log{(1-\hat{y}_n)} \right) \\
$$



#### Sigmoid Fonction

$$
\sigma{(z)} = \frac{1}{1-e^{-z}} \\
z = x*w + b \\
\hat{y} = \sigma{(z)} = \left[{1-e^{-(x*w + b)}}\right]^{-1}
$$

#### TODO

$$
A= \begin{bmatrix}
a_1 & b_1 \\
a_2 & b_2 \\
\cdots & \cdots \\
a_n & b_n \\
\end{bmatrix}  \\
    \\
    \\
w = \begin{bmatrix}
w_1 \\
w_2 \\
\end{bmatrix} ,\\
    \\
Y = \begin{bmatrix}
y_1 \\
y_2 \\
\cdots \\
y_n
\end{bmatrix} \\
    \\
XW = \hat{Y}
$$





#### SoftMax

$$
softmax() = \frac{e_i} {\sum_{j=1}^{N} {e_j}} \\
\prod_{i=1}^{n} =  \\
\Sigma \sum \\
\Pi \prod
$$

#### Back Propagation

$$
\frac{\partial{loss}}{\partial{w}} = ?
$$

$$
k'(x)=\lim_{\Delta x\to 0}\frac{k(x)-k(x-\Delta x)}{\Delta x}
$$


$$
\mathcal{JL} \\
\ell  \\ 
\phi \Phi \\
\Theta \theta \\
\psi \Psi \\
h_{\Theta }(x) \in \mathbb{R} ^4 \\
$$

$$
J(\theta_0, \theta_1) = \frac{1}{2m} (\sum_{i=1}^m(h_{\theta}(x^{(i)})  -y^{(i)})^2 + \lambda \sum_{j=1}^n{\theta_j^2})
$$

$$
\parallel  \\
\mid \\
$$

