$$
f(x) = \boldsymbol{w}^T \boldsymbol{x} + \gamma \\
g(f(x)) = \boldsymbol{w}^T \boldsymbol{x} + \gamma\\
$$

单调可微 $g(\cdot)$,使得线性模型推广到广义线性模型。而应用$\sigma$函数：

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


