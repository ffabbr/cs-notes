## Quick-Facts

- $A^{^\dagger}=R^{^\dagger} C^{^\dagger}=R^{\top} (C^{\top} A R^{\top})^{-1} C^{\top}$
- $(A^\top)^\dagger=(A^\dagger)^\top$
- NUR wenn wir einmal vollen Spaltenrang und einmal vollen Zeilenrang haben gilt $(CR)^\dagger=R^\dagger C^\dagger$

---

- $AA^+A = A$
- $A^+AA^+ = A^+$   
- $(AA^+)^T = AA^+$ (Symmetrie)
- $(A^+A)^T = A^+A$ (Symmetrie)

---

## Formeln

#### Linksinverse bei vollem Spaltenrang

$A^\dagger=(A^\top A)^{-1}A^\top$
$A^\dagger A=I$

#### Rechtsinverse bei vollem Zeilenrang

$A^\dagger=A^\top (AA^\top)^{-1}$
$AA^\dagger=I$

#### Pseudoinverse

**[[Zerlegungen und Gram Schmidt#CR-Zerlegung|CR-Zerlegung]] durchführen** 
$$
A^\dagger=R^\dagger C^\dagger
$$
C voller Spaltenrang, 
R voller Zeilenrang, also

$$
\begin{align}
A^{^\dagger} 
&= R^{^\dagger} C^{^\dagger} \\
&= R^{\top} (R R^{\top})^{-1} \, (C^{\top} C)^{-1} C^{\top} \\
&= R^{\top} (C^{\top} C \, R R^{\top})^{-1} C^{\top} \\
&= R^{\top} (C^{\top} A R^{\top})^{-1} C^{\top}
\end{align}
$$

---

Vgl. [[Least Squares und Lineare Regression]]