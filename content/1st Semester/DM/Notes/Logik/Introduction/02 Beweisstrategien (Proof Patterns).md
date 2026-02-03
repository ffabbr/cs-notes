## 01 Beweise für Implikationen

$A \Rightarrow T$

### 1.1 Transitivität (Verkettung von Implikationen)

finde eine andere Aussage R mit $A \Rightarrow R$ und $R \Rightarrow T$

![[Transitivität.png]]

Kind of Modus Ponens

#### 1.1.1 Modus Ponens

Beweise eine andere Aussage, und zeige, dass die eigentliche Aussage aus dieser anderen Aussage folgt. 

$\vDash$ (F ∧ (F → G)) → G

### 1.2 Finde $R_{1}$ und $R_{2}$ mit $S \Rightarrow R_{1}$ und $S \Rightarrow R_{2}$ und zeige, dass $(R_{1}$ und $R_{2}) \Rightarrow T$

### 1.3 Direkter Beweis von $S \Rightarrow T$

1) nimm S als wahr an
2) beweise T unter der Annahme, dass S wahr ist

"klassicher Beweis durch umformen"

Let n,m $\in$ N be arbitrary (beliebig). We assume S. Es existieren k,l $\in$ N, sodass n=2k+1 und m=2l+1

### 1.4 Indirekter Beweis von $S \Rightarrow T$

1) nimm T als falsch an 
2) zeige, dass S falsch ist

(¬ G → ¬ F) $\vDash$ F → G

![[Indirekter Beweis.png]]
## 02 Beweise für allgemeinere Aussagen

### 2.2 Fallunterscheidung (Verallgemeinerung vom Modus Ponens)

1) Endliche Liste an Aussagen T
2) Beweise, dass aus jeder Aussage die eigentliche Aussage S folgt
3) Beweise, dass immer eine der k Aussagen $T_{1}, \dots, T_{k}$Aussagen gilt. 

![[Fallunterscheidung.png]]

### 2.3 Beweis durch Widerspruch (contradiction)

1) Nimm die Aussage S als falsch an 
2) Forme um, sodass du auf eine offensichtlich falsche Aussage kommst.

![[Beweis durch Widerspruch.png]]
![[Bildschirmfoto 2025-10-08 um 19.52.37.png]]
### Existenzbeweis

Finde ein Beispiel

### [[Pigeonhole Principle]]

## 03 Beweise in der Prädikatenlogik

![[Beweise in der Prädikatenlogik.png]]

## 04 Induktion