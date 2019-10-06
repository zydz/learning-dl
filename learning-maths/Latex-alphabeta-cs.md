# LaTeX数学符号总结（jupyter notebook）

-----

[Referance](https://blog.csdn.net/qq_39232265/article/details/78868487)

---

##  1. LaTeX 数学公式基础知识

LaTeX的强大之处在于对数学符号和公式的排版，所以jupyter notebook采用LaTeX来进行数学符号和公式的显示排版。
首先，在jupyter notebook 里面，LaTeX数学公式用$$括起来。
数学模式和文本模式又很多的不同之处。例如在数学模式中：

空格和分行都会被忽略，所有的空格或是由数学表达式逻辑的衍生，或是由特殊命令如\，\quad或\qquad来得到。空格可以用&emsp;或者&nbsp;表示
不允许有空行，每个公式中只能有一个段落。
每个字符都将被看作是一个变量名并以此来排版。

## 2. 常用的排版命令

**分式**
命令\frac{a}{b}形式：$\frac{a}{b}$
​    

命令\sum_{i=1}^n p_i形式：$\sum_{i=1}^n p_i$
​    

## 3.常用的数学模式命令

##### **1. 数学模式重音符**

| Symbol | Command   | Symbol | Command   | Symbol | Command       |
|:------:|:---------:|:------:|:---------:|:------:|:-------------:|
| a^a^   | \hat{a}   | aˋaˋ   | \grave{a} | aˉaˉ   | \bar{a}       |
| aˇaˇ   | \check{a} | a˙a˙   | \dot{a}   | a⃗a    | \vec{a}       |
| a~a~   | \tilde{a} | a¨a¨   | \ddot{a}  | A^A    | \widehat{A}   |
| aˊaˊ   | \acute{a} | a˘a˘   | \breve{a} | A~A    | \widetilde{A} |

##### **2. 小写希腊字母**

| Symbol | Command     | Symbol | Command   | Symbol | Command   |
|:------:|:-----------:|:------:|:---------:|:------:|:---------:|
| αα     | \alpha      | θθ     | \theta    | oo     | o         |
| ββ     | \beta       | ϑϑ     | \vartheta | ππ     | \pi       |
| γγ     | \gamma      | ιι     | \iota     | ϖϖ     | \varpi    |
| δδ     | \delta      | κκ     | \kappa    | ρρ     | \rho      |
| ϵϵ     | \epsilon    | λλ     | \lambda   | ϱϱ     | \varrho   |
| εε     | \varepsilon | μμ     | \mu       | σσ     | \sigma    |
| ζζ     | \zeta       | νν     | \nu       | ςς     | \varsigma |
| ηη     | \eta        | ξξ     | \xi       | ττ     | \tau      |
| υυ     | \upsilon    | ϕϕ     | \phi      | φφ     | \varphi   |
| χχ     | \chi        | ψψ     | \psi      | ωω     | \omega    |

##### **3. 大写希腊字母**

| Symbol | Command | Symbol | Command | Symbol | Command  |
|:------:|:-------:|:------:|:-------:|:------:|:--------:|
| ΓΓ     | \Gamma  | ΛΛ     | \Lambda | ΣΣ     | \Sigma   |
| ΔΔ     | \Delta  | ΞΞ     | \Xi     | ΥΥ     | \Upsilon |
| ΘΘ     | \Theta  | ΠΠ     | \Pi     | ΦΦ     | \Phi     |
| ΨΨ     | \Psi    | ΩΩ     | \Omega  |        |          |

##### **4. 二元关系符**

| Symbol | Command     | Symbol | Command      | Symbol | Command     |
|:------:|:-----------:|:------:|:------------:|:------:|:-----------:|
| &gt;>  | >           | &lt;<  | <            | ==     | =           |
| ≤≤     | \leq or \le | ≥≥     | \geq or \ge  | ≡≡     | \equiv      |
| ≪≪     | \ll         | ≫≫     | \gg          | ≐≐     | \doteq      |
| ≺≺     | \prec       | ≻≻     | \succ        | ∼∼     | \sim        |
| ⪯⪯     | \preceq     | ⪰⪰     | \succeq      | ≃≃     | \simeq      |
| ⊂⊂     | \subset     | ⊃⊃     | \supset      | ≈≈     | \approx     |
| ⊆⊆     | \subseteq   | ⊇⊇     | \supseteq    | ≅≅     | \cong       |
| ⊏⊏     | \sqsubset   | ⊐⊐     | \sqsupset    | ⋈⋈     | \Join       |
| ⊑⊑     | \sqsubseteq | ⊒⊒     | \sqsupseteq  | ⋈⋈     | \bowtie     |
| ∈∈     | \in         | ∋∋     | \ni or \owns | ∝∝     | \propto     |
| ⊢⊢     | \vdash      | ⊣⊣     | \dashv       | ⊨⊨     | \models     |
| ∣∣     | \mid        | ∥∥     | \parallel    | ⊥⊥     | \perp       |
| ⌣⌣     | \smile      | ⌢⌢     | \frown       | ≍≍     | \asymp      |
| ::     | :           | ∉∈/​   | \notin       | ≠̸​=   | \neq or \ne |

##### **5. 二元运算符**

| Symbol | Command        | Symbol | Command          | Symbol | Command        |
|:------:|:--------------:|:------:|:----------------:|:------:|:--------------:|
| ++     | +              | −−     | -                |        |                |
| ±±     | \pm            | ∓∓     | \mp              | ◃◃     | \triangleleft  |
| ⋅⋅     | \cdot          | ÷÷     | \div             | ▹▹     | \triangleright |
| ××     | \times         | ∖∖     | \setminus        | ⋆⋆     | \star          |
| ∪∪     | \cup           | ∩∩     | \cap             | ∗∗     | \ast           |
| ⊔⊔     | \sqcup         | ⊓⊓     | \sqcap           | ∘∘     | \circ          |
| ∨∨     | \vee or \lor   | ∧∧     | \wedge or \land  | ∙∙     | \bullet        |
| ⊕⊕     | \oplus         | ⊖⊖     | \ominus          | ⋄⋄     | \diamond       |
| ⊙⊙     | \odot          | ⊘⊘     | \oslash          | ⊎⊎     | \uplus         |
| ⊗⊗     | \otimes        | ◯◯     | \bigcirc         | ⨿⨿     | \amalg         |
| △△     | \bigtriangleup | ▽▽     | \bigtriangledown | ††     | \dagger        |
| ⊲⊲     | \lhd           | ⊳⊳     | \rhd             | ‡‡     | \ddagger       |
| ⊴⊴     | \unlhd         | ⊵⊵     | \unrhd           | ≀≀     | \wr            |

##### **6. 大尺寸运算符**

| Symbol | Command   | Symbol | Command    | Symbol | Command |
|:------:|:---------:|:------:|:----------:|:------:|:-------:|
| ∑∑     | \sum      | ⋃⋃     | \bigcup    | ⋂⋂     | \bigcap |
| ⋁⋁     | \bigvee   | ⨁⨁     | \bigoplus  | ∏∏     | \prod   |
| ⋀⋀     | \bigwedge | ⨂⨂     | \bigotimes | ∐∐     | \coprod |
| ⨆⨆     | \bigsqcup | ⨀⨀     | \bigodot   | ∫∫     | \int    |
| ∮∮     | \oint     | ⨄⨄     | \biguplus  |        |         |

##### **7. 箭头**

| Symbol | Command             | Symbol | Command             | Symbol | Command      |
|:------:|:-------------------:|:------:|:-------------------:|:------:|:------------:|
| ←←     | \leftarrow or \gets | ⟵⟵     | \longleftarrow      | ↑↑     | \uparrow     |
| →→     | \rightarrow or \to  | ⟶⟶     | \longrightarrow     | ↓↓     | \downarrow   |
| ↔↔     | \leftrightarrow     | ⟷⟷     | \longleftrightarrow | ↕↕     | \updownarrow |
| ⇐⇐     | \Leftarrow          | ⟸⟸     | \Longleftarrow      | ⇑⇑     | \Uparrow     |
| ⇒⇒     | \Rightarrow         | ⟹⟹     | \Longrightarrow     | ⇓⇓     | \Downarrow   |
| ⇔⇔     | \Leftrightarrow     | ⟺⟺     | \Longleftrightarrow | ⇕⇕     | \Updownarrow |
| ↦↦     | \mapsto             | ⟼⟼     | \longmapsto         | ↗↗     | \nearrow     |
| ↩↩     | \hookleftarrow      | ↪↪     | \hookrightarrow     | ↘↘     | \searrow     |
| ↼↼     | \leftharpoonup      | ⇀⇀     | \rightharpoonup     | ↙↙     | \swarrow     |
| ↽↽     | \leftharpoondown    | ⇁⇁     | \rightharpoondown   | ↖↖     | \nwarrow     |
| ⇌⇌     | \rightleftharpoons  | ⟺⟺     | \iff                | ⇝⇝     | \leadsto     |

##### **8. 定界符**

| Symbol | Command      | Symbol | Command      | Symbol | Command      |
|:------:|:------------:|:------:|:------------:|:------:|:------------:|
| ((     | (            | ))     | )            | ↑↑     | \uparrow     |
| [[     | [ or \lbrack | ]]     | ] or \rbrack | ↓↓     | \downarrow   |
| {{     | { or \lbrace | }}     | } or \rbrace | ↕↕     | \updownarrow |
| ⟨⟨     | \langle      | ⟩⟩     | \rangle      | ⇑⇑     | \Uparrow     |
| $      | $            | \vert  | ∥∥           |        | or \Vert     |
| ⌊⌊     | \lfloor      | ⌋⌋     | \rfloor      | ⇕⇕     | \Updownarrow |
| ⌈⌈     | \lceil       | ⌉⌉     | \rceil       | //     | /            |
| \\     | \backslash   |        |              |        |              |

##### **9. 大尺寸定界符**

| Symbol                                                                                  | Command     | Symbol                                                                                  | Command    | Symbol                                                                                  | Command     |
|:---------------------------------------------------------------------------------------:|:-----------:|:---------------------------------------------------------------------------------------:|:----------:|:---------------------------------------------------------------------------------------:|:-----------:|
| ⟮⟮                                                                                      | \lgroup     | ⟯⟯                                                                                      | \rgroup    | ⎰⎰                                                                                      | \lmoustache |
| ⎱⎱                                                                                      | \rmoustache | KaTeX parse error: Expected 'EOF', got '\arrowvert' at position 1: \̲a̲r̲r̲o̲w̲v̲e̲r̲t̲ | \arrowvert | KaTeX parse error: Expected 'EOF', got '\Arrowvert' at position 1: \̲A̲r̲r̲o̲w̲v̲e̲r̲t̲ | \Arrowvert  |
| KaTeX parse error: Expected 'EOF', got '\bracevert' at position 1: \̲b̲r̲a̲c̲e̲v̲e̲r̲t̲ | \bracevert  |                                                                                         |            |                                                                                         |             |

##### **10. 其他符号**

| Symbol | Command   | Symbol | Command      | Symbol | Command       |
|:------:|:---------:|:------:|:------------:|:------:|:-------------:|
| ……     | \dots     | ⋯⋯     | \cdots       | ⋮⋮     | \vdots        |
| ⋱⋱     | \ddots    | ℏℏ     | \hbar        | ıı     | \imath        |
| ȷȷ     | \jmath    | ℓℓ     | \ell         | ℜℜ     | \Re           |
| ℑℑ     | \Im       | ℵℵ     | \aleph       | ℘℘     | \wp           |
| ∀∀     | \forall   | ∃∃     | \exists      | ℧℧     | \mho          |
| ∂∂     | \partial  | ′′     | ’            | ′′     | \prime        |
| ∅∅     | \emptyset | ∞∞     | \infty       | ∇∇     | \nabla        |
| △△     | \triangle | □□     | \Box         | ◊◊     | \Diamond      |
| ⊥⊥     | \bot      | ⊤⊤     | \top         | ∠∠     | \angle        |
| √√     | \surd     | ♢♢     | \diamondsuit | ♡♡     | \heartsuit    |
| ♣♣     | \clubsuit | ♠♠     | \spadesuit   | ¬¬     | \neg or \lnot |
| ♭♭     | \flat     | ♮♮     | \natural     | ♯♯     | \sharp        |

##### **11. 非数学符号**

| Symbol                                                          | Command |
|:---------------------------------------------------------------:|:-------:|
| KaTeX parse error: Expected 'EOF', got '\S' at position 1: \̲S̲ | \S      |

##### **12. AMS定界符**

| Symbol | Command   | Symbol | Command   | Symbol | Command   |
|:------:|:---------:|:------:|:---------:|:------:|:---------:|
| ┌┌     | \ulcorner | ┐┐     | \urcorner | └└     | \llcorner |
| ┘┘     | \lrcorner | ∣∣     | \lvert    | ∣∣     | \rvert    |
| ∥∥     | \lVert    | ∥∥     | \rVert    |        |           |

##### **13. AMS希腊和希伯来字母**

| Symbol | Command  | Symbol | Command   | Symbol | Command |
|:------:|:--------:|:------:|:---------:|:------:|:-------:|
| ϝϝ     | \digamma | ϰϰ     | \varkappa | ℶℶ     | \beth   |
| ℸℸ     | \daleth  | ℷℷ     | \gimel    |        |         |

##### **14. AMS二元关系符**

| Symbol | Command         | Symbol | Command        | Symbol | Command             |
|:------:|:---------------:|:------:|:--------------:|:------:|:-------------------:|
| ⋖⋖     | \lessdot        | ⋗⋗     | \gtrdot        | ≑≑     | \doteqdot or \Doteq |
| ⩽⩽     | \leqslant       | ⩾⩾     | \geqslant      | ≓≓     | \risingdotseq       |
| ⪕⪕     | \eqslantless    | ⪖⪖     | \eqslantgtr    | ≒≒     | \fallingdotseq      |
| ≦≦     | \leqq           | ≧≧     | \geqq          | ≖≖     | \eqcirc             |
| ⋘⋘     | \lll or \llless | ⋙⋙     | \ggg or \gggtr | ≗≗     | \circeq             |
| ≲≲     | \lesssim        | ≳≳     | \gtrsim        | ≜≜     | \triangleq          |
| ⪅⪅     | \lessapprox     | ⪆⪆     | \gtrapprox     | ≏≏     | \bumpeq             |
| ≶≶     | \lessgtr        | ≷≷     | \gtrless       | ≎≎     | \Bumpeq             |
| ⋚⋚     | \lesseqgtr      | ⋛⋛     | \gtreqless     | ∼∼     | \thicksim           |
| ⪋⪋     | \lesseqqgtr     | ⪌⪌     | \gtreqqless    | ≈≈     | \thickapprox        |
| ≼≼     | \preccurlyeq    | ≽≽     | \succcurlyeq   | ≊≊     | \approxeq           |
| ⋞⋞     | \curlyeqprec    | ⋟⋟     | \curlyeqsucc   | ∽∽     | \backsim            |
| ≾≾     | \precsim        | ≿≿     | \succsim       | ⋍⋍     | \backsimeq          |
| ⪷⪷     | \precapprox     | ⪸⪸     | \succapprox    | ⊨⊨     | \vDash              |
| ⫅⫅     | \subseteqq      | ⫆⫆     | \supseteqq     | ⊩⊩     | \Vdash              |
| ⋐⋐     | \Subset         | ⋑⋑     | \Supset        | ⊪⊪     | \Vvdash             |
| ⊏⊏     | \sqsubset       | ⊐⊐     | \sqsupset      | ∍∍     | \backepsilon        |
| ∴∴     | \therefore      | ∵∵     | \because       | ∝∝     | \varpropto          |
| ϝϝ     | \digamma        | ϰϰ     | \varkappa      | ℶℶ     | \beth               |
| ϝϝ     | \digamma        | ϰϰ     | \varkappa      | ℶℶ     | \beth               |

##### **15. AMS箭头**

| Symbol | Command            | Symbol | Command            | Symbol | Command              |
|:------:|:------------------:|:------:|:------------------:|:------:|:--------------------:|
| ⇠⇠     | \dashleftarrow     | ⇢⇢     | \dashrightarrow    | ⊸⊸     | \multimap            |
| ⇇⇇     | \leftleftarrows    | ⇉⇉     | \rightrightarrows  | ⇈⇈     | \upuparrows          |
| ⇆⇆     | \leftrightarrows   | ⇄⇄     | \rightleftarrows   | ⇊⇊     | \downdownarrows      |
| ⇚⇚     | \Lleftarrow        | ⇛⇛     | \Rrightarrow       | ↿↿     | \upharpoonleft       |
| ↞↞     | \twoheadleftarrow  | ↠↠     | \twoheadrightarrow | ↾↾     | \upharpoonright      |
| ↢↢     | \leftarrowtail     | ↣↣     | \rightarrowtail    | ⇃⇃     | \downharpoonleft     |
| ⇋⇋     | \leftrightharpoons | ⇌⇌     | \rightleftharpoons | ⇂⇂     | \downharpoonright    |
| ↰↰     | \Lsh               | ↱↱     | \Rsh               | ⇝⇝     | \rightsquigarrow     |
| ↫↫     | \looparrowleft     | ↬↬     | \looparrowright    | ↭↭     | \leftrightsquigarrow |
| ↶↶     | \curvearrowleft    | ↷↷     | \curvearrowright   | ↺↺     | \circlearrowleft     |
| ↻↻     | \circlearrowright  |        |                    |        |                      |

##### **16. AMS二元否定关系符和箭头**

| Symbol | Command       | Symbol | Command       | Symbol | Command           |
|:------:|:-------------:|:------:|:-------------:|:------:|:-----------------:|
| ≮≮     | \nless        | ≯≯     | \ngtr         |      | \varsubsetneqq    |
| ⪇⪇     | \lneq         | ⪈⪈     | \gneq         |      | \varsupsetneqq    |
| ≰≰     | \nleq         | ≱≱     | \ngeq         |      | \nsubseteqq       |
|      | \nleqslant    |      | \ngeqslant    |      | \nsupseteqq       |
| ≨≨     | \lneqq        | ≩≩     | \gneqq        | ∤∤     | \nmid             |
|      | \lvertneqq    |      | \gvertneqq    | ∦∦     | \nparallel        |
|      | \nleqq        |      | \ngeqq        |      | \nshortmid        |
| ⋦⋦     | \lnsim        | ⋧⋧     | \gnsim        |      | \nshortparallel   |
| ⪉⪉     | \lnapprox     | ⪊⪊     | \gnapprox     | ≁≁     | \nsim             |
| ⊀⊀     | \nprec        | ⊁⊁     | \nsucc        | ≆≆     | \ncong            |
| ⋠⋠     | \npreceq      | ⋡⋡     | \nsucceq      | ⊬⊬     | \nvdash           |
| ⪵⪵     | \precneqq     | ⪶⪶     | \succneqq     | ⊭⊭     | \nvDash           |
| ⋨⋨     | \precnsim     | ⋩⋩     | \succnsim     | ⊮⊮     | \nVdash           |
| ⪹⪹     | \precnapprox  | ⪺⪺     | \succnapprox  | ⊯⊯     | \nVDash           |
| ⊊⊊     | \subsetneq    | ⊋⊋     | \supsetneq    | ⋪⋪     | \ntriangleleft    |
|      | \varsubsetneq |      | \varsupsetneq | ⋫⋫     | \ntriangleright   |
| ⊈⊈     | \nsubseteq    | ⊉⊉     | \nsupseteq    | ⋬⋬     | \ntrianglelefteq  |
| ⫋⫋     | \subsetneqq   | ⫌⫌     | \supsetneqq   | ⋭⋭     | \ntrianglerighteq |
| ↚↚     | \nleftarrow   | ↛↛     | \nrightarrow  | ↮↮     | \nleftrightarrow  |
| ⇍⇍     | \nLeftarrow   | ⇏⇏     | \nRightarrow  | ⇎⇎     | \nLeftrightarrow  |

##### **17. AMS二元运算符**

| Symbol | Command            | Symbol | Command            | Symbol | Command         |
|:------:|:------------------:|:------:|:------------------:|:------:|:---------------:|
| ∔∔     | \dotplus           | ⋅⋅     | \centerdot         | ⊺⊺     | \intercal       |
| ⋉⋉     | \ltimes            | ⋊⋊     | \rtimes            | ⋇⋇     | \divideontimes  |
| ⋓⋓     | \Cup or \doublecup | ⋒⋒     | \Cap or \doublecap | ∖∖     | \smallsetminus  |
| ⊻⊻     | \veebar            | ⊼⊼     | \barwedge          | ⩞⩞     | \doublebarwedge |
| ⊞⊞     | \boxplus           | ⊟⊟     | \boxminus          | ⊝⊝     | \circleddash    |
| ⊠⊠     | \boxtimes          | ⊡⊡     | \boxdot            | ⊚⊚     | \circledcirc    |
| ⋋⋋     | \leftthreetimes    | ⋌⋌     | \rightthreetimes   | ⊛⊛     | \circledast     |
| ⋎⋎     | \curlyvee          | ⋏⋏     | \curlywedge        |        |                 |

##### **18. AMS其它符号**

| Symbol | Command       | Symbol | Command            | Symbol | Command         |
|:------:|:-------------:|:------:|:------------------:|:------:|:---------------:|
| ℏℏ     | \hbar         | ℏℏ     | \hslash            | kk     | \Bbbk           |
| □□     | \square       | ■■     | \blacksquare       | ⓈⓈ     | \circledS       |
| △△     | \vartriangle  | ▲▲     | \blacktriangle     | ∁∁     | \complement     |
| ▽▽     | \triangledown | ▼▼     | \blacktriangledown | ⅁⅁     | \Game           |
| ◊◊     | \lozenge      | ⧫⧫     | \blacklozenge      | ★★     | \bigstar        |
| ∠∠     | \angle        | ∡∡     | \measuredangle     | ∢∢     | \sphericalangle |
| ╱╱     | \diagup       | ╲╲     | \diagdown          | ‵‵     | \backprime      |
| ∄∄     | \nexists      | ℲℲ     | \Finv              | ∅∅     | \varnothing     |
| ðð     | \eth          | ℧℧     | \mho               |        |                 |


