$$
y = f(x) = \vec{w}^T\vec{x} + b \\
if \: x \in X:\{\vec{x}_1,\vec{x}_2, \cdots ,\vec{x}_m\}, Y = \{y_1, \cdots, y_m\} \\
J(\vec{w},b) = \frac{1}{2} \sum_{i=1}^m (\hat{y}_i - y_i)^2 
\\
\hat{X} = 
\begin{bmatrix}
 \vec{x}_1;b \\
 \vec{x}_2;b \\
 \cdots      \\
 \vec{x}_m;b
\end{bmatrix}\\
\hat{w} = \{\vec{w}; b\}_{d+1}\\
\hat{Y} = \hat{X}^T\hat{w} \\
J= \frac{1}{2} \| \hat{Y} -Y \|^2 = \frac{1}{2}(\hat{Y}-Y)^T(\hat{Y}- Y)
\\
$$

$$
w^*,b^* = \vec{\hat{w}}^* = \arg \min_{\vec{\hat{w}}} J(\vec{w}) 
\\ 
\frac{\partial{J}}{\partial{\hat{w}}}=0, \\
\hat{w}^* = (\hat{X}^T\hat{X})^{-1}\hat{X}^TY \\
\hat{w}^* = \hat{X}^{\dagger}Y
$$

$$
\Phi = \{\phi_1,\phi_2,\cdots, \phi_d \}\\
\begin{align*}
f(\vec{x} )
& = \theta_1\phi_1(\vec{x})+\theta_2\phi_2(\vec{x}) + \cdots+ \theta_b\phi_b(\vec{x}) \\
& = \sum_{i=1}^d \theta_i \phi_i(\vec{x}) \\
& = \vec{\theta}^T \vec{\phi}(\vec{x})
\end{align*} \\

\Phi = 
\begin{bmatrix}
\phi_1(x_1) &\phi_2(x_1) & \cdots & \phi_b(x_1) \\
\phi_1(x_2) &\phi_2(x_2) & \cdots & \phi_b(x_2) \\
\cdots & \cdots & \cdots & \cdots \\
\phi_1(x_n) &\phi_2(x_n) & \cdots & \phi_b(x_n)
\end{bmatrix} \;\;\;
\vec{\theta} = 
\begin{bmatrix}
\theta_1 \\
\theta_2 \\
\cdots \\
\theta_b
\end{bmatrix}\\
J_{LS} = \frac{1}{2} \|\Phi \vec{\theta} - \vec{y}\| \\
$$

$$
\begin{alignat}{2} 
&
\begin{aligned}
\nabla _{\vec{\theta}} J_{LS} 
& = 
\left( 
\frac{\partial J_{LS}} {\partial{\theta_i}},
\frac{\partial J_{LS}} {\partial{\theta_2}}
\cdots,
\frac{\partial J_{LS}} {\partial{\theta_b}}
\right )^T \\
&= \Phi^T\Phi\vec{\theta} - \Phi^T\vec{y} = 0 \\
\end{aligned} \\
\\
&
\begin{aligned}
\vec{\theta}^* \hspace{0em}
&= (\Phi^T\Phi)^{-1}\Phi^T\vec{y} \\
&= {\Phi}^{\dagger}\vec{y}
\end{aligned}
\end{alignat}
$$

-----

$$
f(\vec{x}) = \vec{w}^T\vec{x} + b \\
margin: \: f(\vec{x}) = \pm 1 \\
\arg \max_{\vec{w}} \frac{2}{\|\vec{w}\|} \\
\Rightarrow 
\boxed{
\vec{w}^* =\arg\min_{\vec{w}}\frac{\|\vec{w}\|}{2} \\
s.t.  \:\: y_i(\vec{w}^T\vec{x}_i + b ) \ge 1
}
$$

$$
\mathcal{L}(w,b,\alpha)
= \frac{\|w\|}{2} + \sum_{i=1}^m \alpha_i\left(1 - (\vec{w}^T\vec{x}_i + b )\right), \\
s.t.
\begin{cases}
\alpha_i \ge 0, \\
y_i(\vec{w}^T\vec{x}_i + b ) -1 \ge 0 \\
\alpha_i\left((\vec{w}^T\vec{x}_i + b )-1\right) = 0,\\ 
\end{cases}
$$

$$
{\nabla{\mathcal{L}}}= 
( 
\frac{\partial{\mathcal{L}}}{\partial{w}},
\frac{\partial{\mathcal{L}}}{\partial{b}},
\frac{\partial{\mathcal{L}}}{\partial{\alpha}}
)^T 
= 0 \\
\boxed{\max_\alpha \sum_{i=1}^m \alpha_i- \frac{1}{2}\sum_{i=1}^m\sum_{j=1}^m\alpha_i\alpha_j y_i y_j x_i^Tx_j \\
s.t. \sum_{i=1}^m\alpha_i y_i = 0, i=1,2,\cdots,m.}
$$

-----

$$
\boxed{\min_{w,b} \frac{1}{2}\|w\|^2 + C \sum_{i=1}^m\xi_i ,\\
s.t. \begin{cases}
y_i(w^Tx_i+b) \ge 1-\xi_i \\
\xi_i \ge 0, i=1,2,\cdots,m
\end{cases}}\\
\begin{align*}
L(w,b,\alpha,\xi,\mu) 
&= \frac{1}{2}\|w\|^2 + C\sum_{i=1}^m\xi_i \\
&+\sum_{i=1}^m\alpha_i\left(1-\xi_i-y_i(w^Tx_i+b)\right) \\
\end{align*}\\

{\nabla{\mathcal{L}}}= 
( 
\frac{\partial{\mathcal{L}}}{\partial{w}},
\frac{\partial{\mathcal{L}}}{\partial{b}},
\frac{\partial{\mathcal{L}}}{\partial{\alpha}},
\frac{\partial{\mathcal{L}}}{\partial{\xi}},
\frac{\partial{\mathcal{L}}}{\partial{\mu}},
)^T 
= 0
$$

$$
\boxed{
\max_\alpha \sum_{i=1}^m \alpha_i- \frac{1}{2}\sum_{i=1}^m\sum_{j=1}^m\alpha_i\alpha_j y_i y_j x_i^Tx_j \\
s.t. \sum_{i=1}^m\alpha_i y_i = 0, 0 \le \alpha_i \le C, i=1,2,\cdots,m.
}
$$

-----

