# kinematic
!!! tip "newton law of intertia (n1l)"
	Mass resist a change in motion (object moves at constant speed or stay still (unless acted by external net force) <- n2l)
## 1D motion (linear)
### const acceleration
derive suvat equation

$$
\begin{align}
\frac{dv}{dt} &\triangleq a  \\
v &= \int adt \\
v &= at + u \quad (0,u) \\
\end{align}
$$

!!! note
    $v = u + at \quad (1)$

$$
\begin{align}
\frac{ds}{dt} &\triangleq v \\
s &= \int u + at dt \\
s &= ut + \frac{1}{2}at^{2} + s_{i} \quad (0,s_{i})\\
\end{align}
$$

!!! note
    $s = s_i + ut + \frac{1}{2}at^2 \quad (2)$

$$
\begin{align}
(1) \Rightarrow s &= s_i + (v-at)t + \frac{1}{2}at^{2} \\
s &= s_i + vt - \frac{1}{2}at^{2}
\end{align}
$$

!!! note
    $s = s_i + vt - \frac{1}{2}at^2 \quad (2.1)$

$$
\begin{align}
 & (1) \quad t = \frac{v-u}{a} \\ \\
 & (2) \quad s = s_{i} + u\left( \frac{v-u}{a} \right) + \frac{1}{2}a \left( \frac{v-u}{a} \right)^{2} \\ \\
\end{align}
$$

$$
\begin{align}
 \Rightarrow \quad & 2a(s - s_{i}) = 2u(v-u) + (v-u)^{2} \\
 & 2a \Delta s = - u^{2} + v^{2}\\ \\
& v^{2} = u^{2} + 2a\Delta{s}
\end{align}
$$

!!! note
    $v^{2} = u^{2} + 2a\Delta{s} \quad (3)$

!!! note
	$s = (\frac{u+v}{2})t \quad (4)$ trapezium area on a $v=u + at$ graph

### var acceleration
use $\int ,  \frac{d}{dx}$ to find the equation of $v, s, a$ when given one of them and sub in the right $t$
## 2D motion or 3D motion (linear)

two/three perpendicular 1D motions => 2D/3D motion.

- [x] [projectiles](1-projectile) closely related to freefall
- [circular motion](2-circular)
- [oscillation](3-oscillation)
# rotational motion