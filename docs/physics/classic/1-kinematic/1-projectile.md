# projectile

For projectile:

- $x: \ F_{d} \ \text{is negligible} \ \Sigma F = 0\Rightarrow a=0$ 
- $y: \Sigma F = -W \Rightarrow a = -g$
## equation of projectile
$$
\begin{align}
& x = u_{x}t \\ \\
& t = \frac{x}{u_{x}} \qquad (1) \\ \\
y &  = u_{y}t + \frac{1}{2}a_{y}t^{2} \\
 & = \frac{u_{y}x}{u_{x}} + \frac{a_{y}x^{2}}{2u_{x}^{2}} \\
 & = \frac{a_{y}}{2u_{x}^{2}}x^{2} + \frac{u_{y}}{u_{x}}x  \\ \\
y & = x \left( \frac{a_{y}}{2u_{x}^{2}}x + \frac{u_{y}}{u_{x}}  \right) \qquad (2)
\end{align} 
$$

!!! note
	since $a_{y}, \vec{u} \ \text{or} \  \theta$ are not funciton of x $\therefore$ a parabola.

 ![](https://i.imgur.com/fCA81VC.png)

$$
\vec{s}= \begin{pmatrix}
u_{x}t \\
u_{y}t + \frac{1}{2}a_{y}t^{2}
\end{pmatrix}
$$

$$
\vec{v} = \begin{pmatrix}
u_{x} \\
u_{y} + a_{y}t
\end{pmatrix}
$$

$$
\vec{a} = \begin{pmatrix}
0 \\
a_{y}
\end{pmatrix}
$$

!!! tip
	to $\int / \frac{d}{dx}$ a vector, perform the operation on all components of the vector individually. The $+ \vec{c}$ can also be found by using boundary condition $(\text{time}, \overrightarrow{\text{quantity}})$

where

$$\vec{u}= \begin{pmatrix} u\cos \theta \\
u\sin \theta
\end{pmatrix}$$

finding $\theta$ at any $t$

$$\tan\theta = \frac{u_{y}}{u_{x}}$$

max height ($\text{y-axis}$)

$$
\begin{align} \\
 & v  = 0 \\
 & u+at   = 0 \\ \\
 & t  = -\frac{u}{a} \\
\end{align}
$$

!!! note "important points"
	- time to max height: $t = -\frac{u_{y}}{a_{y}}$ 
	- max height position: $\vec{s}\left( -\frac{u_{y}}{a_{y}} \right)$
	- range: $x\left( -\frac{2u_{y}}{a_y} \right)$
## multiple bounce
requires [collision](../../2-dynamic/5-collision/)