### Least Squared Method

------

$$
\begin{cases}
&LS
& \boldsymbol{\theta}^* =\boldsymbol{\Phi}^\dagger\boldsymbol{y}
\\
&LA
&\widehat{\boldsymbol{\theta}} = (\boldsymbol\Phi^\top \widetilde{W}\boldsymbol{\Phi})^\dagger\boldsymbol\Phi^\top \widetilde{W}\boldsymbol{y}
\\
&Hugger
& \widehat{\boldsymbol{\theta}} = (\boldsymbol\Phi^\top \widetilde{W}\boldsymbol{\Phi}+ \lambda\boldsymbol\Theta^\dagger)^\dagger\boldsymbol\Phi^\top \widetilde{W}\boldsymbol{y}
\\
&Tukey
& TBD
\\
&0/1
& TBD
\\
&Ramp
& \widehat{\boldsymbol{\theta}} = (\boldsymbol\Phi^\top {W}\boldsymbol{\Phi}+ \lambda\boldsymbol I)^\dagger\boldsymbol\Phi^\top {WV}\boldsymbol{y}
\end{cases}
$$

-------

$$
\begin{cases} 
&LS  	&\|\Delta\|_2   
\\

&LA 	&\|\Delta\|_1
\\

&Hugger & \sum\rho_{Huger}(r), 
    &\rho_H = \begin{cases}
    r^2/2 &(|r| \le \eta)\\
    \eta|r|-\eta^2/2 & (|r| \gt \eta)
    \end{cases}
\\

&Tukey  & \sum\rho_{Tukey}(r),
    &\rho_T =  \begin{cases}
        \frac{\left(1- [1-\frac{r^2}{\eta^2}]^3 \right)\eta^2}{6},
        &|r|\le\eta
        \\
        
        \frac{\eta^2}{6}, &|r| > \eta
    \end{cases}
\\

& 0/1 
	& \frac{1}{2}\sum_{i=1}^n \left(sign(\hat{y}_i)-y_i\right)^2
	& sign(m) = \begin{cases}
		& +1 & m \gt 0 \\
		& 0  & m = 0  \\
		& -1 & m < 0
	\end{cases}	
\\

& 0/1 
	&\frac{1}{2}\sum_{i=1}^n\left( 1 - sign(\hat{y}_i)y_i \right)
\\
& Ramp
    & \sum_{i=1}^n \gamma(1-\hat{y}_iy_i)
    & \gamma(m)=\min \left\{ 1, \max(0,1-m) \right\}= 	           
    \begin{cases}
       &1          &(m\lt 0) \\
       & 1-m       &(0\le m \le 1) \\
       &0          &(m\gt 1)
    \end{cases}

\end{cases}
$$

------

$$
\begin{cases}
\|\boldsymbol{\theta}\|_0 &= \sum_{j=1}^b\delta(\theta_j \ne 0), \delta(\theta_j \ne 0) = \begin{cases}
1 & (\theta_j \ne 0) \\
0 & (\theta = 0)
\end{cases}
\\
\|\boldsymbol\theta\|_1 &= \sum_{j=1}^b |\theta_j| \\
\|\boldsymbol\theta\|_2 &=  \boldsymbol\theta^\top\boldsymbol\theta
= \sum_{j=1}^b\theta_j^2\\
\|\boldsymbol\theta\|_p &= \left(\sum_{j=1}^b|\theta_j|^p \right)^{\frac{1}{p}} \\
\|\boldsymbol\theta\|_\infty &=\max\{|\theta_1|, |\theta_2|, \cdots, |\theta_b|\} \\
\end{cases}
$$

------

$$
\min_{\theta} J_{LS}(\boldsymbol{\theta}), 
J_{LS}(\boldsymbol{\theta})  = \frac{1}{2}\|\boldsymbol{y}-\hat{\boldsymbol{y}}\|^2 \\

\boldsymbol{\theta}^* = (X^TX)^{-1}X^TY = X^\dagger Y
$$

------

$$
\min_{\theta} J_{LS}(\boldsymbol{\theta}) , s.t. P\theta = \boldsymbol{\theta} \\
\boldsymbol{\theta}^* = (XP)^{\dagger}Y
$$

-----

$$
\min_{\theta} J_{LS}(\boldsymbol{\theta}), \: s.t. \|\boldsymbol{\theta}\|^2 \le R \\
L(\boldsymbol{\theta}, {\lambda}) 
= J_{LS} + \frac{\lambda}{2} (\|\boldsymbol{\theta}\|^2 - R) \\
\max_{\lambda}\min_{\theta} \left[ J_{LS} + \frac{\lambda}{2} (\|\boldsymbol{\theta}\|^2 - R)  \right], 
s.t. \lambda \gt 0 \\
\hat{\boldsymbol{\theta}} = \left( X^TX+ \lambda I\right)^{-1}X^TY
$$

-----

$$
\min_{\theta} J_{LS}(\boldsymbol{\theta}), \: s.t. \|\boldsymbol{\theta}\|_1 \le R \\
\|\boldsymbol{\theta}\|_1  = \sum_{j=1}^m|\theta_j| \\
\min J (\boldsymbol{\theta}), J(\boldsymbol{\theta}) = J_{LS}(\boldsymbol{\theta}) + \lambda\|\boldsymbol{\theta}\|_1 \\
\hat{\boldsymbol{\theta}} = \left( \Phi^\top\Phi +\lambda \tilde{\Theta}^{\dagger} \right)^{-1}\Phi^\top \boldsymbol{y}\\
$$

------

$$
\widehat{\boldsymbol{\theta}}_{LA} = \mathop{\arg\min}_\theta J_{LA}(\boldsymbol{\theta}),
J_{LA}(\boldsymbol{\theta}) = \sum_{i=1}^m|\hat{y}_i - y_i |
$$

------

$$
\widehat{\boldsymbol{\theta}} = \mathop{\arg\min}_\theta{\widetilde{J}(\boldsymbol{\theta})},\\

\widetilde{J}(\boldsymbol{\theta}) = \frac{1}{2} \sum_{i=1}^n \widetilde{w}_ir_i +C , 
\\\text{where}
\begin{cases}
&\widetilde{w}_i = \begin{cases}
1, &(|\widetilde{r}_i|\le \eta )\\
\eta/|\widetilde{r}_i|, & (|\widetilde{r}_i|\ge\eta)\\
\end{cases} \\
&C = \sum_{i:|\widetilde{r}_i|\gt\eta}(\eta|\widetilde{r}_i| - \eta^2)/2
\end{cases}
$$

$$
\widehat{\boldsymbol{\theta}} = (\boldsymbol\Phi^\top \widetilde{W}\boldsymbol{\Phi})^\dagger\boldsymbol\Phi^\top \widetilde{W}\boldsymbol{y}
$$

------------

$$
\widehat{\boldsymbol{\theta}} = \mathop{\arg\min}_{\theta} \sum_{i=1}^n \rho_{Huber}(r_i),
 \: s.t. \|\theta\|_1 \le R \\
 \widehat{\boldsymbol{\theta}} = (\boldsymbol\Phi^\top \widetilde{W}\boldsymbol{\Phi}+ \lambda\boldsymbol\Theta^\dagger)^\dagger\boldsymbol\Phi^\top \widetilde{W}\boldsymbol{y}
$$

----

$$
\widehat{\boldsymbol{\theta}} = \mathop{\arg\min}_{\theta} \sum_{i=1}^n \rho_{Ramp}(r_i),\\
 \widehat{\boldsymbol{\theta}} = (\boldsymbol\Phi^\top {W}\boldsymbol{\Phi}+ \lambda\boldsymbol I)^\dagger\boldsymbol\Phi^\top {WV}\boldsymbol{y}
$$

