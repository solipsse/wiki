# circular motion

!!! note "preliminary: [rotational motion](../4-rotation) (angular motion)"
	- $\theta = \omega t$ => a function of time
	- $\frac{d\theta}{dt}\triangleq\omega$
	- $\frac{d\omega}{dt} \triangleq \alpha$ (not on physic syllabus)
	- const $r$
## const speed (uniform)
- horizontal circular motion xz-plane
!!! tip 
	- $\Delta\vec {v}$ : direction only
	- $\theta(t) \ \text{is linear}, \ \text{const} \ \omega \ ,\ \alpha = 0$


$$
\begin{align}
 \vec{s} &  \triangleq r\begin{pmatrix} 
\cos \theta \\
\sin \theta
\end{pmatrix} \\ \\
\vec{v} &  \equiv \omega r\begin{pmatrix}
-\sin \theta \\
\cos \theta
\end{pmatrix} \qquad \frac{d}{dt}\\ \\ 
\vec{a} &  \equiv -\omega^{2}r\begin{pmatrix}
\cos \theta \\
\sin \theta
\end{pmatrix}\qquad \frac{d}{dt}\\  \\
 \\
\Rightarrow  \vec{a} & \equiv -\omega^{2} \vec{s} \quad \Rightarrow \text{equation for SHM}
\end{align}
$$

- $\vec{s}$ points on the circumference of the circle from the center $O$
- $\vec{a}$ act opposite to $\vec{s}$ hence it is center seeking => centripedalacceleration ($a_{c}$)

!!! note
	$\sqrt{ \sin ^{2}\theta + \cos ^{2}\theta } = 1 \quad (1)$ 
## magnitude equation
$$
\begin{align}
(1) \Rightarrow s & \equiv r \qquad \text{this shouldn't be surprising} \\ \\ 
v &  \equiv \omega r \\ \\ 
a_{c}  & \equiv \omega^{2}r \\
 & \equiv \frac{v^{2}}{r} \\ \\
 ma_{c}&= \frac{mv^{2}}{r} \\
F_{c} & \equiv \frac{mv^{2}}{r} \qquad \text{}
\end{align}
$$

- $F_{c}$ is the minimum force requires to produce the $a_c$ which keeps particle in circular motion with const speed ($v$)
### connected particle
- conical pendulum
### reaction and/or friction
- car turning (banking)
- "wall running"

## var speed (non-uniform)
- vertical motion (xy-plane)
!!! tip
	- $\Delta\vec {v}$ : direction and speed
	- const $r$
	- $\theta(t) \ \text{is not linear}, \ \text{var} \ \omega (t) ,\ \text{ var }\alpha (t)$

$$
\begin{align}
 \vec{s} &  \triangleq r\begin{pmatrix} 
\cos \theta \\
\sin \theta
\end{pmatrix} \\ \\
\vec{v} &  \equiv \omega \ r\begin{pmatrix}
-\sin \theta \\
\cos \theta
\end{pmatrix} \qquad \frac{d}{dt}\\ \\ 
\vec{a} &  = \omega\left(\omega \ r\begin{pmatrix}
-\cos \theta \\
-\sin \theta
\end{pmatrix}\right) + \alpha \ r\begin{pmatrix}
-\sin \theta \\
\cos \theta
\end{pmatrix}\qquad \frac{d}{dt} \ \text{product rule}\\
 & \equiv \underbrace{-\omega^{2}r\begin{pmatrix} 
\cos \theta \\
\sin \theta
\end{pmatrix}}_{\quad \text{centripedal component} \quad } + \underbrace{\alpha r\begin{pmatrix}
-\sin \theta \\
\cos \theta
\end{pmatrix} }_{\quad \text{tangential component} \quad}\\ \\
\vec{a} & \equiv -\omega^{2} \vec{s} + \alpha \vec{v} \\
\end{align}
$$
### magnitude equation

$$
\begin{align}
(1) \Rightarrow s & \equiv r \qquad \text{the same thing} \\ \\ 
v &  \equiv \omega r \\ \\   & \text{we are able to split acceleration into a two} \perp \text{components} \ \vec{a_{c}}\cdot  \vec{a_{t}} = 0 \\  \\ \
\Rightarrow \quad a_{c}  & \equiv \omega^{2}r \\
 & \equiv \frac{v^{2}}{r} \\ \\
\text{n2l:} \quad F_{c} & \equiv \frac{mv^{2}}{r} \qquad \text{} \\ \\
\Rightarrow \quad a_{t}  & \equiv \alpha r \\ \\
\text{n2l:} \quad F_{t} & \equiv m\alpha r \qquad \text{}
\end{align}
$$