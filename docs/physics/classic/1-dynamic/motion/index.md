---
weight: -3
---
# motion
???+ tip "type of motion"
	- translational motion (linear)
	- rotational motion (angular)
	- oscillatory motion (could be linear or angular)
	- random motion (chaos theory, quantum theory)

## translational motion

## rotational motion
Most of rotational motion is an analouge of translational motion onto angular values. So $d \ sv_{0}vat \ F \ m p \mapsto r \ \theta \omega_{0} \omega \alpha t \  \tau \ I L$ respectively.

!!! tip
	Rotational motion is periodic(!link to page...) $\theta\equiv\theta \pm(2\pi)k$
	
	<iframe width="500" height="300" src="https://www.youtube.com/embed/erA0jb9dSm0" title="How to rotate in higher dimensions? Complex dimensions? | Lie groups, algebras, brackets #2" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
	
!!! tip "connection between rotation and translation"
	$$\begin{align}
	 & \text{arc length} = \theta r \\
	 & s = r\hat{r} \qquad \text{point in a circle}\\
	 & v =  \omega r \\
	 & \vec{a} = -\omega^{2}r\hat{r} + \alpha r\hat{t} \\ 
	  & \tau = F \times s \\
	\text{coordinate system}: \quad & \vec{s} = \langle x, y, z \rangle  \\
	 & \ \ = r\langle \cos \theta,\sin \theta,\dots?\rangle \text{TBC when learn more} \\
	 & r^{2} =x^{2} + y^{2} +z^{2} +\dots  \\
	 & \theta = \pm\tan ^{-1}(y / x) \qquad \theta \in \left( -\frac{\pi}{2}, \frac{\pi}{2}\right)
	\end{align}$$

	- all one dimensional motion of rotational motion are analouge to translation motion, as it is define in a similar way by ODE. Even work, power, potential energy and kinetic energy $K =\frac{1}{2}I\omega^{2}$

![](https://i.imgur.com/LKSry79.png)
### rolling
## special type of motion
- projectile (parabola: 2D linear)
- circular motion (Circle: 2D oscillatory)
- SHM (oscillatory)

!!! info "[symmetry](https://physics.info/displacement/)"
	"How we view the world does not change distance and displacement. A symmetric operation does not change the input. Quantities that are not affected by a change are said to show a symmetry.
	
	- The location of the observer does not matter so orgin can be placed anywhere $O \ (0,0)$. Distance and displacement are not affected by a translation of the origin. Space is homogeneous.
	- the orientation of the axes is irrelevant, BUT $\text{xyz-axis must always be } \perp$. Distance and displacement are not affected by a rotation of the axes. All directions are equivalent. Space is isotropic.
	- the chirality or handedness of the coordinate system is also irrelevant. $\text{x-axis } \rightarrow \text{ y-axis } \uparrow$. choosing $\text{z-axis}$ in or out of the page create a right-hand or left-hand coordinate system. The two possible coordinate systems are like hands because they are mirror images of one another.
	
	Distance and displacement are not affected by a reflection of the coordinate system. This is not true for all physical quantities, however. The ones that don't work the same when viewed in a mirror are called pseudovectors (e.g. [torque](https://physics.info/rotational-dynamics/), [angular momentum](https://physics.info/rotational-momentum/) or spin, and [magnetic field](https://physics.info/electromagnetism/)).
	
	The direction of a pseudovector is always related to a hand rule of some sort (like the one used in [vector multiplication](https://physics.info/vector-multiplication/)). But as we have just discussed and as everyone knows, right hands become left hands and left hands become right hands when viewed in a mirror. Wrong hand means wrong direction. Space appears to know the difference between left and right for some quantities."


## not organise
### 1D linear motion
!!! warning "convention"
	$\to$ and $\uparrow$ are positive 
#### no acceleration
!!! note
	$s \triangleq vt$
#### const acceleration
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

#### var acceleration
use $\int ,  \frac{d}{dt}$ to find the equation of $v, s, a$ when given one of them and sub in the right $t$
## 1D rotational motion

!!! warning "convention"
	$\curvearrowleft$ is positive


!!! warning "frequency and period (beware unit)"
	$$f  \triangleq \frac{1}{T} \quad \text{complete "something" per second}$$
	
	- rps, fps, cps ... or Hz 
	- $1 \mathrm{\ rev} = 2\pi \ \mathrm{rad}$

!!! tip
	use the boundary condition $(t, \theta) = (T, 2\pi)$ or $(f, \frac{1}{2\pi})$

### no acceleration

!!! note
	$\theta \triangleq \omega t$

!!! note
	- $\omega = \frac{2\pi}{T}$
	- $\omega = 2\pi f$

### const acceleration
$\theta \omega_{i} \omega \alpha t$ is the $suvat$ equation for angular quantity. Deriving them follow the same pattern.

- $\frac{d\theta}{dt}\triangleq\omega$
- $\frac{d\omega}{dt} \triangleq \alpha$$\frac{d\theta}{dt}\triangleq\omega$
- $\frac{d\omega}{dt} \triangleq \alpha$

!!! note
	- $\omega = \omega_{i} + \alpha t \quad (1)$
	- $\theta = \theta_i + \omega_{i}t + \frac{1}{2}\alpha t^2 \quad (2)$
	- $s = s_i + vt - \frac{1}{2}at^2 \quad (2.1)$
	- $\omega^{2} = \omega_{i}^{2} + 2\alpha\Delta{\theta} \quad (3)$
	- $s = (\frac{u+v}{2})t \quad (4)$
	

### var acceleration
use $\int ,  \frac{d}{dt}$ to find the equation of $\theta, \omega, \alpha$ when given one of them and sub in the right $t$

## 2D motion or 3D motion
!!! note
	- two/three $\perp$ linear 1D motions => 2D/3D motion
	- one/two $\perp$ rotational 1D motion => 2D/3D motion