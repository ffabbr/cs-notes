	
- **Ordnung einer Gruppe:** 
  Anzahl Elemente in der Gruppe (ist eine Zahl oder $\infty$)

- **Ordnung eines Elementes:** 
  Wie oft man ein Element mit sich selbst verknüpfen muss, damit das neutrale Element entsteht. Also $a^{\text{ord}(a)}=e$. Wenn das nicht möglich ist, dann unendlich. 
  
  $\text{ord(a ∈ G)}=\min \{\, n \geq 1 \mid a^n = e \,\} \cup \{ \infty \}$, 

- **Lagrange**. H ist eine Untergruppe von G (endlich). Es gilt |H| teilt |G|.
- Die ==Ordnung des Generators muss gleich der Gruppenordnung sein== (bei endlichen Gruppen)
- $g^{|G|}=e$ für alle $g \in G$. Also "irgendwas hoch die Gruppenordnung ist das neutrale Element". Das gilt, da ein Element eine zyklische Untergruppe erstellt, also ==die Ordnung eines Elements teilt die Ordnung der Gruppe==. Dann auch $g^{|G|+1}=g$. 

- Beispiele (Operation Addition)
	- $|\mathbb{Z}_{7}|=7$, und $\text{ord(1)}=7, \text{ord(2)}=7$ 
		- $|\mathbb{Z}_{7}|=7$, weil es 7 Restklassen bei mod 7 gibt, also 0,1,2,3,4,5,6
	- $|\mathbb{Z}_{7}^{*}|=6$, Anzahl Teilerfremd
	- $|\mathbb{Z}_{2} \times \mathbb{Z}_{2}|= |\{(0,0), (0,1), (1,0), (1,1)\}|=4$, und $\text{ord(1,1)}=2$
	- $|\mathbb{Z}|=\infty$, und $\text{ord(1)}=\infty$
	- $|\mathbb{Z}_{p}^{*}|=p-1$, wenn p eine **Primzahl**. In dem Fall $\mathbb{Z}_7^*=\{1,2,3,4,5,6\}$
	- Siehe [[04 Euler]] 

- In einer endlichen Gruppe hat jedes Element eine endliche Ordnung. 
	- Vorstellung: wenn ich a wiederholt mit a verknüpfe bis ich das neutrale Element bekomme, dann muss ich ja irgendwann im Kreis laufen, da ich nur endlich viele Elemente habe in der Gruppe. Also z.B. $a$ → $a^2$ → $a^3$ → $a^4$, und z.B. ist $a^2=a^4$. 
	- Wir haben also $$\begin{align}
a^r&=a^s\ \text{mit}\ r<s \\
(a^{-r})*a^r&=(a^{-r})*a^s \\
e &= a^{s-r} \\
\text{ord(a)} & \leq s-r
\end{align}$$
![[Pasted image 20251120151759.png]]