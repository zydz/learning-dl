能量函数E总是非递增的，

即随着时间的不断增加而逐渐减小，

直到网络达到稳定的状态为止。
$$
x_i(t+1) = 
\begin{cases}
1 		& u_i(t) > 0  	\\
x_i(t) 	& u_i(t) = 0	\\
0 		&u_i(t) < 0		\\
\end{cases} 
\\

u_i(t) = \sum_{j=1}^n w_{ij}x_j(t) - b_i(t) 
\\

E = -\frac{1}{2}\sum_{i=1}^n\sum_{j=1}^n w_{ij}x_ix_j + \sum_{i=1}^n b_ix_i
$$

$$
\begin{align*}
E = & - \frac{1}{2}\sum_{i \ne k}^n\sum_{j\ne k}^n w_{ij}x_ix_j - \sum_{i\ne k}^n b_ix_i \\
&- \frac{1}{2}\left( \sum_j^n w_{kj}x_j \sum_i^n w_{ki}x_i \right)x_k + b_kx_k
\end{align*}
$$

$$
x_k(t) \to x_k(t+1)
$$

$$
\begin{align*}
\Delta E_k &= - \frac{1}{2}\left( \sum_j^n w_{kj}x_j \sum_i^n w_{ki}x_i \right)\Delta x_k + b_k \Delta x_k \\
&= - \left( \sum_{j=1}^nw_{ij}-b_k \right)\Delta x_k
\end{align*}
$$

$$
\Delta E_k = -u_k \Delta x_k \\
\Delta E_k \le 0
$$

------------

$$
E^s = \frac{1}{2} \sum_{i=1}^n\sum_{j=1}^n w_{ij}^sx_i^sx_j^s \\
let: w_{ij}^s = x_i^s x_j^s \\
E^s = -\frac{1}{2}\sum_{i=1}^n\sum_{j=1}^n{(x_i^s)}^2(x_j^s)^2 \\
w_{ij} = \frac{1}{P}\sum_{s=1}^Pw_{ij}^s = \frac{1}{P}\sum_{s=1}^Px_i^sx_j^s
$$

-----------------------

