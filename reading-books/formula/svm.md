$$
\boxed{D = \{ (x_1,y_1), (x_2,y_2), \cdots, (x_m, y_m)\}, y_i \in \{ -1, +1 \} } \\
\boxed{\boldsymbol{w}^T \boldsymbol{x} + b = 0, \\
\gamma = \frac{|\boldsymbol{w}^T \boldsymbol{x} + b|}{ \| \boldsymbol{w} \|} }\\
\boxed{
\begin{cases}
\boldsymbol{w}^T \boldsymbol{x}_i + b \ge +1, y_i = +1 ; \\
\boldsymbol{w}^T \boldsymbol{x}_i + b \le +1, y_i = -1 .
\end{cases} \\
\gamma = \frac{2}{\|\boldsymbol{w}\|} \\ }\\
\boxed {\max_{w,b}  \frac{2}{\| \boldsymbol{w} \|} \\
 s.t.\: y_i{(w^T x_i+b)} \ge 1, i = 1,2,\cdots, m. \\
 }\\
\boxed{\min_{w,b}  \frac{1}{2} {\| \boldsymbol{w} \|}^2\\
s.t.\: y_i{(w^T x_i+b)} \ge 1, i = 1,2,\cdots, m. \\ }
$$


$$
\begin{align}

&
L(\boldsymbol{w},b,\boldsymbol{\alpha)}  = \frac{1}{2} \|\boldsymbol{w}\|^2 
+ \sum_{i=1}^m{\alpha_i\left(1-y_i\left(\boldsymbol{w}^T \boldsymbol{x}_i + b\right) \right)} \\

&
\begin{cases}
\frac{\partial{L}} {\partial{\boldsymbol{w}}} = 0  \\
\frac{\partial{L}} {\partial{{b}}} = 0 
\end{cases} 
\Rightarrow  
\begin {cases}
\boldsymbol{w} = \sum _{i=1}^m {\alpha_i y_i x_i} , \\
0 = \sum _{i=1} ^{m} \alpha_i y_i .
\end{cases} \\

& \Rightarrow 
\boxed{
 \max_\alpha \sum_{i=1}^m {\alpha_i - \frac{1}{2}} \sum_{i=1}^{m} \sum_{j=1}^m \alpha_i \alpha_j y_i y_jx_i^Tx_j \\
 s.t. \sum_{i=1}^m \alpha_i y_i = 0, \alpha_i \ge 0, i=1,2,\cdots,m.
}


\end{align}
$$

$$
\begin{align*}
f(\boldsymbol{x}) &= \boldsymbol{w}^T \boldsymbol{x} + b\\
& = \sum_{i=1}^m \alpha_i y_i \boldsymbol{x}_i^T \boldsymbol{x} + b
\end{align*} \\
s.t. KKT: 
\begin{cases}
\alpha_i \ge 0; \\
y_i f(x_i) - 1 \ge 0 ; \\
\alpha_i(y_i f(x_i) - 1) = 0.
\end{cases}
$$

$$
\begin{matrix}
Apples & Green \\
Strawberries & Red \\
Oranges & Orange \\
\end{matrix}
$$

-----

$$
\begin{align*}
f(\boldsymbol{x}) &= \boldsymbol{w}^T\phi(\boldsymbol{x}) +b \\
&=\sum_{i=1}^m\alpha_iy_i\kappa(x,x_i) +b
\end{align*}
$$

----

$$
\begin{matrix}
& x: \vec{\boldsymbol{x}}\\
&linear & \kappa(x_i,x_j) = x_i^Tx_j \\
&poly   & \kappa(x_i,x_j) = (x_i^Tx_j)^d \\
&Gause & \kappa(x_i,x_j) = exp(-\frac{\|x_i-x_j\|^2}{2\sigma^2}) \\
&laplas & \kappa(x_i,x_j) = exp(-\frac{\|x_i-x_j\|}{\sigma}) \\
&sigmoid & \kappa(x_i,x_j) = \tanh(\beta x_i^Tx_j+\theta)
\end{matrix}
$$

