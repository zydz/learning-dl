# Features of Typora

This is an example for how to write with Typora

------

### Table of Contents

[TOC]

### Basic

- Heading
- Emphasis
- Hype-link
- Code Fences
- List
  - ordered List
  - unordered List
- Task List
  - Completed 
  - To Do
- Table
- Table of Content
- Image



### Maths

$$
- \frac{\hbar^2}{2\mu}\frac{\partial^2\Psi(x,t) }{\partial x^2} 
+ U(x,t)\Psi(x,t) = i\hbar \frac{\partial\Psi(x,t)}{\partial t}
$$



### Sequence

```sequence
Andrew->China: Says Hello 
Note right of China: China thinks\nabout it 
China-->Andrew: How are you? 
Andrew->>China: I am good thanks!
Note left of Andrew: Aha....
```

### Flow

```flow
st=>start: Start:>http://www.google.com[blank]
e=>end:>http://www.google.com
op1=>operation: My Operation
sub1=>subroutine: My Subroutine
cond=>condition: Yes
or No?:>http://www.google.com
io=>inputoutput: catch something...
para=>parallel: parallel tasks

st->op1->cond
cond(yes)->io->e
cond(no)->para
para(path1, bottom)->sub1(right)->op1
para(path2, top)->op1
```

