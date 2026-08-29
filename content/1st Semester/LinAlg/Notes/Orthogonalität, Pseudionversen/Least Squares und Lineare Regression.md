**Least Squares** ist die Methode, um **Linear Regression** durchzuführen

## Quick-Facts

- $A^\top A \hat{x} = A^\top b$ **(normal equations)**
- $\hat{x} = (A^\top A)^{-1}A^\top b$, **oder** $\hat{x} = A^\dagger b$ (**Pseudoinverse**)
- $P = A(A^\top A)^{-1}A^\top$ **(Projektionsmatrix)**
- $\begin{bmatrix}\alpha_0\\ \alpha_1\end{bmatrix} = (A^\top A)^{-1}A^\top b$ **(Koeffizienten finden, lin. Regr.)**
- [[#Least Squares mit der QR-Zerlegung]]

Explizite Lösung für lineare Regression mit Summen
$$
\begin{bmatrix} \alpha_0 \\ \alpha_1 \end{bmatrix} = \begin{bmatrix} m & \sum_{k=1}^m t_k \\ \sum_{k=1}^m t_k & \sum_{k=1}^m t_k^2 \end{bmatrix}^{-1} \begin{bmatrix} \sum_{k=1}^m b_k \\ \sum_{k=1}^m t_k b_k \end{bmatrix}
$$

## Least Squares, Vorgehen

1. Das Problem als $Ax=b$ darstellen, z.B. eine Gerade $\boxed{y = a_0 + a_1 x}$ als
$$
\begin{bmatrix}
1 & x_1 \\
\vdots & \vdots \\
1 & x_n
\end{bmatrix}
\begin{bmatrix}
a_0 \\
a_1
\end{bmatrix}
=
\begin{bmatrix}
y_1 \\
\vdots \\
y_n
\end{bmatrix}
$$
2. $A^\top A \hat{x} = A^\top b$ lösen, entweder mit $\hat{x} = (A^\top A)^{-1}A^\top b$ oder durch [[Gauss and Gauss-Jordan|das Gauss-Verfahren]] 

### Least Squares mit der QR-Zerlegung

*R und $R^\top$ sind invertierbar, also ist es ev. einfacher, zuerst die QR-Zerlegung durchzuführen, und dann die einfachere Gleichung zu lösen*

$$
\begin{align*}
&A = QR \\
&\Rightarrow A^T A \hat{x} = A^T b \\
&\Rightarrow (QR)^T QR \hat{x} = (QR)^T b \\
&\Rightarrow R^T Q^T Q R \hat{x} = R^T Q^T b \\
&\Rightarrow R^T R \hat{x} = R^T Q^T b \\
&\Rightarrow (R^T)^{-1} R^T R \hat{x} = (R^T)^{-1} R^T Q^T b \\
&\Rightarrow R \hat{x} = Q^T b
&\end{align*}
$$
R ist obere Dreiecksmatrix, also *Rückwertseinsetzen*

## Least Squares, Herleitung

Vorstellung: Wir haben Datenpunkte und eine Linie, die so ca., aber nicht genau, durch diese Datenpunkte verläuft, i.e. wir haben ein Gleichungssystem ohne Lösungen. Wir schauen uns dem Abstand zwischen den echten Werten (z.B. Messwerten), also den Datenpunkten, und unserer Linie an. Dabei können wir für den "Fehler" sagen *Fehler = Echter Wert – Schätzwert*. 

Ziel ist, eine Linie zu finden, sodass der Gesamtfehler möglichst klein ist. Also addieren wir alle Fehler? Da jedoch manche über der Linie liegen und manche unterhalb, würden sie sich (plus und minus) aufheben. Um das zu vermeiden, quadrieren wir die Fehler. 

Mathematisch, ist $b$ unser Messwert und $Ax$ ein Punkt auf unserer Ebene, die vom Spaltenraum von A aufgespannt wird. Wir suchen x, sodass wir am nähesten zu b sind. Den Punkt nennen wir dann $p$ oder $A\hat{x}$. Per siehe [[Projektionen.png]], gilt

$$
\min_{x\in\mathbb{R}^n} \|Ax-b\|^2
$$

Der "Fehler" ist somit $e = b - A\hat{x}=\operatorname{proj}_{C(A)}(b)$, und damit der möglichst klein ist, muss er normal auf die Ebene (die gespanned wird vom Spaltenraum, also normal auf alle Spalten) stehen. Somit gilt 
$$
A^T (b - A\hat{x}) = 0
$$
Aufgelöst haben wir dann die **normal equations**.
$$
\begin{align*}
A^T b - A^T A \hat{x} = 0 \\
\Rightarrow \quad A^T A \hat{x} = A^T b
\end{align*}
$$
$x=Pb$
$P=A(A^TA)^{-1}A^T$

Außerdem gilt
$$
\min_x \|Ax-b\|^2
= \|b - \operatorname{proj}_{C(A)}(b)\|^2
$$
und per normal equations auch
$$
\hat{x}=(A^T A)^{-1}A^T b=A^\dagger b
$$ 
**Im Beispiel von der Notiz zu [[Projektionen (Formel und Beispiel)]]:**

$$
\operatorname{proj}_{C(A)}(\mathbf w)=\begin{pmatrix}1\\4\\5\end{pmatrix}
$$

---

## Linear Regression

Lineare Regression sucht:
$$
b_k \approx \alpha_0 + \alpha_1 t_k
$$
Vgl. klassiche Geradengleichung $y = ax + b$. 
Wir wandeln das in eine Matrix-Situation um und schreiben $Ax \approx b$ mit
$$
A = \begin{bmatrix} 1 & t_1 \\ 1 & t_2 \\ \vdots & \vdots \\ 1 & t_m \end{bmatrix}
$$
Die Spalten stehen für die $t$-Werte. $\alpha_0$ hat den Koeffizient 1, und $t_{k}$ ist unterschiedlich. B ist ein Vektor
$$
\qquad
b=\begin{pmatrix}b_1\\ b_2\\ \vdots\\ b_m\end{pmatrix}
$$
Wir suchen jetzt also $\alpha_0$ und $\alpha_1$, sodass die Fehler minimal sind. Mathematisch: 

$$
\begin{align*}
& \min_{\alpha_0, \alpha_1} \sum_{k=1}^{m} (b_k - (\alpha_0 + \alpha_1 t_k))^2 \\
&= \min_{\alpha_0, \alpha_1} \left\| b - A \begin{bmatrix} \alpha_0 \\ \alpha_1 \end{bmatrix} \right\|^2 \\
&= \min_{\alpha_0, \alpha_1} \left\| \begin{bmatrix} b_1 \\ \vdots \\ b_m \end{bmatrix} - \begin{bmatrix} 1 & t_1 \\ \vdots & \vdots \\ 1 & t_m \end{bmatrix} \begin{bmatrix} \alpha_0 \\ \alpha_1 \end{bmatrix} \right\|^2
\end{align*}
$$
Normal equations:
$$
\begin{align}
A^T A x &= A^T b \\
x&=Pb  \\
P&=A(A^TA)^{-1}A^T
\end{align}
$$

Also mit Least Squares:

$$
\begin{bmatrix}\alpha_0\\ \alpha_1\end{bmatrix}
= (A^T A)^{-1}A^T b
$$

Wenn A linear unabhängige Spalten hat, dann haben wir also
$$
\begin{align*}
\begin{bmatrix} \alpha_0 \\ \alpha_1 \end{bmatrix} &= (A^T A)^{-1} A^T b \\
&= \begin{bmatrix} m & \sum_{k=1}^m t_k \\ \sum_{k=1}^m t_k & \sum_{k=1}^m t_k^2 \end{bmatrix}^{-1} \begin{bmatrix} \sum_{k=1}^m b_k \\ \sum_{k=1}^m t_k b_k \end{bmatrix}
\end{align*}
$$

Wenn A abhängige Spalten hat, dann hätten wir Division durch 0, geht nicht, Vorstellung alle $t$ (also z.B. Zeitpunkte sind zur gleichen Zeit), da können wir keine Gerade aufstellen.