
> [!abstract] Überblick: Worum geht es?
> **Problem:** Wir haben viele Messwerte, die ein *periodisches* Muster zeigen (z.B. Audio, Temperatur über Jahre). Wir wollen sie gut darstellen, analysieren und interpolieren.
>
> **Idee:** Jedes Signal lässt sich als **Summe von reinen Schwingungen** (sin/cos mit verschiedenen Frequenzen) schreiben. Die Fourier-Transformation berechnet, *wie viel* von jeder Frequenz im Signal steckt.
>
> 1. **Motivation:** Warum nicht einfach Polynome?
> 2. **Werkzeug:** komplexe Zahlen & Einheitswurzeln
> 3. **Basis:** Signale als Summe von Schwingungen $\varphi_k$
> 4. **DFT:** Gewichte $y[k]$ berechnen (Formel + Matrix), und **IDFT** zurück
> 5. **Eigenschaften & Interpretation:** Zeit- vs. Frequenzbereich
> 6. **Anwendungen:** Filter, trigonometrische Interpolation

## 0 Notation

| Symbol | Bedeutung |
| --- | --- |
| $n$ | Anzahl Messwerte (Länge des Signals) |
| $t = 0, \dots, n-1$ | Zeitindex (welcher Messpunkt) |
| $k = 0, \dots, n-1$ | Frequenzindex (welche Schwingung) |
| $\mathbf{x} = (x[0], \dots, x[n-1]) \in \mathbb{C}^n$ | Signal, **Zeitbereich** |
| $\mathbf{y} = (y[0], \dots, y[n-1]) \in \mathbb{C}^n$ | Fourier-Koeffizienten / Gewichte, **Frequenzbereich** |
| $i$ | imaginäre Einheit, $i^2 = -1$ |
| $\overline{z}$ | komplex konjugiert (Imaginärteil negiert, an reeller Achse gespiegelt) |
| $\lvert z \rvert$ | Betrag = Länge von $z$ |
| $\omega_n = e^{-2\pi i/n}$ | $n$-te Einheitswurzel: Drehung um $\frac{1}{n}$ Kreis |
| $\varphi_k[t] = e^{2\pi i k t/n}$ | Basis-Schwingung mit Frequenz $k$ |
| $\langle \mathbf{u}, \mathbf{v} \rangle = \mathbf{u}^H \mathbf{v} = \sum_t \overline{u[t]}\, v[t]$ | inneres Produkt (Skalarprodukt) in $\mathbb{C}^n$ |
| $\mathbf{A}^H = \overline{\mathbf{A}}^\top$ | konjugiert-transponiert („hermitesch“) |
| $\mathbf{F}_n$ | Fourier-Matrix, $\mathbf{y} = \mathbf{F}_n \mathbf{x}$ |
| $j \equiv 0 \pmod n$ | $j$ ist ein Vielfaches von $n$ |
| $p_m(t),\ c_k$ | trigonometrisches Polynom vom Grad $m$ und seine Koeffizienten |

> [!note] Ergänzung: Vorzeichen-Falle
> $\omega_n$ hat ein **Minus** im Exponenten, $\varphi_k$ ein **Plus**. Es gilt $\varphi_k[t] = \omega_n^{-kt} = \overline{\omega_n^{kt}}$.
> Die DFT verwendet $\omega_n^{kt}$ (Minus, „rückwärts drehen“), die IDFT $e^{+2\pi i k t/n}$ (Plus).

## 1 Motivation: Warum Fourier?

Möchten eine große Menge von Punkten interpolieren, die ein periodisches Muster aufweisen.

Polynomiale Interpolation eignet sich nur für endliche Intervalle. Polynome sind nicht periodisch und gehen außerhalb gegen $\pm \infty$ (Abweichung an dem Rand des Intervalls)

Trigonometrische Interpolation ist ideal für periodische Datenpunkte. Ev. ungenauer an einer spezifischen Stelle, aber dafür überall korrekt.

→ Wir brauchen also periodische „Bausteine“ (Schwingungen). Am einfachsten rechnet man mit ihnen als komplexe Zahlen auf dem Einheitskreis. Daher zuerst die Grundlagen.

## 2 Grundlagen: Komplexe Zahlen

### 2.1 Zwei Schreibweisen

Es gibt 2 Schreibweisen für komplexe Zahlen.

1. Schreibweise mit sin/cos: Koordinaten werden angegeben
2. Schreibweise mit $e^{\dots}$: wir geben den Winkel an

Wir verwenden oft die Schreibweise mit $e$, da man einfacher rechnen und Wurzeln ziehen kann.

> [!note] Ergänzung: Euler-Formel (verbindet beide Schreibweisen)
> $$z = r\,(\cos\theta + i\sin\theta) = r\,e^{i\theta}, \qquad e^{i\theta} = \cos\theta + i\sin\theta$$
> $r = \lvert z \rvert$ ist die Länge, $\theta$ der Winkel. Für $r = 1$ liegt $z$ auf dem Einheitskreis.

### 2.2 Multiplikation und Wurzeln

Komplexe Zahlen multiplizieren: Längen multipliziert, Winkel addiert
somit ist Wurzel ziehen die Umkehroperation
z.B. 4. Wurzel (aus 1) hat 4 Lösungen: Winkel 0°, 90°, 180°, 270° (Vielfache von 360/4)

### 2.3 Einheitswurzeln

$$\omega_n := e^{-2\pi i/n} = \cos\left(\tfrac{2\pi}{n}\right) - i\sin\left(\tfrac{2\pi}{n}\right)$$
**Einheitswurzeln**
$$\{\omega_n^k \mid k = 0, 1, \dots, n-1\} = \{1,\ \omega_n,\ \omega_n^2,\ \dots,\ \omega_n^{n-1}\}$$
Wir nehmen die Drehung um $\frac{1}{n}$ Kreis und wenden sie mehrmals an, so entstehen $n$ Punkte, gleichmäßig verteilt auf dem Einheitskreis.

### 2.4 Eigenschaften der Einheitswurzeln

1. $\overline{\omega_n} = \omega_n^{-1}$ (konjugiert = Vorzeichen des Imaginärteils umgedreht, Punkt an der reellen Achse spiegeln)
2. $\omega_n^n = 1$ (n Drehungen sind der volle Kreis)
3. $\omega_n^{n/2} = -1$ (halber Kreis ist -1; für gerades n)
4. $\omega_n^k = \omega_n^{k+n}$ (n Schritte ist eine volle Drehung)
5. $\sum_{k=0}^{n-1} \omega_n^{jk} = \begin{cases} n & \text{falls } j \equiv 0 \pmod n \\ 0 & \text{sonst} \end{cases}$

> [!tip] Eigenschaft 5 ist die wichtigste
> Sie ist der Grund, warum die Schwingungen $\varphi_k$ orthogonal sind (Abschnitt 3.3) und damit, warum die ganze DFT funktioniert.

## 3 Signale als Summe von Schwingungen

### 3.1 Signale

Ein Signal ist eine Liste von n Messwerten $\mathbf{x} = (x[0], x[1], \dots, x[n-1])$. Wir wollen dieses Signal als **Summe von reinen Schwingungen** schreiben.

$n$ ist die Anzahl der Messpunkte $t = 0, 1, \dots, n-1$. Also ist x ein Vektor mit n Einträgen.

### 3.2 Die Basis-Schwingungen $\varphi_k$

Somit hat jede Schwingung $\varphi_{0}, \dots, \varphi_{n-1}$ n Einträge (einen pro Zeitpunkt). Jeder dieser Einträge ist ein Punkt auf dem Einheitskreis bei dem Winkel $2\pi k t / n$.
$$\varphi_k[t] = e^{2\pi i k t / n}, \quad t = 0, \dots, n-1$$

**Warum diese Basis?**
$$e^{i\theta} = \cos\theta + i\sin\theta \quad\Rightarrow\quad \varphi_k[t] = \cos\left(\tfrac{2\pi kt}{n}\right) + i\sin\left(\tfrac{2\pi kt}{n}\right)$$
φ_k = cos-Welle + i · sin-Welle mit Frequenz k → „sin + cos zusammengepackt"

$y_{0}, \dots, y_{n-1}$ sind die Gewichte. Sie sagen, wie viel von welcher Schwingung im Signal $x$ steckt. Wir können das Signal x zusammensetzen aus einer **Linearkombination** dieser.

Um *jedes* Signal in $\mathbb{C}^n$ darstellen zu können, brauchen wir eine Basis. Diese braucht genau n verschiedene Vektoren. Die $\varphi_{0}, \dots, \varphi_{n-1}$ sind orthogonal (siehe 3.3) und somit in $\mathbb{C}^n$ eine Basis.

### 3.3 Orthogonalität

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

### 3.4 Norm und der Faktor $\frac{1}{n}$

Es gilt $$\|\varphi_k\|^2 = \sum_{t=0}^{n-1} |\varphi_k[t]|^2 = \underbrace{1 + 1 + \dots + 1}_{n \text{ Einträge}} = n$$
Misst n-mal zu viel, daher $\frac{1}{n}$.

> [!note] Ergänzung: Woher genau kommt das $\frac{1}{n}$?
> Bei einer Orthogonalbasis bekommt man das Gewicht eines Basisvektors durch Projektion:
> $$\text{Anteil von } \varphi_k \text{ in } \mathbf{x} = \frac{\langle \varphi_k, \mathbf{x} \rangle}{\|\varphi_k\|^2} = \frac{\langle \varphi_k, \mathbf{x} \rangle}{n}$$
> Die DFT definiert $y[k] := \langle \varphi_k, \mathbf{x} \rangle$ **ohne** das Teilen (Abschnitt 4.1). Deshalb steht das $\frac{1}{n}$ beim Zusammensetzen:
> $$\mathbf{x} = \frac{1}{n}\sum_{k=0}^{n-1} y[k]\,\varphi_k$$

### 3.5 Beispiel ($n = 4$)

Beispiel: Unser Signal ist $\mathbf{x} = [x_0, x_1, x_2, x_3] = [f(0), f(1), f(2), f(3)]$. Dann muss gelten: $\mathbf{x} = \frac{1}{n}(y_0\varphi_0 + y_1\varphi_1 + y_2\varphi_2 + y_3\varphi_3)$ $= \frac{1}{n}(y_0[1, 1, 1, 1] + y_1[1, i, -1, -i] + y_2[1, -1, 1, -1] + y_3[1, -i, -1, i])$.

→ Wie man die Gewichte $y_0, \dots, y_3$ findet, sagt die DFT im nächsten Abschnitt.

## 4 Diskrete Fourier Transformation (DFT)

### 4.1 Definition

Das Gewicht von Frequenz $k$ ist das innere Produkt von $\varphi_k$ mit dem Signal:

$$\langle\varphi_k, \mathbf{x}\rangle = \sum_t \overline{\varphi_k[t]}\, x[t] = \sum_t x[t]\, e^{-2\pi i k t/n}$$

> [!important] DFT
> $$y[k] = \sum_{t=0}^{n-1} x[t]\, e^{-2\pi i k t/n}, \quad k = 0, \dots, n-1$$

$e^{-2\pi i k t/n} = \omega_n^{kt}$, also

$$y[k] = \sum_{t=0}^{n-1} x[t]\,\omega_n^{kt}$$

### 4.2 Intuition

Für **eine** Frequenz k gehst du alle Zeitpunkte t durch. Jeden Messwert x[t] multiplizierst du mit einem Punkt auf dem Kreis, der sich **rückwärts** mit Frequenz k dreht. Dann summierst du alles. Steckt Frequenz k im Signal, dreht sich dieser Anteil vorwärts mit k. Das Rückwärtsdrehen hebt die Drehung genau auf. Alle Beiträge zeigen in dieselbe Richtung und addieren sich, also wird y[k] gross. Andere Frequenzen drehen weiter und heben sich auf (Orthogonalität).

y[k] misst also, wie stark Frequenz k im Signal vorkommt.

### 4.3 Matrixform: die Fourier-Matrix

Da DFT eine lineare Abbildung ist, können wir eine Abbildungsmatrix definieren.

**Definition (Fourier Matrix):** Sei $n \in \mathbb{N}$. Die Fourier Matrix $\mathbf{F}_n \in \mathbb{C}^{n \times n}$ ist definiert als:
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
Bemerke, dass $\mathbf{F}_n = \mathbf{F}_n^\top$, also $\mathbf{F}_n$ ist symmetrisch.

> [!note] Ergänzung: Kurzform und Lesart
> Eintrag in Zeile $k$, Spalte $t$: $(\mathbf{F}_n)_{k,t} = \omega_n^{kt}$.
> Zeile $k$ ist genau $\overline{\varphi_k}^\top$, d.h. Zeile $k$ mal $\mathbf{x}$ ergibt $\langle \varphi_k, \mathbf{x} \rangle = y[k]$.

![[Pasted image 20261005110030.png]]

### 4.4 Inverse Diskrete Fourier Transformation (IDFT)

Die DFT zerlegt, die IDFT setzt wieder zusammen. Es geht keine Information verloren, es gilt

$$
IDFT(DFT(x)) = \mathbf{F}_{n}^{-1}(\mathbf{F}_{n}\mathbf{x}) = \mathbf{F}_{n}^{-1}\mathbf{y} = \mathbf{x}
$$

![[Pasted image 20261005110141.png]]

> [!note] Ergänzung: Warum $\mathbf{F}_n^{-1} = \frac{1}{n}\mathbf{F}_n^H$?
> Die Spalten von $\mathbf{F}_n^H$ sind genau die $\varphi_k$. Wegen der Orthogonalität (3.3) gilt $\mathbf{F}_n\mathbf{F}_n^H = n\,\mathbf{I}$, also $\mathbf{F}_n \cdot \frac{1}{n}\mathbf{F}_n^H = \mathbf{I}$.
> Die IDFT-Formel oben ist genau $\mathbf{x} = \frac{1}{n}\sum_k y[k]\,\varphi_k$ aus 3.4.

## 5 Eigenschaften & Interpretation

### 5.1 Eigenschaften

- Periodisch: $y[k] = y[k+n]$
- Symmetrie: $y[k] = \overline{y[n-k]}$ (*Ergänzung: gilt nur für **reelles** Signal $\mathbf{x}$*)
- Linearität: $\text{DFT}(a\mathbf{x} + b\mathbf{z}) = a\,\text{DFT}(\mathbf{x}) + b\,\text{DFT}(\mathbf{z})$
- Energie-Erhaltung: $\sum_t |x[t]|^2 = \frac{1}{n}\sum_k |y[k]|^2$

Rechenaufwand naiv: $O(n^2)$

> [!note] Ergänzung: Ausblick
> Naiv: Matrix-Vektor-Produkt mit $n \times n$ Matrix → $O(n^2)$. Die **FFT** (Fast Fourier Transform) nutzt die Eigenschaften der Einheitswurzeln aus und schafft $O(n \log n)$.

### 5.2 Time vs Frequency Domain

- Time domain: gewichtete Summe aller Schwingungen über die Zeit, Wert `x[t]` über Zeit t
- Frequency Domain: Stärke `|y[k]|` über Frequenz k. Wie viel von jeder Frequenz kommt allgemein vor.

### 5.3 Frequenzanalyse

y[k] misst, wie stark Frequenz k im Signal vorkommt.

![[Pasted image 20261005112958.png]]

Das ist wegen der Periodizität. **Frequenz n − k ist dasselbe wie Frequenz −k.**

## 6 Anwendungen

### 6.1 Filter

Wir können im Frequenzbereich gezielt Frequenzen löschen und zurücktransformieren.

1. **Fourier Transformation:** $\mathbf{y} = F_n\mathbf{x}$
2. **Ungewollte Frequenzen auf 0 setzen:** daraus entsteht $\tilde{\mathbf{y}}$.
3. **Inverse Fourier Transformation** um wieder zusammenzusetzen $\tilde{\mathbf{x}} = F_n^{-1}\tilde{\mathbf{y}}$, zurück in die Zeit

### 6.2 Trigonometrische Interpolation

Zurück zur Motivation (Abschnitt 1): Statt nur einen Vektor wollen wir eine Funktion, die durch die Datenpunkte geht.

**Trigonometrisches Polynom (Grad m)**
$$p_m(t) = \sum_{k=-m}^{m} c_k\, e^{2\pi ikt}, \quad t \in [0,1)$$
- Summe von Schwingungen bis Frequenz m, 1-periodisch
- $t$ kontinuierlich → Funktion (nicht nur Vektor wie bei DFT)
- $c_{-k} = \overline{c_k}$ → $p_m$ reell
- Koeffizienten aus DFT: $c_k = y[k]/n$

> [!note] Ergänzung: Zusammenhang mit der DFT
> Die Messwerte liegen bei $t_j = j/n$, also $x[j] = p_m(j/n)$. Für negative $k$ nimmt man wegen der Periodizität $c_{-k} = y[n-k]/n$ (vgl. 5.3: Frequenz $n-k$ = Frequenz $-k$).

## 7 Spickzettel

> [!note] Ergänzung: Die wichtigsten Formeln auf einen Blick
> | | Formel |
> | --- | --- |
> | Einheitswurzel | $\omega_n = e^{-2\pi i/n}$ |
> | Basis-Schwingung | $\varphi_k[t] = e^{2\pi i k t/n}$ |
> | Orthogonalität | $\langle \varphi_k, \varphi_l \rangle = n$ falls $k = l$, sonst $0$ |
> | DFT | $y[k] = \sum_{t} x[t]\,\omega_n^{kt}$, $\ \mathbf{y} = \mathbf{F}_n \mathbf{x}$ |
> | IDFT | $x[t] = \frac{1}{n}\sum_{k} y[k]\,e^{2\pi i k t/n}$, $\ \mathbf{x} = \frac{1}{n}\mathbf{F}_n^H \mathbf{y}$ |
> | Energie | $\sum_t \lvert x[t] \rvert^2 = \frac{1}{n}\sum_k \lvert y[k] \rvert^2$ |
> | Aufwand | naiv $O(n^2)$, FFT $O(n \log n)$ |
