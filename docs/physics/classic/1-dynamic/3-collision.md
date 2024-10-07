# collision
## collision type

### coefficient of restitution
??? abstract
	the word restitution meaning giving something back. In this case, we are trying to describe the energy after collision relative to before.
	
	![](https://i.imgur.com/uuuLa1w.png)


!!! note
	Kinetic energy of a system depend on change in velocity of all the masses.

If mass A, B collides, then they must have approach -> collide -> separate. We can set A as the **inertial reference frame**. $v_{a'}, v_{b'}$ represent the relative velocity. 

$$\begin{align}
 & v_{a'} \triangleq 0 \quad \forall t \quad\Rightarrow \quad v_{b'} \triangleq v_{b} - v_{a} \\
 & v_{b'} \text{ is the relative velocity of b approaching a}  \\
 &  e \triangleq \frac{-v_{b'}}{u_{b'}} \equiv \frac{\text{separating speed}}{\text{approaching speed}}  \\
 & \ \ \equiv -\frac{v_{b}-v_{a}}{u_{b}-u_{a}}
\end{align}$$

!!! tip
	One of $v_{a}$ or $v_{b}$ has to be negative because, initially, they must **approach** each other. we set the direction of $v_{a} \triangleq -$ so that $v_{b} \triangleq +$ , hence $v_{b'}=v_{b}-v_{a}$

??? note "what is e (cor)?"
	$e$ is a ratio where multiplying it to the negative of the approaching speed gives the speed of the separation. It quantifies the elasticity of a collision and give insight to energy conservation of the collision.

Since, $v_{b'}$ is the *only* changing velocity in this reference frame 

$$\begin{align}
 & \Delta K = \frac{1}{2}m_{b}(v_{b'}^{2}-u_{b'}^{2}) \\
 &  K_{i} = \frac{1}{2}m_{b}u_{b'}^{2} = \text{total }E_{system}
\end{align}$$

$$\begin{align}
\text{if} \quad &  v_{b'} = -u_{b'} &  e = 1 \quad\Rightarrow \quad & \Delta K = 0  \quad  &   \text{elastic} \\
 & 0 < |-v_{b'}| < u_{b'}  &  e\in(0,1) \quad \Rightarrow \quad & \Delta K < 0  \quad  & \text{inelastic} \\
 \quad &  v_{b'} = 0  & e= 0  \quad \Rightarrow \quad  & \Delta K = -K_{i} \quad & \text{perfectly inelastic} 
\end{align}$$

??? question "a superelastic collision?!"
	It's fictional type of collision which release potential energy on impact. No need to 

??? note "interpreting $\Delta K = -K_{i}$"
	kinetic energy has been reduce by $K_{i}$ which is the total energy that the system has originally, therefore, it must have stopped moving $v_{a}=v_{b}=0$.


