*number theory*

Wir betrachten hier nur $\mathbb{Z}$, vor allem Integer

> [!success] Gleichung teilen
> Man darf in der Modulo-Rechnung durch eine Zahl a teilen, wenn a und der Modulus teilerfremd sind ($ggT(a,m)=1$).  

Fun Fact: $R_{9}(247) = R_{9}(2+4+7)$ (Skript Seite 85)

## Teilbarkeit

- Euklid-Zerlegung, für alle a, d gibt es $a=dq+r$, $r$ positiv
  
  z.B. $\frac{-1}{2023}$, $a=-1, d=2023$, also $-1=2023\cdot q+r$, 
  sagen wir $q=-1$, also $-1=-2023+r \implies r=2022$ 
  
  Wenn teilbar, dann 
  
  $d\ |\ a \Leftrightarrow r=0$
  $d\ |\ a \Leftrightarrow \exists\ q (a=dq)$

- **Anzahl Teiler** von 100: $100=2^2 \cdot 5^2$. Exponenten +1 und multiplizieren: $3\cdot 3 =9$

## Greatest Common Divisors, $gcd$

- der gcd teilt die beiden Zahlen und alle anderen Teiler der beiden Zahlen sind jeweils kleiner als der gcd
- Wenn $gcd(a,b)=1$, dann sind a und b *relatively prime* (teilerfremd)

$gcd(m,n)=gcd(m,n-qm)$ 

**Beispiel**
$$\begin{align}
gcd(24,70) &= gcd(24,70-2 \cdot 24) \\
&= gcd(24,22) \\
&= gcd(2,22) \\
&= 2
\end{align}$$

## Ideale

Menge aller "Linearkombinationen" der Zahlen. 

**Definition:** 
$(a,b)=\{ua+vb : u,v \in \mathbb{Z}\}$

**Vereinfachung**
$(2,4) = (2) = \{u \cdot 2 : u \in \mathbb{Z}\}$

> Man kann ein Ideal von zwei Zahlen immer auch nur mit einer Zahl darstellen.

$(a,b)=(gcd(a,b))$ 
$(a,b) = \mathbb{Z} \Longleftrightarrow gcd(a,b)=1$


## Least Common Multiples, $lcm$

- das gemeinsame Vielfache, dass alle weiteren gemeinsamen Vielfache teilt

## Primfaktorenzerlegung

$$a = \prod_{i}p_{i}^{e_{i}}$$
$$\begin{aligned}
66 &= 2 \cdot 3 \cdot 11 \\
   &= 2^1 \cdot 3^1 \cdot 5^0 \cdot 7^0 \cdot 11^1
\end{aligned}$$

> Liste der Primfaktoren auf das #helpsheet

$$a=\prod_{i}p_{i}^{e_{i}} \ \ \ \text{und} \ \ \ b=\prod_{i}p_{i}^{f_{i}}$$
dann $$gcd(a,b)=\prod_{i}p_{i}^{min(e_{i}, f_{i})}$$*Jeweils das Minimum jeder Potenz der Primfaktorzerlegung*
$$\begin{align}
gcd(60,126) &= 2^1 \cdot 3^1 \cdot 5^0 \cdot 7^0\dots \\
&= 6
\end{align}$$
Außerdem
$$lcm(a,b)=\prod_{i}p_{i}^{max(e_{i}, f_{i})}$$
und  somit 
$$ab = gcd(a,b) \cdot lcm(a,b)$$da $min(e_{i}, f_{i})+max(e_{i},f_{i})=e_{i}+f_{i}$ für alle $i$.

## Äquivalenzrelation Modulo

$a \equiv_{m} b \Longleftrightarrow m\ |\ (a-b)$
oder $R_{m}(a)=R_{m}(b)$ (Rest. modulo m)

ist eine [[04 Spezielle Relationen|Äquivalenzrelation]] (reflexiv, symmetrisch, transitiv; siehe [[03 Relationen#Wichtige Eigenschaften|Relationseigenschaften]])

Außerdem

$$\begin{align}
a=b &\implies a \equiv_{m} b \\
a \not\equiv_{m}b &\implies a \neq b
\end{align}$$

und

**Lemma 4.14.**  
Wenn $a \equiv_m b$ und $c \equiv_m d$, dann gilt
$$
a + c \equiv_m b + d 
\quad \text{und} \quad 
ac \equiv_m bd.
$$

**Beweis für die erste Aussage**: 
Es gilt $m \mid (a - b)$ und $m \mid (c - d)$.  Daraus folgt, dass $m$ auch
$$
(a - b) + (c - d) = (a + c) - (b + d)
$$
teilt. Und das ist ja die Definition von
$$
a + c \equiv_m b + d.
$$

**Tipp**
Um zu bestimmen, ob $-16 \equiv_{12} 28$ gilt, schauen, ob $28-(-16) \equiv_{12} 0$ gilt.

### Äquivalenzklassen

$[a]_{\equiv_{m}} = \{b\ |\ a \equiv_{m} b\}$

Siehe [[04 Spezielle Relationen#Äquivalenzklassen|Notizen zu speziellen Relationen]] 

### Beispiele für Restklassen

- $R_{15}(16^{1000})=R_{15}(R_{15}(16)^{1000})=R_{15}(1^{1000})=R_{15}(1)=1$
- $R_{2023}(2022^{2023})=R_{2023}(-1^{2023})=R_{2023}(-1)=2022$
- $R_{15}(2^{2024})=R_{15}((2^4)^{506})=R_{15}(R_{15}(16)^{506})=1$ 

→ siehe auch [[04 Euler#Rest berechnen|Rest berechnen mit Euler]] 

## Multiplikatives Inverse

Das multiplikative Inverse einer Zahl ist die Zahl, mit der du die ursprüngliche Zahl multiplizieren musst, um 1 zu erhalten.

**Beispiele**
- $a=2, \ a^{-1}=\frac{1}{2}, \ \text{weil } 2 \cdot \frac{1}{2}=1$
- $3 \equiv_{7} 5$, weil $3\cdot 5=15\equiv_{7}1$

Also z.B. mult. Inverse von 11 mod 26:  $11\cdot u \equiv_{26} 1$

## Chinesischer Restsatz

*Skript 4.5.4*

![[Bildschirmfoto 2025-12-26 um 18.57.21.png]]
![[CRT.png]]

## Diffie-Hellman

→ siehe [[Diffie-Hellman]] 

## Satz von Fermat

**Voraussetzung**: $\textcolor{red}{p}$ ist Primzahl und teilt $\textcolor{green}{m}$ nicht

$$R_{\textcolor{red}{p}}(\textcolor{green}{m}^{\textcolor{orange}{E}}) = R_{\textcolor{red}{p}}\left(\textcolor{green}{m}^{R_{\textcolor{blue}{p-1}}(\textcolor{orange}{E})}\right)$$

Ersetze großen Exponenten $\textcolor{orange}{E}$ durch Rest bei Division durch $\textcolor{blue}{p-1}$.


![[Übung 7.pdf]]
