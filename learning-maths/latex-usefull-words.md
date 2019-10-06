# LaTeX数学符号总结（jupyter notebook）
本文链接：[https://blog.csdn.net/qq\_39232265/article/details/78868487][5]

## 1\. LaTeX 数学公式基础知识

LaTeX的强大之处在于对数学符号和公式的排版，所以jupyter notebook采用LaTeX来进行数学符号和公式的显示排版。  
首先，在jupyter notebook 里面，LaTeX数学公式用$$括起来。  
数学模式和文本模式又很多的不同之处。例如在数学模式中：

1.  空格和分行都会被忽略，所有的空格或是由数学表达式逻辑的衍生，或是由特殊命令如\\，\\quad或\\qquad来得到。空格可以用`&emsp;或者&nbsp;`表示
2.  不允许有空行，每个公式中只能有一个段落。
3.  每个字符都将被看作是一个变量名并以此来排版。

## 2\. 常用的排版命令

**分式**  
命令`\frac{a}{b}`形式：$\frac{a}{b}$
命令`\sum_{i=1}^n p_i`形式：∑i\=1npi\\sum\_{i=1}^n p\_i∑i\=1n​pi​

## 3\. 常用的数学模式命令

##### **1\. 数学模式重音符**

Symbol

Command

Symbol

Command

Symbol

Command

a^\\hat{a}a^

\\hat{a}

aˋ\\grave{a}aˋ

\\grave{a}

aˉ\\bar{a}aˉ

\\bar{a}

aˇ\\check{a}aˇ

\\check{a}

a˙\\dot{a}a˙

\\dot{a}

a⃗\\vec{a}a

\\vec{a}

a~\\tilde{a}a~

\\tilde{a}

a¨\\ddot{a}a¨

\\ddot{a}

A^\\widehat{A}A

\\widehat{A}

aˊ\\acute{a}aˊ

\\acute{a}

a˘\\breve{a}a˘

\\breve{a}

A~\\widetilde{A}A

\\widetilde{A}

##### **2\. 小写希腊字母**

Symbol

Command

Symbol

Command

Symbol

Command

α\\alphaα

\\alpha

θ\\thetaθ

\\theta

ooo

o

β\\betaβ

\\beta

ϑ\\varthetaϑ

\\vartheta

π\\piπ

\\pi

γ\\gammaγ

\\gamma

ι\\iotaι

\\iota

ϖ\\varpiϖ

\\varpi

δ\\deltaδ

\\delta

κ\\kappaκ

\\kappa

ρ\\rhoρ

\\rho

ϵ\\epsilonϵ

\\epsilon

λ\\lambdaλ

\\lambda

ϱ\\varrhoϱ

\\varrho

ε\\varepsilonε

\\varepsilon

μ\\muμ

\\mu

σ\\sigmaσ

\\sigma

ζ\\zetaζ

\\zeta

ν\\nuν

\\nu

ς\\varsigmaς

\\varsigma

η\\etaη

\\eta

ξ\\xiξ

\\xi

τ\\tauτ

\\tau

υ\\upsilonυ

\\upsilon

ϕ\\phiϕ

\\phi

φ\\varphiφ

\\varphi

χ\\chiχ

\\chi

ψ\\psiψ

\\psi

ω\\omegaω

\\omega

##### **3\. 大写希腊字母**

Symbol

Command

Symbol

Command

Symbol

Command

Γ\\GammaΓ

\\Gamma

Λ\\LambdaΛ

\\Lambda

Σ\\SigmaΣ

\\Sigma

Δ\\DeltaΔ

\\Delta

Ξ\\XiΞ

\\Xi

Υ\\UpsilonΥ

\\Upsilon

Θ\\ThetaΘ

\\Theta

Π\\PiΠ

\\Pi

Φ\\PhiΦ

\\Phi

Ψ\\PsiΨ

\\Psi

Ω\\OmegaΩ

\\Omega

##### **4\. 二元关系符**

Symbol

Command

Symbol

Command

Symbol

Command

&gt;&gt;\>

\>

&lt;&lt;<

<

\=\=\=

\=

≤\\leq≤

\\leq or \\le

≥\\geq≥

\\geq or \\ge

≡\\equiv≡

\\equiv

≪\\ll≪

\\ll

≫\\gg≫

\\gg

≐\\doteq≐

\\doteq

≺\\prec≺

\\prec

≻\\succ≻

\\succ

∼\\sim∼

\\sim

⪯\\preceq⪯

\\preceq

⪰\\succeq⪰

\\succeq

≃\\simeq≃

\\simeq

⊂\\subset⊂

\\subset

⊃\\supset⊃

\\supset

≈\\approx≈

\\approx

⊆\\subseteq⊆

\\subseteq

⊇\\supseteq⊇

\\supseteq

≅\\cong≅

\\cong

⊏\\sqsubset⊏

\\sqsubset

⊐\\sqsupset⊐

\\sqsupset

⋈\\Join⋈

\\Join

⊑\\sqsubseteq⊑

\\sqsubseteq

⊒\\sqsupseteq⊒

\\sqsupseteq

⋈\\bowtie⋈

\\bowtie

∈\\in∈

\\in

∋\\ni∋

\\ni or \\owns

∝\\propto∝

\\propto

⊢\\vdash⊢

\\vdash

⊣\\dashv⊣

\\dashv

⊨\\models⊨

\\models

∣\\mid∣

\\mid

∥\\parallel∥

\\parallel

⊥\\perp⊥

\\perp

⌣\\smile⌣

\\smile

⌢\\frown⌢

\\frown

≍\\asymp≍

\\asymp

:::

:

∉\\notin∈/​

\\notin

≠\\neq​\=

\\neq or \\ne

##### **5\. 二元运算符**

Symbol

Command

Symbol

Command

Symbol

Command

+++

+

−\-−

\-

±\\pm±

\\pm

∓\\mp∓

\\mp

◃\\triangleleft◃

\\triangleleft

⋅\\cdot⋅

\\cdot

÷\\div÷

\\div

▹\\triangleright▹

\\triangleright

×\\times×

\\times

∖\\setminus∖

\\setminus

⋆\\star⋆

\\star

∪\\cup∪

\\cup

∩\\cap∩

\\cap

∗\\ast∗

\\ast

⊔\\sqcup⊔

\\sqcup

⊓\\sqcap⊓

\\sqcap

∘\\circ∘

\\circ

∨\\vee∨

\\vee or \\lor

∧\\wedge∧

\\wedge or \\land

∙\\bullet∙

\\bullet

⊕\\oplus⊕

\\oplus

⊖\\ominus⊖

\\ominus

⋄\\diamond⋄

\\diamond

⊙\\odot⊙

\\odot

⊘\\oslash⊘

\\oslash

⊎\\uplus⊎

\\uplus

⊗\\otimes⊗

\\otimes

◯\\bigcirc◯

\\bigcirc

⨿\\amalg⨿

\\amalg

△\\bigtriangleup△

\\bigtriangleup

▽\\bigtriangledown▽

\\bigtriangledown

†\\dagger†

\\dagger

⊲\\lhd⊲

\\lhd

⊳\\rhd⊳

\\rhd

‡\\ddagger‡

\\ddagger

⊴\\unlhd⊴

\\unlhd

⊵\\unrhd⊵

\\unrhd

≀\\wr≀

\\wr

##### **6\. 大尺寸运算符**

Symbol

Command

Symbol

Command

Symbol

Command

∑\\sum∑

\\sum

⋃\\bigcup⋃

\\bigcup

⋂\\bigcap⋂

\\bigcap

⋁\\bigvee⋁

\\bigvee

⨁\\bigoplus⨁

\\bigoplus

∏\\prod∏

\\prod

⋀\\bigwedge⋀

\\bigwedge

⨂\\bigotimes⨂

\\bigotimes

∐\\coprod∐

\\coprod

⨆\\bigsqcup⨆

\\bigsqcup

⨀\\bigodot⨀

\\bigodot

∫\\int∫

\\int

∮\\oint∮

\\oint

⨄\\biguplus⨄

\\biguplus

##### **7\. 箭头**

Symbol

Command

Symbol

Command

Symbol

Command

←\\gets←

\\leftarrow or \\gets

⟵\\longleftarrow⟵

\\longleftarrow

↑\\uparrow↑

\\uparrow

→\\to→

\\rightarrow or \\to

⟶\\longrightarrow⟶

\\longrightarrow

↓\\downarrow↓

\\downarrow

↔\\leftrightarrow↔

\\leftrightarrow

⟷\\longleftrightarrow⟷

\\longleftrightarrow

↕\\updownarrow↕

\\updownarrow

⇐\\Leftarrow⇐

\\Leftarrow

⟸\\Longleftarrow⟸

\\Longleftarrow

⇑\\Uparrow⇑

\\Uparrow

⇒\\Rightarrow⇒

\\Rightarrow

⟹\\Longrightarrow⟹

\\Longrightarrow

⇓\\Downarrow⇓

\\Downarrow

⇔\\Leftrightarrow⇔

\\Leftrightarrow

⟺\\Longleftrightarrow⟺

\\Longleftrightarrow

⇕\\Updownarrow⇕

\\Updownarrow

↦\\mapsto↦

\\mapsto

⟼\\longmapsto⟼

\\longmapsto

↗\\nearrow↗

\\nearrow

↩\\hookleftarrow↩

\\hookleftarrow

↪\\hookrightarrow↪

\\hookrightarrow

↘\\searrow↘

\\searrow

↼\\leftharpoonup↼

\\leftharpoonup

⇀\\rightharpoonup⇀

\\rightharpoonup

↙\\swarrow↙

\\swarrow

↽\\leftharpoondown↽

\\leftharpoondown

⇁\\rightharpoondown⇁

\\rightharpoondown

↖\\nwarrow↖

\\nwarrow

⇌\\rightleftharpoons⇌

\\rightleftharpoons

&ThickSpace;⟺&ThickSpace;\\iff⟺

\\iff

⇝\\leadsto⇝

\\leadsto

##### **8\. 定界符**

Symbol

Command

Symbol

Command

Symbol

Command

(((

(

)))

)

↑\\uparrow↑

\\uparrow

\[\[\[

\[ or \\lbrack

\]\]\]

\] or \\rbrack

↓\\downarrow↓

\\downarrow

{\\{{

{ or \\lbrace

}\\}}

} or \\rbrace

↕\\updownarrow↕

\\updownarrow

⟨\\langle⟨

\\langle

⟩\\rangle⟩

\\rangle

⇑\\Uparrow⇑

\\Uparrow

$

$

\\vert

∥\\|∥

| or \\Vert

⇓\\Downarrow⇓

⌊\\lfloor⌊

\\lfloor

⌋\\rfloor⌋

\\rfloor

⇕\\Updownarrow⇕

\\Updownarrow

⌈\\lceil⌈

\\lceil

⌉\\rceil⌉

\\rceil

///

/

\\\\backslash\\

\\backslash

##### **9\. 大尺寸定界符**

Symbol

Command

Symbol

Command

Symbol

Command

⟮\\lgroup⟮

\\lgroup

⟯\\rgroup⟯

\\rgroup

⎰\\lmoustache⎰

\\lmoustache

⎱\\rmoustache⎱

\\rmoustache

KaTeX parse error: Expected 'EOF', got '\\arrowvert' at position 1: \\̲a̲r̲r̲o̲w̲v̲e̲r̲t̲

\\arrowvert

KaTeX parse error: Expected 'EOF', got '\\Arrowvert' at position 1: \\̲A̲r̲r̲o̲w̲v̲e̲r̲t̲

\\Arrowvert

KaTeX parse error: Expected 'EOF', got '\\bracevert' at position 1: \\̲b̲r̲a̲c̲e̲v̲e̲r̲t̲

\\bracevert

##### **10\. 其他符号**

Symbol

Command

Symbol

Command

Symbol

Command

…\\dots…

\\dots

⋯\\cdots⋯

\\cdots

⋮\\vdots⋮

\\vdots

⋱\\ddots⋱

\\ddots

ℏ\\hbarℏ

\\hbar

ı\\imathı

\\imath

ȷ\\jmathȷ

\\jmath

ℓ\\ellℓ

\\ell

ℜ\\Reℜ

\\Re

ℑ\\Imℑ

\\Im

ℵ\\alephℵ

\\aleph

℘\\wp℘

\\wp

∀\\forall∀

\\forall

∃\\exists∃

\\exists

℧\\mho℧

\\mho

∂\\partial∂

\\partial

′&#x27;′

’

′\\prime′

\\prime

∅\\emptyset∅

\\emptyset

∞\\infty∞

\\infty

∇\\nabla∇

\\nabla

△\\triangle△

\\triangle

□\\Box□

\\Box

◊\\Diamond◊

\\Diamond

⊥\\bot⊥

\\bot

⊤\\top⊤

\\top

∠\\angle∠

\\angle

√\\surd√

\\surd

♢\\diamondsuit♢

\\diamondsuit

♡\\heartsuit♡

\\heartsuit

♣\\clubsuit♣

\\clubsuit

♠\\spadesuit♠

\\spadesuit

¬\\neg¬

\\neg or \\lnot

♭\\flat♭

\\flat

♮\\natural♮

\\natural

♯\\sharp♯

\\sharp

##### **11\. 非数学符号**

Symbol

Command

KaTeX parse error: Expected 'EOF', got '\\S' at position 1: \\̲S̲

\\S

##### **12\. AMS定界符**

Symbol

Command

Symbol

Command

Symbol

Command

┌\\ulcorner┌

\\ulcorner

┐\\urcorner┐

\\urcorner

└\\llcorner└

\\llcorner

┘\\lrcorner┘

\\lrcorner

∣\\lvert∣

\\lvert

∣\\rvert∣

\\rvert

∥\\lVert∥

\\lVert

∥\\rVert∥

\\rVert

##### **13\. AMS希腊和希伯来字母**

Symbol

Command

Symbol

Command

Symbol

Command

ϝ\\digammaϝ

\\digamma

ϰ\\varkappaϰ

\\varkappa

ℶ\\bethℶ

\\beth

ℸ\\dalethℸ

\\daleth

ℷ\\gimelℷ

\\gimel

##### **14\. AMS二元关系符**

Symbol

Command

Symbol

Command

Symbol

Command

⋖\\lessdot⋖

\\lessdot

⋗\\gtrdot⋗

\\gtrdot

≑\\doteqdot≑

\\doteqdot or \\Doteq

⩽\\leqslant⩽

\\leqslant

⩾\\geqslant⩾

\\geqslant

≓\\risingdotseq≓

\\risingdotseq

⪕\\eqslantless⪕

\\eqslantless

⪖\\eqslantgtr⪖

\\eqslantgtr

≒\\fallingdotseq≒

\\fallingdotseq

≦\\leqq≦

\\leqq

≧\\geqq≧

\\geqq

≖\\eqcirc≖

\\eqcirc

⋘\\lll⋘

\\lll or \\llless

⋙\\ggg⋙

\\ggg or \\gggtr

≗\\circeq≗

\\circeq

≲\\lesssim≲

\\lesssim

≳\\gtrsim≳

\\gtrsim

≜\\triangleq≜

\\triangleq

⪅\\lessapprox⪅

\\lessapprox

⪆\\gtrapprox⪆

\\gtrapprox

≏\\bumpeq≏

\\bumpeq

≶\\lessgtr≶

\\lessgtr

≷\\gtrless≷

\\gtrless

≎\\Bumpeq≎

\\Bumpeq

⋚\\lesseqgtr⋚

\\lesseqgtr

⋛\\gtreqless⋛

\\gtreqless

∼\\thicksim∼

\\thicksim

⪋\\lesseqqgtr⪋

\\lesseqqgtr

⪌\\gtreqqless⪌

\\gtreqqless

≈\\thickapprox≈

\\thickapprox

≼\\preccurlyeq≼

\\preccurlyeq

≽\\succcurlyeq≽

\\succcurlyeq

≊\\approxeq≊

\\approxeq

⋞\\curlyeqprec⋞

\\curlyeqprec

⋟\\curlyeqsucc⋟

\\curlyeqsucc

∽\\backsim∽

\\backsim

≾\\precsim≾

\\precsim

≿\\succsim≿

\\succsim

⋍\\backsimeq⋍

\\backsimeq

⪷\\precapprox⪷

\\precapprox

⪸\\succapprox⪸

\\succapprox

⊨\\vDash⊨

\\vDash

⫅\\subseteqq⫅

\\subseteqq

⫆\\supseteqq⫆

\\supseteqq

⊩\\Vdash⊩

\\Vdash

⋐\\Subset⋐

\\Subset

⋑\\Supset⋑

\\Supset

⊪\\Vvdash⊪

\\Vvdash

⊏\\sqsubset⊏

\\sqsubset

⊐\\sqsupset⊐

\\sqsupset

∍\\backepsilon∍

\\backepsilon

∴\\therefore∴

\\therefore

∵\\because∵

\\because

∝\\varpropto∝

\\varpropto

ϝ\\digammaϝ

\\digamma

ϰ\\varkappaϰ

\\varkappa

ℶ\\bethℶ

\\beth

ϝ\\digammaϝ

\\digamma

ϰ\\varkappaϰ

\\varkappa

ℶ\\bethℶ

\\beth

##### **15\. AMS箭头**

Symbol

Command

Symbol

Command

Symbol

Command

⇠\\dashleftarrow⇠

\\dashleftarrow

⇢\\dashrightarrow⇢

\\dashrightarrow

⊸\\multimap⊸

\\multimap

⇇\\leftleftarrows⇇

\\leftleftarrows

⇉\\rightrightarrows⇉

\\rightrightarrows

⇈\\upuparrows⇈

\\upuparrows

⇆\\leftrightarrows⇆

\\leftrightarrows

⇄\\rightleftarrows⇄

\\rightleftarrows

⇊\\downdownarrows⇊

\\downdownarrows

⇚\\Lleftarrow⇚

\\Lleftarrow

⇛\\Rrightarrow⇛

\\Rrightarrow

↿\\upharpoonleft↿

\\upharpoonleft

↞\\twoheadleftarrow↞

\\twoheadleftarrow

↠\\twoheadrightarrow↠

\\twoheadrightarrow

↾\\upharpoonright↾

\\upharpoonright

↢\\leftarrowtail↢

\\leftarrowtail

↣\\rightarrowtail↣

\\rightarrowtail

⇃\\downharpoonleft⇃

\\downharpoonleft

⇋\\leftrightharpoons⇋

\\leftrightharpoons

⇌\\rightleftharpoons⇌

\\rightleftharpoons

⇂\\downharpoonright⇂

\\downharpoonright

↰\\Lsh↰

\\Lsh

↱\\Rsh↱

\\Rsh

⇝\\rightsquigarrow⇝

\\rightsquigarrow

↫\\looparrowleft↫

\\looparrowleft

↬\\looparrowright↬

\\looparrowright

↭\\leftrightsquigarrow↭

\\leftrightsquigarrow

↶\\curvearrowleft↶

\\curvearrowleft

↷\\curvearrowright↷

\\curvearrowright

↺\\circlearrowleft↺

\\circlearrowleft

↻\\circlearrowright↻

\\circlearrowright

##### **16\. AMS二元否定关系符和箭头**

Symbol

Command

Symbol

Command

Symbol

Command

≮\\nless≮

\\nless

≯\\ngtr≯

\\ngtr

\\varsubsetneqq

\\varsubsetneqq

⪇\\lneq⪇

\\lneq

⪈\\gneq⪈

\\gneq

\\varsupsetneqq

\\varsupsetneqq

≰\\nleq≰

\\nleq

≱\\ngeq≱

\\ngeq

\\nsubseteqq

\\nsubseteqq

\\nleqslant

\\nleqslant

\\ngeqslant

\\ngeqslant

\\nsupseteqq

\\nsupseteqq

≨\\lneqq≨

\\lneqq

≩\\gneqq≩

\\gneqq

∤\\nmid∤

\\nmid

\\lvertneqq

\\lvertneqq

\\gvertneqq

\\gvertneqq

∦\\nparallel∦

\\nparallel

\\nleqq

\\nleqq

\\ngeqq

\\ngeqq

\\nshortmid

\\nshortmid

⋦\\lnsim⋦

\\lnsim

⋧\\gnsim⋧

\\gnsim

\\nshortparallel

\\nshortparallel

⪉\\lnapprox⪉

\\lnapprox

⪊\\gnapprox⪊

\\gnapprox

≁\\nsim≁

\\nsim

⊀\\nprec⊀

\\nprec

⊁\\nsucc⊁

\\nsucc

≆\\ncong≆

\\ncong

⋠\\npreceq⋠

\\npreceq

⋡\\nsucceq⋡

\\nsucceq

⊬\\nvdash⊬

\\nvdash

⪵\\precneqq⪵

\\precneqq

⪶\\succneqq⪶

\\succneqq

⊭\\nvDash⊭

\\nvDash

⋨\\precnsim⋨

\\precnsim

⋩\\succnsim⋩

\\succnsim

⊮\\nVdash⊮

\\nVdash

⪹\\precnapprox⪹

\\precnapprox

⪺\\succnapprox⪺

\\succnapprox

⊯\\nVDash⊯

\\nVDash

⊊\\subsetneq⊊

\\subsetneq

⊋\\supsetneq⊋

\\supsetneq

⋪\\ntriangleleft⋪

\\ntriangleleft

\\varsubsetneq

\\varsubsetneq

\\varsupsetneq

\\varsupsetneq

⋫\\ntriangleright⋫

\\ntriangleright

⊈\\nsubseteq⊈

\\nsubseteq

⊉\\nsupseteq⊉

\\nsupseteq

⋬\\ntrianglelefteq⋬

\\ntrianglelefteq

⫋\\subsetneqq⫋

\\subsetneqq

⫌\\supsetneqq⫌

\\supsetneqq

⋭\\ntrianglerighteq⋭

\\ntrianglerighteq

↚\\nleftarrow↚

\\nleftarrow

↛\\nrightarrow↛

\\nrightarrow

↮\\nleftrightarrow↮

\\nleftrightarrow

⇍\\nLeftarrow⇍

\\nLeftarrow

⇏\\nRightarrow⇏

\\nRightarrow

⇎\\nLeftrightarrow⇎

\\nLeftrightarrow

##### **17\. AMS二元运算符**

Symbol

Command

Symbol

Command

Symbol

Command

∔\\dotplus∔

\\dotplus

⋅\\centerdot⋅

\\centerdot

⊺\\intercal⊺

\\intercal

⋉\\ltimes⋉

\\ltimes

⋊\\rtimes⋊

\\rtimes

⋇\\divideontimes⋇

\\divideontimes

⋓\\Cup⋓

\\Cup or \\doublecup

⋒\\Cap⋒

\\Cap or \\doublecap

∖\\smallsetminus∖

\\smallsetminus

⊻\\veebar⊻

\\veebar

⊼\\barwedge⊼

\\barwedge

⩞\\doublebarwedge⩞

\\doublebarwedge

⊞\\boxplus⊞

\\boxplus

⊟\\boxminus⊟

\\boxminus

⊝\\circleddash⊝

\\circleddash

⊠\\boxtimes⊠

\\boxtimes

⊡\\boxdot⊡

\\boxdot

⊚\\circledcirc⊚

\\circledcirc

⋋\\leftthreetimes⋋

\\leftthreetimes

⋌\\rightthreetimes⋌

\\rightthreetimes

⊛\\circledast⊛

\\circledast

⋎\\curlyvee⋎

\\curlyvee

⋏\\curlywedge⋏

\\curlywedge

##### **18\. AMS其它符号**

Symbol

Command

Symbol

Command

Symbol

Command

ℏ\\hbarℏ

\\hbar

ℏ\\hslashℏ

\\hslash

k\\Bbbkk

\\Bbbk

□\\square□

\\square

■\\blacksquare■

\\blacksquare

Ⓢ\\circledSⓈ

\\circledS

△\\vartriangle△

\\vartriangle

▲\\blacktriangle▲

\\blacktriangle

∁\\complement∁

\\complement

▽\\triangledown▽

\\triangledown

▼\\blacktriangledown▼

\\blacktriangledown

⅁\\Game⅁

\\Game

◊\\lozenge◊

\\lozenge

⧫\\blacklozenge⧫

\\blacklozenge

★\\bigstar★

\\bigstar

∠\\angle∠

\\angle

∡\\measuredangle∡

\\measuredangle

∢\\sphericalangle∢

\\sphericalangle

╱\\diagup╱

\\diagup

╲\\diagdown╲

\\diagdown

‵\\backprime‵

\\backprime

∄\\nexists∄

\\nexists

Ⅎ\\FinvℲ

\\Finv

∅\\varnothing∅

\\varnothing

ð\\ethð

\\eth

℧\\mho℧

\\mho
