$$
Ent(D) = -\sum _{k=1} ^{|\mathcal{Y}|} {p_k \log_2 p_k} \\
Gain(D,a) = Ent(D)- \sum _{v=1} ^V {\frac{|D^v|}{D} Ent(D^v)} \\
a_* = \arg \max _{a \in A} {Gain(D,a)}
$$



$$
Gain\_ratio(D,a) = \frac{Gain(D,a)}{IV(a)} \\
IV(a) = - \sum_{v=1}^V \frac{|D^v|}{|D|} \log_2{\frac{|D^v|}{|D|}} \\
a_* = \arg \max _{a \in A} {Gain\_ratio(D,a)}
$$



$$
Gini(D) = \sum_{k=1}^{|\mathcal{Y}|} \sum_{k'\ne k} p_k p_{k'} 
= 1 - \sum _{k=1}^{|\mathcal{Y}|} p_k^2 \\
Gini\_index(D,a) = \sum _{v=1}^{V} \frac{|D^v|}{|D|}Gini(D^v) \\
a_* = \arg \min _{a \in A} Gini\_index(D,a)
$$

