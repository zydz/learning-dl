$$
\begin{cases}
p(x_i=1|u_i) = \frac{exp(\frac{x}{kT})} {1+ exp{\frac{x}{kT}}}
\\
p(x_i=0|u_i) = \frac{1}{1+ exp{\frac{x}{kT}}}
\end{cases}
$$

$$
L(\theta) = \prod_{n=1}^N p(x_n| \theta) \\
p(x_n|\theta) = \frac{1}{Z(\theta)}exp\{x,\theta \} \\
Z(\theta) = \sum_x{exp\{ -E(x, \theta) \}}
$$

$$
\log{L(\theta)} = \sum_{n=1}^N \log{p(x_n| \theta)}
$$

