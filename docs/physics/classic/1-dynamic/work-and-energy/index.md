---
weight: -1
---
# work

!!! info
	- external work: when system excert a force to its surrounding causing a displacement (when we say something doing work, we generally means external work)
	- internal work: when part of system excert a force to another part of system, causing a displacement
	- energy is...
	- abstract and cannot always be perceived
	- given meaning through calculation
	- a central concept in science

When work is done on a mass, it changes the state of energy of that system. We have define force as the only interaction that could change the motion of object. If we apply force to the surrounding and cause masses to displace, then work must have been done to the surrounding.

!!! info
	A force can only affect motion in the same direction (sometimes we need to break down forces into two perpendicular components, rotating the xy-axis).
	!!! example ""
		veritcal force can only affect vertical motion and horizontal force can only affect horizontal motion. 
	!!! example
		a mass moving right but has a force acting upward means no work is done (system is still in dynamic equilibrium).

based from the observation:

$$\begin{align}
 \text{when F and s are on the same line}:  \quad &  \mathcal{W} \triangleq Fs \quad  \\
\text{when F and s depend on time}: \quad  & \mathcal{W} \triangleq \int \vec{F} \cdot \vec{ds} \quad
\end{align}$$

## work-energy theorem
!!! tip
	- Work causes a change in energy
	- Work can shifts energy from one system to another or change their form
$$\begin{align}
\text{since }   \quad  & \mathcal{W} \triangleq \Delta E \\  \\
\text{if}:\quad & \mathcal{W}<0 \quad \text{work is done by the system/system lose energy} \\
\text{else if}: \quad  & \mathcal{W} > 0 \quad \text{work is done on the system/system gain energy} \\
\text{otherwise}: \quad &  \mathcal{W}= 0 \quad \text{no work is done}
\end{align}$$

!!! tip "cme (4)"
	"The law of conservation of energy cannot be derived. Energy is not concrete; it is not a material substance; it is given meaning through the calculation of numbers. A true historical discussion of the law of conservation of energy is best left to the chapters in this book devoted to thermodynamics. The 19th century law of conservation of energy of Mayer and von Helmholtz (and Clausius, Carnot, Rumford, Kelvin, and maybe some more). For now, just take it as a really good idea."
!!! tip
	$$P \triangleq \dot{\mathcal{W}}$$
$$\begin{align}
P &  \triangleq \frac{d\mathcal{W}}{dt} \\
 & =\frac{d}{dt}\int F \cdot ds \\
 & = \frac{d}{dt} \int F \cdot \frac{ds}{dt} dt \\
 & = F \cdot v
\end{align}$$

## machine

!!! note
	Machines are devices that takes in Force (effort) and convert this force to Force (load/output) somehow and somewhere

$$\begin{align}
\text{effort: } \quad\mathcal{W_{in}} &  = F\cdot s \quad\text{on machine}\\ 
\text{output:} \quad \mathcal{W_{out}} & = F \cdot s \quad \text{by machine}\\ \\
\text{Ideally (cme)}:\quad \mathcal{W_{in}} & = \mathcal{W_{out}}  \\
	\text{real}: \quad \mathcal{W_{in}} &  > \mathcal{W_{out}} \\
\text{so efficiency}: \quad \eta  & =\frac{\mathcal{W_{out}}}{\mathcal{W_{in}}} = \frac{Fs_{load}}{Fs_{effort}}\\
 & = \frac{P_{out}}{P_{in}} = \frac{Fv_{load}}{Fv_{effort}} \\
\end{align}$$