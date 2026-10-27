
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

Bei der trigonometrischen Interpolation wollen wir $n$ gegebene Datenpunkte (unser Signal $x[t]$) durch ein trigonometrisches Polynom annähern. Da die Daten periodisch sind, arbeiten wir meist mit äquidistanten Stützstellen.

Wir nutzen als Basis die $n$-te primitive komplexe Einheitswurzel $\omega_n = e^{-2\pi i/n}$.

Um die Koeffizienten $y[k]$ für unser trigonometrisches Polynom zu finden, nutzen wir die DFT:

$$y[k] = \sum_{t=0}^{n-1} x[t] \omega_n^{kt}$$

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

### Eigenschaften

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

### Anwendungen

### Filter

![[Bildschirmfoto 2026-10-12 um 16.52.44.png]]

Wir können Frequenzen löschen und zurücktransformieren.

1. **Fourier Transformation:** $\mathbf{y} = F_n\mathbf{x}$
2. **Ungewollte Frequenzen auf 0 setzen:** daraus entsteht $\tilde{\mathbf{y}}$.
3. **Inverse Fourier Transformation** um wieder zusammenzusetzen $\tilde{\mathbf{x}} = F_n^{-1}\tilde{\mathbf{y}}$, zurück in die Zeit

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

Statt alle $N^2$ Multiplikationen direkt auszuführen, verwenden wir Berechnungen wieder, mit divide and conquer. 

Wenn $N$ gerade, teilen wir auf 

1. Summe über alle geraden Indizes
2. Summer über alle ungeraden Indizes

Pro Ebene ist das Zusammenführen in $O(N)$.

![[Bildschirmfoto 2026-10-12 um 16.36.08.png]]

## Faltung

Eine Faltung im Zeitbereich entspricht einer (einfachen) Multiplikation  im Frequenzbereich.
$$
\text{DFT}(u * v) = \text{DFT}(u) \odot \text{DFT}(v)
$$
Mit der FFT können wir die Faltung in $O(n \log n)$ berechnen. 

1. $u$ und $v$ mit FFT in Frequenzbereich $2 \cdot \mathcal{O}(n \log n)$
2. Multipliziere die Spektren elementweise ($\odot$) $\mathcal{O}(n)$.
3. Transformiere das Ergebnis mit IFFT zurück in den Zeitbereich $\mathcal{O}(n \log n)$

### Diskrete Faltung

Kombinieren zweier Vektoren unterschiedlicher Länge zu einem Vektor. Nehme Vektor 1, invertiere, lege links oben über Vektor 2 und schiebe dann Schritt für Schritt nach rechts. Bei jedem Schritt addiere das Ergebnis der Multiplikationen der Zahlen, die direkt übereinander liegen übereinander liegen. Wenn keine zweite Zahl verfügbar, rechne mit `0`.

![[Bildschirmfoto 2026-10-12 um 22.16.37.png]]

### Periodische Faltung

Die beiden Vektoren haben die gleiche Länge. Der Lösungsvektor ebenso. Gleicher Ablauf wie vorher, aber statt wenn keine Zahl des anderen Vektors verfügbar ist, `0` zu verwenden, sind die zahlen hier periodisch, daher nehmen wir einen Eintrag mod. 

![[Bildschirmfoto 2026-10-12 um 22.49.42.png]]

![[Bildschirmfoto 2026-10-12 um 22.49.56.png]]

### Zirkulante Matrizen

Eine zirkulante Matrix ist eine quadratische $n \times n$ Matrix, bei der jede Zeile (oder Spalte) eine um eine Position nach rechts (bzw. unten) verschobene Version der vorherigen Zeile ist. 

$$
C = \begin{pmatrix} c_0 & c_{n-1} & \dots & c_2 & c_1 \\  c_1 & c_0 & c_{n-1} & & c_2 \\  \vdots & c_1 & c_0 & \ddots & \vdots \\  c_{n-2} & & \ddots & \ddots & c_{n-1} \\  c_{n-1} & c_{n-2} & \dots & c_1 & c_0 \end{pmatrix}
$$

Die zirkulante Matrix ist die Matrix-Darstellung der zyklischen Faltungsoperation. 

Eigenschaften

![[Bildschirmfoto 2026-10-12 um 22.51.29.png|270]]
![[Bildschirmfoto 2026-10-12 um 22.51.40.png|271]]
![[Bildschirmfoto 2026-10-12 um 22.51.47.png|273]]
![[Bildschirmfoto 2026-10-12 um 22.51.54.png|271]]
![[Bildschirmfoto 2026-10-12 um 22.52.02.png|271]]
![[Bildschirmfoto 2026-10-12 um 22.52.10.png|273]]

## Stückweise Interpolation mit Splines

Vermeidet das Runge-Phänomen. Vorteil ist auch, dass wir die Interpolation lokal anpassen können.

Ein Spline ist eine Funktion, die stückweise aus Polynomen zusammengesetzt ist. 

Man hat Stützstellen $x_0 < x_1 < \dots < x_n$ (Knoten). Auf jedem Teilintervall $[x_i, x_{i+1}]$ ist der Spline ein eigenes Polynom, und an den Knoten werden die Stücke glatt aneinandergeklebt.

$S_{1, D}$ Menge der stückweise linearen Funktionen die auf $D$ stetig sind
$S_{3, D}$ Menge der zweimal stetig differenzierbaren kubischen Polynome auf D

### Stückweise linearer Spline

jedes Stück ist eine Gerade, somit sind Punkte einfach verbunden. Es gibt "Knicks".

![[Bildschirmfoto 2026-10-12 um 23.00.36.png]]

Vgl. $\lambda(t)$ als "Fortschrittsbalken". 
Den y-Wert bekommen wir mit $f(t) = y_s(1 - \lambda(t)) + y_e\lambda(t)$.
Fortschritt $\lambda(t)$ berechnen: $\lambda(t) = \frac{t - t_s}{t_e - t_s}$

![[Bildschirmfoto 2026-10-12 um 23.01.48.png]]


```python
# === 1. VORBEREITUNG (in __init__) ===

# 1. Daten nach x-Werten sortieren
idx = np.argsort(t)
self.t = t[idx]
self.y = y[idx]

# 2. Steigung für jedes Intervall berechnen: m = (y2 - y1) / (t2 - t1)
self.slopes = np.diff(self.y) / np.diff(self.t)

# === 2. AUSWERTUNG (in __call__) ===

# 3. passendes Intervall finden
idx = np.searchsorted(self.t, x, side="right") - 1

# random safety ding
idxc = np.clip(idx, 0, self.t.size - 2)

# 4. y_neu = y_start + Steigung * Distanz_zum_Start
out = self.y[idxc] + self.slopes[idxc] * (x - self.t[idxc])
```

### Stückweise kubischer Spline

stückweise lineare Interpolation ist nicht glatt (nur $C^0$-stetig), daher kubisch

- jedes Stück ist ein Polynom 3. Grades
- der Spline muss exakt durch die Stützstellen (Datenpunkte) gehen

anliegende **innere** Splines sind
- stetig (Ende des einen Polynoms gleich Anfang des nächsten)
- 1. Ableitung stetig $S_i'(x_{i+1}) = S_{i+1}'(x_{i+1})$, Glattheit der Steigung
- 2. Ableitung stetig $S_i''(x_{i+1}) = S_{i+1}''(x_{i+1})$, Glattheit der Krümmung

**Randwertproblem**
Wenn man $n$ Stützstellen hat, entstehen $n-1$ Intervalle. Man muss ein globales Gleichungssystem mit $3(n-1)+(n+1)=4n-1$ Bedingungen (3 pro innerem Punkt, plus jeder Punkt gleich der ursprünglichen Funktion) lösen. Das Ergebnis ist $C^2$. 

Es fehlen 2 Gleichungen, um das GLS eindeutig lösbar zu machen. Das sind die Randbedingungen an den äußersten Punkten ($x_0$ und $x_{n-1}$).

![[Bildschirmfoto 2026-10-19 um 21.47.16.png]]

- ***vollständiger* kubischer Spline**: 1. Ableitungen an den Endpunkten festgelegt, $O(N)$
- ***natürlicher* kubischer Spline**: 2. Ableitungen an den Endpunkten 0, minimiert die Gesamtkrümmung $O(N)$
- ***periodischer* kubischer Spline**: 1. und 2. Ableitungen an den beiden Endpunkten ident

### Kubische Hermite-Interpolation Spline

Bei den kubischen Splines beeinflusst das Verschieben eines Punktes die Form der gesamten Kurve. 

**Hermite-Interpolation** ist $C^1$ stetig, nicht $C^2$, aber dafür sind die Splines "entkoppelt", jedes Intervall ist rein lokal/isoliert.

Auf jedem Teilintervall gibt man **zwei Werte und zwei Ableitungen** vor, nämlich $f(x_i), f'(x_i)$ und $f(x_{i+1}), f'(x_{i+1})$. 

**Hermite-Basis**
$\varphi(t), \varphi(1-t)$ und $\psi(t), \psi(1-t)$ gewichten den Einfluss der Funktions- und Ableitungswerte auf das Polynomsegment.

![[Bildschirmfoto 2026-10-12 um 23.51.45.png]]


Herleitung:

![[Bildschirmfoto 2026-10-12 um 23.51.15.png]]

![[Bildschirmfoto 2026-10-12 um 23.51.24.png]]

![[Bildschirmfoto 2026-10-12 um 23.51.34.png]]

![[Bildschirmfoto 2026-10-12 um 23.51.39.png]]




## Kurveninterpolation mit quadratischen Splines

```python
def chord_length_knots(points):
    """
    Normierte Bogenlängen-Parametrisierung:
    liefert Stützstellen t und Schrittweiten h.
    Voraussetzung: geschlossene Punktmenge, also p[0] == p[-1].
    """
    p = np.asarray(points, float)
    if p.ndim != 2 or p.shape[1] != 2:
        raise ValueError("points muss die Form (n+1, 2) haben")
    if not np.allclose(p[0], p[-1]):
        raise ValueError("Kurve muss geschlossen sein (p[-1] == p[0])")

    n = p.shape[0] - 1
    if n < 3:
        raise ValueError("mindestens 3 Segmente erforderlich")

    chords = np.linalg.norm(p[1:] - p[:-1], axis=1)
    if np.any(chords <= 0):
        raise ValueError("aufeinanderfolgende Duplikate sind nicht erlaubt")

    L = np.sum(chords)
    t = np.zeros(n + 1)
    t[1:] = np.cumsum(chords) / L
    h = np.diff(t)
    return t, h


# ---------- zyklisches System A = I + shift ----------
def _build_A(n):
    """
    Zirkulante Matrix A: Einsen auf der Diagonale und Superdiagonale,
    plus Wrap-Around A[-1, 0] = 1.
    Entspricht d_j + d_{j+1} = rhs_j.
    """
    A = np.zeros((n, n))
    np.fill_diagonal(A, 1.0)
    A[np.arange(n - 1), np.arange(1, n)] = 1.0
    A[-1, 0] = 1.0
    return A


class ClosedQuadraticSplineCurve:
    """
    Geschlossener quadratischer Spline durch Punkte p (p[0] == p[-1]).
    """

    def __init__(self, points):
        p = np.asarray(points, float)
        t, h = chord_length_knots(p)
        n = len(h)

        dp = p[1:] - p[:-1]                    # Form (n, 2)
        rhs = 2.0 * dp / h[:, None]            
        A = _build_A(n)        # A d = rhs, getrennt pro Koordinate

        # pro Koordinate lösen; falls singulär (n gerade), auf Least Squares ausweichen
        try:
            d_x = np.linalg.solve(A, rhs[:, 0])
        except np.linalg.LinAlgError:
            d_x = np.linalg.lstsq(A, rhs[:, 0], rcond=None)[0]
        try:
            d_y = np.linalg.solve(A, rhs[:, 1])
        except np.linalg.LinAlgError:
            d_y = np.linalg.lstsq(A, rhs[:, 1], rcond=None)[0]
        d = np.column_stack([d_x, d_y])        # Form (n, 2)

        # chi_j = 0.5 * (d_j - d_{j+1})
        d_next = np.roll(d, -1, axis=0)
        chi = 0.5 * (d - d_next)

        self.points = p
        self.t = t
        self.h = h
        self.d = d
        self.chi = chi
        self.n = n

    def _locate(self, t):
        """Intervallindex j und lokale Koordinate tau bestimmen."""
        tt = np.mod(t, 1.0)
        j = np.searchsorted(self.t, tt, side="right") - 1
        j = np.clip(j, 0, self.n - 1)
        tau = (tt - self.t[j]) / self.h[j]
        return j, tau

    def eval(self, t):
        t = np.asarray(t, float)
        j, tau = self._locate(t)
        p_j  = self.points[j]
        p_j1 = self.points[(j + 1) % self.n]
        chi_j = self.chi[j]
        h_j   = self.h[j][..., None]
        tau   = tau[..., None]
        # s_j(t) = (1-τ) p_j + τ p_{j+1} + χ_j h_j τ(1-τ)
        return p_j * (1 - tau) + p_j1 * tau + chi_j * h_j * tau * (1 - tau)

    def derivative(self, t):
        t = np.asarray(t, float)
        j, tau = self._locate(t)
        dp   = self.points[(j + 1) % self.n] - self.points[j]
        base = dp / self.h[j][..., None]
        chi_j = self.chi[j]
        tau   = tau[..., None]
        # s'_j(t) = base + χ_j (1 - 2τ)
        return base + chi_j * (1 - 2 * tau)

    def curvature(self, t):
        t = np.asarray(t, float)
        j, _ = self._locate(t)
        s1 = self.derivative(t)
        s2 = (-2.0 * self.chi[j]) / self.h[j][..., None]
        x1, y1 = s1[..., 0], s1[..., 1]
        x2, y2 = s2[..., 0], s2[..., 1]
        num = x1 * y2 - y1 * x2
        den = np.linalg.norm(s1, axis=-1) ** 3
        out = np.zeros_like(num)
        m = den > 0
        out[m] = num[m] / den[m]
        return out

    def length(self, n_per_seg=200):
        """Gesamtlänge per gleichmäßiger Abtastung (Trapezregel) approximieren."""
        ts = np.linspace(0, 1, self.n * n_per_seg)
        s1 = self.derivative(ts)
        v = np.linalg.norm(s1, axis=1)
        return float(np.trapz(v, ts))
```


## Hermite und co. 

```python
import numpy as np
import matplotlib.pyplot as plt


# ----------------------------
# Hilfsfunktionen für Geometrie
# ----------------------------

def _to_points(Sigma):
    """Stellt sicher, dass Sigma ein Float-Array der Form (n,2) mit n>=2 ist."""
    P = np.array(Sigma, dtype=float)
    if P.ndim != 2 or P.shape[1] != 2 or P.shape[0] < 2:
        raise ValueError("Sigma muss eine Form (n, 2) mit n>=2 haben.")
    return P


def _arc_data(P):
    """
    Berechnet:
      deltas[i] = ||p_{i+1}-p_i|| für i=0..n-2, deltas[n-1] = ||p1 - pn||
      lambdas[k] : λ_0=0, λ_k = Summe_{j=0}^{k-1} deltas[j]
      tangents[i] = (p_{i+1}-p_i)/||...||
    Gibt deltas, lambdas, tangents zurück.
    """
    n = P.shape[0]
    diffs = np.zeros((n, 2))
    for i in range(n - 1):
        diffs[i] = P[i + 1] - P[i]
    diffs[n - 1] = P[0] - P[n - 1]  # Schlisskante

    deltas = np.sqrt((diffs**2).sum(axis=1))
    if np.any(deltas == 0):
        raise ValueError("Aufeinanderfolgende Punkte müssen verschieden sein.")
    tangents = diffs / deltas[:, None]

    lambdas = np.zeros(n + 1)
    for k in range(1, n + 1):
        lambdas[k] = lambdas[k - 1] + deltas[k - 1]

    return deltas, lambdas, tangents


def _find_segment(lambdas, t):
    """
    Finde j in {1..n} mit λ_{j-1} <= t < λ_j (rechts nur am Ende abgeschlossen).
    Falls t == λ_n, gib j = n zurück.
    """
    n = len(lambdas) - 1
    if t >= lambdas[-1]:
        return n
    for j in range(1, n + 1):
        if lambdas[j - 1] <= t < lambdas[j]:
            return j
    return n  # Fallback (sollte nicht auftreten)


# ----------------------------
# (a) Geschlossener polygonaler Interpolant
# ----------------------------

def closed_polygonal_interpolant(Sigma, x):
    """
    Liefert Π_Σ(x_k * λ_n) für sortierte 0 <= x_k < 1.
    """
    P = _to_points(Sigma)
    x = np.asarray(x, dtype=float)
    if x.ndim != 1 or np.any(x < 0) or np.any(x >= 1) or np.any(np.diff(x) < 0):
        raise ValueError("x muss sortiert sein mit 0 <= x_k < 1.")

    deltas, lambdas, _ = _arc_data(P)
    L = lambdas[-1]
    n = P.shape[0]

    Y = np.zeros((x.size, 2))
    for k in range(x.size):
        tk = x[k] * L
        j = _find_segment(lambdas, tk)         # j in 1..n
        t0, t1 = lambdas[j - 1], lambdas[j]
        a = 0.0 if t1 == t0 else (tk - t0) / (t1 - t0)
        p_left = P[j - 1]
        p_right = P[j % n]                     # zyklischer Anschluss
        Y[k] = (1 - a) * p_left + a * p_right
    return Y


# ----------------------------
# (b) Geschlossener kubischer Hermite-Interpolant
# ----------------------------

def _hermite_local(t, t1, t2, y1, y2, c1, c2):
    """
    Skalarer kubischer Hermite auf [t1,t2] mit Werten y1,y2 und Randableitungen c1,c2.
    """
    h = t2 - t1
    if h <= 0:
        return y1
    tau = (t - t1) / h
    # Basisfunktionen
    h00 = (1 + 2*tau) * (1 - tau)**2
    h10 = tau * (1 - tau)**2
    h01 = tau**2 * (3 - 2*tau)
    h11 = tau**2 * (tau - 1)
    return h00 * y1 + h10 * h * c1 + h01 * y2 + h11 * h * c2


def closed_hermite_interpolant(Sigma, x):
    """
    Liefert H_Σ(x_k * λ_n) für sortierte 0 <= x_k <= 1.
    Ableitungen an Knoten gemäss Vorgabe:
      H'(λ_k) = s_k / ||s_k||, wobei s_k aus δ und t gebildet wird.
    """
    P = _to_points(Sigma)
    x = np.asarray(x, dtype=float)
    if x.ndim != 1 or np.any(x < 0) or np.any(x > 1) or np.any(np.diff(x) < 0):
        raise ValueError("x muss sortiert sein mit 0 <= x_k <= 1.")

    deltas, lambdas, tangents = _arc_data(P)
    n = P.shape[0]
    L = lambdas[-1]

    # Ableitungen an den Knoten λ_k, speichere v[0..n] (mit v[n]=v[0])
    v = np.zeros((n + 1, 2))
    # k = 1..n-1
    for k in range(1, n):
        denom = deltas[k - 1] + deltas[k % n]
        s = (deltas[(k) % n] / denom) * tangents[k - 1] + (deltas[k - 1] / denom) * tangents[k % n]
        v[k] = s / np.linalg.norm(s)
    # k = 0 und n
    denom0 = deltas[0] + deltas[-1]
    s0 = (deltas[-1] / denom0) * tangents[0] + (deltas[0] / denom0) * tangents[-1]
    s0 = s0 / np.linalg.norm(s0)
    v[0] = s0
    v[n] = s0

    # Auswertung
    Y = np.zeros((x.size, 2))
    # dupliziere p1 am Ende zur Ausrichtung mit λ_n
    Pk = np.vstack([P, P[0]])
    for k in range(x.size):
        tk = x[k] * L
        j = _find_segment(lambdas, tk)  # [λ_{j-1}, λ_j]
        t1, t2 = lambdas[j - 1], lambdas[j]
        p1, p2 = Pk[j - 1], Pk[j]
        c1, c2 = v[j - 1], v[j]
        Y[k, 0] = _hermite_local(tk, t1, t2, p1[0], p2[0], c1[0], c2[0])
        Y[k, 1] = _hermite_local(tk, t1, t2, p1[1], p2[1], c1[1], c2[1])
    return Y


# ----------------------------
# (c) Adaptive Hermite-Interpolation
# ----------------------------

def adapted_hermite_interpolant(c, nmin, x, tol=1e-3):
    """
    Adaptiver Algorithmus gemäß Pseudocode:
      - starte mit M = {0, 1/nmin, ..., (nmin-1)/nmin}
      - bilde Σ = (c(t))_{t in M}
      - berechne σ_k = ||(H_Σ - Π_Σ)( Mittelpunkt des Segments k in λ )||
      - α = Mittelwert(σ_k); verfeinere dort, wo σ_j > 0.9α (füge t-Mittelpunkte ein)
      - stoppe, wenn max σ_k <= tol
    Gibt (H_vals_at_x, Sigma_final) zurück.
    """
    if nmin <= 1:
        raise ValueError("nmin muss >= 2 sein.")
    x = np.asarray(x, dtype=float)
    if x.ndim != 1 or np.any(x < 0) or np.any(x > 1) or np.any(np.diff(x) < 0):
        raise ValueError("x muss sortiert sein mit 0 <= x_k <= 1.")

    # initiale Parametersammlung M in [0,1)
    M = list(np.linspace(0.0, 1.0, nmin, endpoint=False))

    while True:
        # Σ aus aktuellem M
        Sigma = np.array([c(t) for t in M], dtype=float)
        deltas, lambdas, _ = _arc_data(Sigma)
        n = Sigma.shape[0]
        L = lambdas[-1]

        # λ-Mittelpunkte der Segmente -> normalisierte Mittelpunkte in x
        mids_lambda = 0.5 * (lambdas[:-1] + lambdas[1:])
        mids_x = mids_lambda / L

        # beide Kurven an Mittelpunkten auswerten
        Hm = closed_hermite_interpolant(Sigma, mids_x)
        Pm = closed_polygonal_interpolant(Sigma, mids_x)
        sigmas = np.sqrt(((Hm - Pm) ** 2).sum(axis=1))
        alpha = float(sigmas.mean())

        if sigmas.max() <= tol:
            # fertig
            H_vals = closed_hermite_interpolant(Sigma, x)
            return H_vals, Sigma

        # Verfeinerung: vergleiche jedes σ_j mit 0.9*α
        new_params = []
        for j in range(n):
            if sigmas[j] > 0.9 * alpha:
                # Mittelpunkt im Parameter t zwischen M[j] und M[j+1] (zyklisch)
                t_left = M[j]
                t_right = M[(j + 1) % n] if j + 1 < n else 1.0
                t_mid = 0.5 * (t_left + t_right)
                if t_mid >= 1.0:
                    t_mid -= 1.0
                new_params.append(t_mid)

        # zusammenführen und sortiert eindeutige Werte bilden
        M = sorted(set(M + new_params))


# ----------------------------
# (d) Plot der Drachenform-Kurve
# ----------------------------

def plot_kite(filename, tol=1e-3):
    # c(t) gemäß Aufgabenstellung
    def c(t):
        return np.array([
            np.cos(2*np.pi*t) + (2.0/3.0)*np.cos(4*np.pi*t),
            1.5*np.sin(2*np.pi*t)
        ], dtype=float)

    N = 10_000
    nmin = 6
    xs = np.linspace(0.0, 1.0, N, endpoint=False)

    H_vals, Sigma = adapted_hermite_interpolant(c, nmin, xs, tol=tol)
    P_vals = closed_polygonal_interpolant(Sigma, xs)

    plt.figure()
    plt.plot(P_vals[:, 0], P_vals[:, 1], label="Polygonal interpolant")
    plt.plot(H_vals[:, 0], H_vals[:, 1], label="Hermite interpolation")
    plt.plot(Sigma[:, 0], Sigma[:, 1], "o", markersize=3, label="Vertices Σ")
    plt.gca().set_aspect("equal", adjustable="box")
    plt.xlabel("x"); plt.ylabel("y")
    plt.title(f"Adaptive interpolation (tol={tol:g})")
    plt.legend()
    if not filename.lower().endswith(".png"):
        filename += ".png"
    plt.savefig('./cx_out/'+filename, dpi=150, bbox_inches="tight")
    plt.close()

plot_kite('kite01.png')
```
