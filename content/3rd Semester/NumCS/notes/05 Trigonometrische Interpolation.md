
## 00 Introduction

Polynomiale Interpolation eignet sich nur für endliche Intervalle. Polynome sind nicht periodisch und gehen außerhalb gegen $\pm \infty$ (Abweichung an dem Rand des Intervalls)

Trigonometrische Interpolation ist ideal für periodische Datenpunkte. Ev. ungenauer an einer spezifischen Stelle, aber dafür überall korrekt.

## 01 Komplexe Zahlen

Schreibweise mit $e$ ist einfacher zum rechnen und Wurzeln ziehen
$$z = r\,(\cos\theta + i\sin\theta) = r\,e^{i\theta}, \qquad e^{i\theta} = \cos\theta + i\sin\theta$$
Komplexe Zahlen multiplizieren: Längen multipliziert, Winkel addiert
somit ist Wurzel ziehen die Umkehroperation, z.B. 4. Wurzel (aus 1) hat 4 Lösungen: Winkel 0°, 90°, 180°, 270° (Vielfache von 360/4)

**Einheitswurzeln**
$$\omega_n := e^{-2\pi i/n} = \cos\left(\tfrac{2\pi}{n}\right) - i\sin\left(\tfrac{2\pi}{n}\right)$$
$$\{\omega_n^k \mid k = 0, 1, \dots, n-1\} = \{1,\ \omega_n,\ \omega_n^2,\ \dots,\ \omega_n^{n-1}\}$$
Wir nehmen die Drehung um $\frac{1}{n}$ Kreis und wenden sie mehrmals an, so entstehen $n$ Punkte, gleichmäßig verteilt auf dem Einheitskreis.

Die Funktionen $\varphi_k(t) = \exp(2\pi i k t)$ bilden eine vollständige **Orthonormalbasis** in $L^2(0,1)$.

**Eigenschaften der Einheitswurzeln**

1. $\overline{\omega_n} = \omega_n^{-1}$ (konjugiert = Vorzeichen des Imaginärteils umgedreht, Punkt an der reellen Achse spiegeln)
2. $\omega_n^n = 1$ (n Drehungen sind der volle Kreis)
3. $\omega_n^{n/2} = -1$ (halber Kreis ist -1; für gerades n)
4. $\omega_n^k = \omega_n^{k+n}$ (n Schritte ist eine volle Drehung)
5. $\sum_{k=0}^{n-1} \omega_n^{jk} = \begin{cases} n & \text{falls } j \equiv 0 \pmod n \\ 0 & \text{sonst} \end{cases}$

## Introduction

**Signale**
Ein Signal ist eine Liste von n Messwerten $\mathbf{x} = (x[0], x[1], \dots, x[n-1])$. Wir wollen dieses Signal als **Summe von reinen Schwingungen** schreiben.

$n$ ist die Anzahl der Messpunkte $t = 0, 1, \dots, n-1$. Also ist x ein Vektor mit n Einträgen.

**Basis-Schwingungen**
Somit hat jede Schwingung $\varphi_{0}, \dots, \varphi_{n-1}$ n Einträge (einen pro Zeitpunkt). Jeder dieser Einträge ist ein Punkt auf dem Einheitskreis bei dem Winkel $2\pi k t / n$.
$$\varphi_k[t] = e^{2\pi i k t / n}, \quad t = 0, \dots, n-1$$

**Warum diese Basis?**
$$e^{i\theta} = \cos\theta + i\sin\theta \quad\Rightarrow\quad \varphi_k[t] = \cos\left(\tfrac{2\pi kt}{n}\right) + i\sin\left(\tfrac{2\pi kt}{n}\right)$$
φ_k = cos-Welle + i · sin-Welle mit Frequenz k → „sin + cos zusammengepackt"

$y_{0}, \dots, y_{n-1}$ sind die Gewichte. Sie sagen, wie viel von welcher Schwingung im Signal $x$ steckt. Wir können das Signal x zusammensetzen aus einer **Linearkombination** dieser.

Um *jedes* Signal in $\mathbb{C}^n$ darstellen zu können, brauchen wir eine Basis. Diese braucht genau n verschiedene Vektoren. Die $\varphi_{0}, \dots, \varphi_{n-1}$ sind orthogonal (siehe 3.3) und somit in $\mathbb{C}^n$ eine Basis.

> [!success]- Weitere Informationen zu der Orthogonalbasis
> Die $\varphi_0, \dots, \varphi_{n-1}$ sind unsere Basis. Sie sind orthogonal zueinander:
> $$\langle \varphi_k, \varphi_l \rangle = \varphi_k^H \varphi_l = \sum_{t=0}^{n-1} \overline{\varphi_k[t]}\, \varphi_l[t] = \begin{cases} n & , l=k \\ 0 & , l \neq k \end{cases}$$
>
> **Why?** Für einen einzelnen Summanden gilt
> $$\overline{\varphi_k[t]}\,\varphi_l[t] = e^{-2\pi i k t/n} \cdot e^{2\pi i l t/n} = e^{2\pi i (l-k) t/n}$$
> (konjugieren dreht das Vorzeichen um, beim Multiplizieren werden Exponenten addiert)
>
> Das gilt für jeden Summanden. Mit $j := k - l$ ist $e^{2\pi i (l-k) t/n} = \omega_n^{jt}$, also
> $$\sum_{t=0}^{n-1} \overline{\varphi_k[t]}\,\varphi_l[t] = \sum_{t=0}^{n-1} \omega_n^{jt} = \begin{cases} n & , j = 0 \ (l = k) \\ 0 & , \text{sonst} \end{cases}$$
> → genau Eigenschaft 5 (siehe 2.4).
>
> **Intuition:** $\overline{\varphi_k}\varphi_l$ ist die relative Drehung zwischen den beiden Schwingungen. Bei gleicher Frequenz sind alle Produkte $= 1$ und summieren sich zu $n$. Bei verschiedener Frequenz laufen die Produkte gleichmässig um den Kreis und heben sich auf, die Summe ist $0$.

**Norm**
Es gilt $$\|\varphi_k\|^2 = \sum_{t=0}^{n-1} |\varphi_k[t]|^2 = \underbrace{1 + 1 + \dots + 1}_{n \text{ Einträge}} = n$$
Misst n-mal zu viel, daher $\frac{1}{n}$.

> [!note]- Ergänzung: Woher genau kommt das $\frac{1}{n}$?
> Bei einer Orthogonalbasis bekommt man das Gewicht eines Basisvektors durch Projektion:
> $$\text{Anteil von } \varphi_k \text{ in } \mathbf{x} = \frac{\langle \varphi_k, \mathbf{x} \rangle}{\|\varphi_k\|^2} = \frac{\langle \varphi_k, \mathbf{x} \rangle}{n}$$
> Die DFT definiert $y[k] := \langle \varphi_k, \mathbf{x} \rangle$ **ohne** das Teilen (Abschnitt 4.1). Deshalb steht das $\frac{1}{n}$ beim Zusammensetzen:
> $$\mathbf{x} = \frac{1}{n}\sum_{k=0}^{n-1} y[k]\,\varphi_k$$


## Fourier- Reihen

Das Ziel unserer Untersuchungen sind (eventuell unglatte) **Funktionen**:

$$
f : (0,1) \longrightarrow \mathbb{C} \text{ mit} \int_0^1 |f(t)|^2 dt < \infty
$$

Für solche Funktionen definieren wir die (kontinuierlichen) Fourier-Koeffizienten:

$$
\hat{f}(k) = \int_0^1 f(t)e^{-2\pi i k t} dt
$$

Dann bilden wir die Summen
$$
p_m(t) = \sum_{k=-m}^{m} \hat{f}(k)e^{2\pi i k t}
$$

und wir lassen $m \to \infty$. Fourier besagt:
$$ \lim_{m\to\infty} \|p_m(\cdot) - f(\cdot)\|_2 = \lim_{m\to\infty} \sqrt{\int_0^1 |p_m(x) - f(x)|^2 dx} = 0 $$
und Parseval besagt:
$$ \|f\|_2^2 = \int_0^1 |f(x)|^2 dx = \lim_{m \to \infty} \sum_{k=-m}^m |\hat{f}(k)|^2 = \|\hat{f}\|_{\ell^2}^2, $$

wobei $\hat{f} = (\hat{f}(k))_{k \in \mathbb{Z}}$  eine Folge mit entsprechender Norm ist.

#### Gibbs Phänomen

Funktion mit einem Sprung durch Fourier beschrieben hat Überschwingungen

Beispiel 3.1.17: 
$b - a + \frac{1}{\pi} \sum_{k \neq 0} e^{-ikc} \frac{\sin kd}{k} e^{i2\pi kt}$, $t \in [0, 1]$

```python
def exactFourierSeries(x,N): 
	result = 1j * zeros(x.size)
	result += b-a
	
	for k in range(-N, N+1): # since we can't do infty
	  if k==0: continue
	  result += exp(-1j*k*c) * sin(k*d)/k * exp(1j*2*pi*k*x) / pi
	
	return result
```


## Diskrete Fourier-Transformation

Statt kontinuierliche Funktionen betrachten haben wir jetzt nur eine endliche Liste an Datenpunkten. 

$$\langle\varphi_k, \mathbf{x}\rangle = \sum_t \overline{\varphi_k[t]}\, x[t] = \sum_t x[t]\, e^{-2\pi i k t/n}$$

> [!success] DFT
> $$y[k] = \sum_{t=0}^{n-1} x[t]\, e^{-2\pi i k t/n}, \quad k = 0, \dots, n-1$$

$e^{-2\pi i k t/n} = \omega_n^{kt}$, also

$$y[k] = \sum_{t=0}^{n-1} x[t]\,\omega_n^{kt}$$

**Intuition**
Für **eine** Frequenz k gehst du alle Zeitpunkte t durch. Jeden Messwert `x[t]` multiplizierst du mit einem Punkt auf dem Kreis, der sich **rückwärts** mit Frequenz k dreht. Dann summierst du alles. Steckt Frequenz k im Signal, dreht sich dieser Anteil vorwärts mit k. Das Rückwärtsdrehen hebt die Drehung genau auf. Alle Beiträge zeigen in dieselbe Richtung und addieren sich, also wird `y[k]` gross. Andere Frequenzen drehen weiter und heben sich auf (Orthogonalität).

`y[k]` misst also, wie stark Frequenz k im Signal vorkommt.

### Fourier-Matrix

$$
\mathbf{F}_n = \left[\exp\left(\frac{-2\pi i k t}{n}\right)\right]_{k,t=0}^{n-1}
$$
Also:
$$
\mathbf{F}_n = \begin{bmatrix}
1 & 1 & 1 & \cdots & 1 \\
1 & e^{-2\pi i/n} & e^{-4\pi i/n} & \cdots & e^{-2\pi i(n-1)/n} \\
1 & e^{-4\pi i/n} & e^{-8\pi i/n} & \cdots & e^{-4\pi i(n-1)/n} \\
1 & e^{-6\pi i/n} & e^{-12\pi i/n} & \cdots & e^{-6\pi i(n-1)/n} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
1 & e^{-2\pi i(n-1)/n} & e^{-4\pi i(n-1)/n} & \cdots & e^{-2\pi i(n-1)^2/n}
\end{bmatrix} \in \mathbb{C}^{n \times n}.
$$
ist symmetrisch.

> [!note] Ergänzung: Kurzform und Lesart
> Eintrag in Zeile $k$, Spalte $t$: $(\mathbf{F}_n)_{k,t} = \omega_n^{kt}$.
> Zeile $k$ ist genau $\overline{\varphi_k}^\top$, d.h. Zeile $k$ mal $\mathbf{x}$ ergibt $\langle \varphi_k, \mathbf{x} \rangle = y[k]$.

![[Pasted image 20261005110030.png]]

### Inverse DFT

Die IDFT setzt wieder zusammen. Es gilt

$$
IDFT(DFT(x)) = \mathbf{F}_{n}^{-1}(\mathbf{F}_{n}\mathbf{x}) = \mathbf{F}_{n}^{-1}\mathbf{y} = \mathbf{x}
$$

![[Pasted image 20261005110141.png]]

## Eigenschaften

- Periodisch: $y[k] = y[k+n]$
- Symmetrie: $y[k] = \overline{y[n-k]}$ (*Ergänzung: gilt nur für **reelles** Signal $\mathbf{x}$*)
- Linearität: $\text{DFT}(a\mathbf{x} + b\mathbf{z}) = a\,\text{DFT}(\mathbf{x}) + b\,\text{DFT}(\mathbf{z})$
- Energie-Erhaltung: $\sum_t |x[t]|^2 = \frac{1}{n}\sum_k |y[k]|^2$

Rechenaufwand naiv: $O(n^2)$, FFT $O(n \log n)$

### Time vs Frequency Domain

- **Time domain**: gewichtete Summe aller Schwingungen über die Zeit, Wert `x[t]` über Zeit t
- **Frequency Domain**: Stärke `|y[k]|` über Frequenz k. Wie viel von jeder Frequenz kommt allgemein vor.

### Frequenzanalyse

`y[k]` misst, wie stark Frequenz k im Signal vorkommt.

![[Pasted image 20261005112958.png]]

Das ist wegen der Periodizität. **Frequenz n − k ist dasselbe wie Frequenz −k.**


## Anwendungen

### Filter

![[Bildschirmfoto 2026-10-12 um 16.52.44.png]]

Wir können Frequenzen löschen und zurücktransformieren.

1. **Fourier Transformation:** $\mathbf{y} = F_n\mathbf{x}$
2. **Ungewollte Frequenzen auf 0 setzen:** daraus entsteht $\tilde{\mathbf{y}}$.
3. **Inverse Fourier Transformation** um wieder zusammenzusetzen $\tilde{\mathbf{x}} = F_n^{-1}\tilde{\mathbf{y}}$, zurück in die Zeit

---

Beispiel, schwache Frequenzen (Noise) entfernen

```python
r = 0.25 # Threshold
N = len(y)
c = np.fft.fft(y) # y = F_n * x

py = np.abs(c)**2 / N # power spectrum berechnen

# boolean mask, true if bigger than 25% of maximum
mask = py > (r * py.max())
c_filtered = c * mask

y_filtered = np.fft.ifft(c_filtered).real # inverse, back to zeitsignal
```

Beispiel, hohe Frequenzen entfernen

```python
# Vorwärtstransformation (Zeit -> Frequenz)
c = fft.fft(y)

# Einen einfachen Tiefpassfilter entwerfen
cutoff = N // 8
mask = np.zeros(N)
mask[:cutoff] = 1
mask[-cutoff:] = 1

# Filter im Frequenzbereich anwenden
c_filtered = c * mask

# Inverse Transformation (Frequenz -> Zeit)
y_filtered = np.fft.ifft(c_filtered)
```

Beispiel, tiefe Frequenzen entfernen

```python
# Vorwärtstransformation
c = fft.fft(y)
N = len(y)

cutoff = N // 8
mask = np.ones(N)
mask[:cutoff] = 0
mask[-cutoff:] = 0

c_filtered = c * mask
y_filtered = fft.ifft(c_filtered).real
```

### Approximation einer Funktion

$n$ Datenpunkte, somit können wir in $n$ Frequenzen zerlegen. Um $N$ Punkte zu berechnen ($N > n$), machen wir eine Rücktransformation. Dafür nehmen wir ein größeres Array. Alte Kurve hatte nur Frequenzen bis `max_freq`, somit alles höher als das (also in der Mitte) füllen wir mit `0`. 

```python
def evaliptrig(y, N):
    n = len(y) # Anzahl ursprüngliche Messpunkte
    if(n % 2 != 0):
        raise ValueError("y must be of even length") 
        
    max_freq = n // 2 # Ganzzahldivision
    coeffs = np.fft.ifft(y) # Originaldaten -> Frequenzbereich mit Koeffizienten
    
    # ---- FALLs mit f' statt f ---
    # k = np.fft.fftfreq(n, d=1.0 / n)
    # dcoeffs = -2j * np.pi * k * coeffs
    # padded = np.zeros(N, dtype=complex)
    # padded[:max_freq] = dcoeffs[:max_freq]
    # padded[-max_freq:] = dcoeffs[max_freq:]
    # --------
    
    padded = np.zeros(N, dtype=complex) # neues, großes Zielarray
    
    # niedrige Frequenzen kopieren
    padded[:max_freq] = coeffs[:max_freq]
    padded[-max_freq:] = coeffs[max_freq:] # beginne bei dem max_freq letzten element und gehe bis ans Ende
    
    v = np.fft.fft(padded) # verlängertes Frequenz-Array -> Ortsbereich
    
    return v
```

---


## Fast Fourier Transformation

$O(N \log N)$

Statt alle $N^2$ Multiplikationen direkt auszuführen, verwenden wir Berechnungen wieder, indem wir das Problem in Hälften aufteilen (divide and conquer). Pro Ebene ist das Zusammenführen in $O(N)$.

![[Bildschirmfoto 2026-10-12 um 21.12.28.png]]


![[Bildschirmfoto 2026-10-12 um 16.36.08.png]]

## Faltung

**Diskrete Faltung**
Kombinieren zweier Vektoren unterschiedlicher Länge zu einem Vektor. Nehme Vektor 1, invertiere, lege links oben über Vektor 2 und schiebe dann Schritt für Schritt nach rechts. Bei jedem Schritt addiere das Ergebnis der Multiplikationen der Zahlen, die direkt übereinander liegen übereinander liegen. Wenn keine zweite Zahl verfügbar, rechne mit `0`.

![[Bildschirmfoto 2026-10-12 um 22.16.37.png]]

**Periodische Faltung**
Die beiden Vektoren haben die gleiche Länge. Der Lösungsvektor ebenso. Gleicher Ablauf wie vorher, aber statt wenn keine Zahl des anderen Vektors verfügbar ist, `0` zu verwenden, sind die zahlen hier periodisch, daher nehmen wir einen Eintrag mod. 

![[Bildschirmfoto 2026-10-12 um 22.49.42.png]]![[Bildschirmfoto 2026-10-12 um 22.49.56.png]]

**Zirkulante Matrizen**

![[Bildschirmfoto 2026-10-12 um 22.51.20.png]]

![[Bildschirmfoto 2026-10-12 um 22.51.29.png]]

![[Bildschirmfoto 2026-10-12 um 22.51.40.png]]

![[Bildschirmfoto 2026-10-12 um 22.51.47.png]]

![[Bildschirmfoto 2026-10-12 um 22.51.54.png]]

![[Bildschirmfoto 2026-10-12 um 22.52.02.png]]

![[Bildschirmfoto 2026-10-12 um 22.52.10.png]]

## Stückweise Interpolation mit Splines

Vermeidet das Runge-Phänomen. Vorteil ist auch, dass wir die Interpolation lokal anpassen können.

Ein Spline ist eine Funktion, die **stückweise aus Polynomen** zusammengesetzt ist. Man hat Stützstellen $x_0 < x_1 < \dots < x_n$ (die „Knoten“). Auf jedem Teilintervall $[x_i, x_{i+1}]$ ist der Spline ein eigenes Polynom, und an den Knoten werden die Stücke **glatt aneinandergeklebt**.

Slides

$S_{1, D}$ Menge der stückweise linearen Funktionen die auf $D$ stetig sind
$S_{3, D}$ Menge der zweimal stetig differenzierbaren kubischen Polynome auf D


### Stückweise linearer Spline

**linearer Spline**
jedes Stück ist eine Gerade (Punkte einfach verbunden)


![[Bildschirmfoto 2026-10-12 um 23.00.36.png]]

Vgl. $\lambda(t)$ als "Fortschrittsbalken". Den y-Wert bekommen wir mit $f(t) = y_s(1 - \lambda(t)) + y_e\lambda(t)$.

Fortschritt $\lambda(t)$ berechnen: 
$\lambda(t) = \frac{t - t_s}{t_e - t_s}$

![[Bildschirmfoto 2026-10-12 um 23.01.48.png]]


### Stückweise kubischer Spline

stückweise lineare Interpolation ist nicht glatt (nur $C^0$-stetig), das lösen wir hier. 

jedes Stück ein Polynom 3. Grades. An jedem inneren Knoten muss der Spline durch den Datenpunkt gehen, und mit $s$, $s'$ und $s''$ von links und rechts übereinstimmen.

anliegende **innere** Splines
- stetig
- 1. Ableitung stetig
- 2. Ableitung stetig

Dadurch hängen alle Stücke zusammen, und man muss ein globales Gleichungssystem mit $3(n-1)+(n+1)=4n-1$ Bedingungen (3 Bedingungen pro innerem Punkt, plus für jeden Punkt gleich der ursprünglichen Funktion) lösen. Das Ergebnis ist $C^2$. 

*vollständiger* kubischer Spline: 1. Ableitungen an den Endpunkten (ganz links, ganz rechts) festgelegt, $O(N)$
*natürlicher* kubischer Spline: 2. Ableitungen an den Endpunkten 0, minimiert die Gesamtkrümmung $O(N)$
*periodischer* kubischer Spline: 1. und 2. Ableitungen an den Endpunkten gleich

### Kubische Hermite-Interpolation Spline

**Ein Spline ist $C^2$-stetig, ein Hermite-Polynom im Allgemeinen nur $C^1$-stetig.**

Auf jedem Teilintervall gibt man **zwei Werte und zwei Ableitungen** vor, nämlich $f(x_i), f'(x_i)$ und $f(x_{i+1}), f'(x_{i+1})$. Das sind genau 4 Bedingungen für 4 Koeffizienten, also ist jedes Stück für sich allein eindeutig festgelegt.

Hermite Basisfunktionen $\varphi(t), \varphi(1-t)$ und $\psi(t), \psi(1-t)$ gewichten den Einfluss der Funktions- und Ableitungswerte auf das Polynomsegment.

![[Bildschirmfoto 2026-10-12 um 23.51.07.png]]

![[Bildschirmfoto 2026-10-12 um 23.51.15.png]]

![[Bildschirmfoto 2026-10-12 um 23.51.24.png]]

![[Bildschirmfoto 2026-10-12 um 23.51.34.png]]

![[Bildschirmfoto 2026-10-12 um 23.51.39.png]]

![[Bildschirmfoto 2026-10-12 um 23.51.45.png]]

![[Bildschirmfoto 2026-10-12 um 23.51.52.png]]

## Quadratur

Approximation von Integralen

Algebraische Konvergenz: $E(n) \in O\left( \frac{1}{n^p} \right) \text{ für } p> 0$
Exponentielle Konvergenz: $E(n) \in O(q^n) \text{ für } 0 \leq q \leq 1$ 

