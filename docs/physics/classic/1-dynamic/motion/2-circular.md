# circular motion
## kinematic

!!! tip "preliminary: rotational motion (angular motion)"
	- $\frac{d\theta}{dt}\triangleq\omega$ which is angular velocity here not angular frequency
	- $\frac{d\omega}{dt} \triangleq \alpha$

For a general cirucular motion, assume $O$ at centre. Consider $\hat{r}(\theta)$ (radius) and $\hat{t}(\theta)$ (tangent) as the rotation of the xy plane in which we will work on. (MAY DRAW DIAGRAM TO SHOW THE r hat and t hat)

$$\begin{align}
 & \hat{r}\triangleq\begin{pmatrix}\cos \theta \\ \sin \theta\end{pmatrix} \> \quad \hat{t}\triangleq \begin{pmatrix}-\sin \theta \\ \cos \theta \end{pmatrix} \\ \\
\text{notice}:\quad & \dot{\hat{r}} = \omega\overbrace {\begin{pmatrix}-\sin \theta \\ \cos \theta \end{pmatrix}}^{\hat{t}} \quad \dot{\hat{t}}=\omega\overbrace{\begin{pmatrix}-\cos \theta \\ -\sin \theta \end{pmatrix}}^{-\hat{r}}\\ \\
\Rightarrow \quad & \vec{s}  \triangleq r\hat{r} \\
 & \vec{v} =\omega r \hat{t} \\
 & \vec{a}= -\omega^{2}r\hat{r} +\alpha r\hat{t} \\ \\
\therefore \quad  & s =r \quad v=\omega r \quad a_{r} = \omega^{2}r \quad a_{t} = \alpha r
\end{align}$$
!!! note "two case of circular motion"
	- uniform
	- non-uniform 

we have discovered that $\alpha$ determine the $a_{t}$ and can be use to observe the two cases of circular motion:

$$\begin{align}
 & \alpha = 0 , \ a_{t}=0 & \Rightarrow   & \quad  v = k   & \quad \text{uniform}\\
 & \alpha = k , \ a_{t}=k & \Rightarrow  & \quad  v = u + (\alpha r)t &  \quad  \text{non-uniform} \\
 & \text{otherwise} & \Rightarrow  & \quad v = v_{i} + \int (\alpha r) \ dt  & \quad \text{non-uniform}
\end{align}$$
## dynamic
by $\text{n2l}$ multiplying mass of the mass in motion on both sides:

- $F_{r} = mw^{2}r = \frac{mv^{2}}{r}$
- $F_{t}=m\alpha r$
