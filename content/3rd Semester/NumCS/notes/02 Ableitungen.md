## Ableitung mit imaginärem Schritt

Bekannt ist der Differenzenquotient:

$$
\boxed{
f'(x)\approx\frac{f(x+h)-f(x)}{h}
}
$$

**Laufzeit:** $O(1)$, also 2 Auswertungen von $f$ pro Ableitung.

Multipliziert man mit $h$, erhält man:

$$
f(x+h)-f(x)\approx h f'(x)
$$

also

$$
f(x+h)\approx f(x)+h f'(x).
$$

Statt eines reellen Schrittes $h$ verwenden wir nun einen **imaginären Schritt** $ih$:

$$
f(x+ih)\approx f(x)+ihf'(x).
$$

Also

$$
\operatorname{Im}(f(x+ih))
\approx h f'(x).
$$

Und:

$$
\boxed{
f'(x)\approx
\frac{\operatorname{Im}(f(x+ih))}{h}
}
$$

**Laufzeit:** $O(1)$, also nur 1 (komplexe) Auswertung von $f$ pro Ableitung.

### Warum funktioniert das?

Betrachten wir die Taylorentwicklung:

$$
f(x+\Delta)
=
f(x)
+
f'(x)\Delta
+
\frac{f''(x)}{2}\Delta^2
+
\frac{f'''(x)}{6}\Delta^3
+\ldots
$$

Wir setzen

$$
\Delta=ih.
$$

Dann erhalten wir:

$$
f(x+ih)
=
f(x)
+
f'(x)(ih)
+
\frac{f''(x)}{2}(ih)^2
+
\frac{f'''(x)}{6}(ih)^3
+\ldots
$$

Da

$$
i^2=-1
\qquad\text{und}\qquad
i^3=-i,
$$

folgt:

$$
f(x+ih)
=
\underbrace{f(x)}_{\text{reell}}
+
\underbrace{ihf'(x)}_{\text{imaginär}}
-
\underbrace{\frac{h^2}{2}f''(x)}_{\text{reell}}
-
\underbrace{i\frac{h^3}{6}f'''(x)}_{\text{imaginär}}
+\ldots
$$

Wir können Real- und Imaginärteil zusammenfassen:

$$
f(x+ih)
=
\underbrace{
\left(
f(x)-\frac{h^2}{2}f''(x)+\ldots
\right)
}_{\text{Realteil}}
+
i
\underbrace{
\left(
hf'(x)-\frac{h^3}{6}f'''(x)+\ldots
\right)
}_{\text{Imaginärteil}}.
$$

Der Imaginärteil ist daher:

$$
\operatorname{Im}(f(x+ih))
=
hf'(x)
-
\frac{h^3}{6}f'''(x)
+\ldots
$$

Teilen durch $h$:

$$
\frac{\operatorname{Im}(f(x+ih))}{h}
=
f'(x)
-
\frac{h^2}{6}f'''(x)
+\ldots
$$

Für kleines $h$ ist der Rest sehr klein. Somit:

$$
\boxed{
\frac{\operatorname{Im}(f(x+ih))}{h}
\approx f'(x)
}
$$

```python
def diffih(f,x, h0):
    nit = 60 # max depth of iterations
    h = np.zeros(nit); 
    h[0] = h0 # width of diff. quot.
    y = np.zeros(nit)
    # TODO: implement here the complex imaginary step formula
    
    for k in range(nit):
      y[k] = np.imag(f(x+1j*h[k]))/h[k]
      
      if (k < (nit-1)):
        h[k+1] = h[k]/2
    
    return y, h
```

**Laufzeit:** $O(\text{nit})$, eine Auswertung von $f$ pro Schrittweite $h_k$.

## Ableitung zweiter Ordnung

Wir schauen nach links und nach rechts, nehmen den Mittelwert. 

$$
\frac12\left(
\frac{f(x+h)-f(x)}h
+
\frac{f(x)-f(x-h)}h
\right)
$$
$$
\boxed{
f'(x)\approx
\frac{f(x+h)-f(x-h)}{2h}
}
$$

**Laufzeit:** $O(1)$, also 2 Auswertungen von $f$ pro Ableitung.

## Richardson Konvergenzbeschleunigung

Startend bei 

$$
D(h)=\frac{f(x+h)-f(x-h)}{2h}.
$$

Haben wir einen Fehler von 

$$
D(h) = f'(x) + C h^2 + \dots \tag{i}
$$

Wenn wir $D\left(\frac h2\right)$ berechnen sehen wir der Hauptfehler wurde 4x kleiner.

$$
D\left(\frac h2\right)
\approx
f'(x)+\frac14Ch^2
$$

1. **Mal 4 rechnen**  $4D(h/2)\approx4f'(x)+Ch^2.$
2. **Subtrahieren von (i)**  $4D(h/2)-D(h)\approx3f'(x).$ 
3. **durch 3 dividieren**

$$
\boxed{
f'(x)\approx
\frac{4D(h/2)-D(h)}{3}
}
$$

Jetzt ist der $h^2$ Fehler weg, der nächste größte Fehler ist $h^4$, dann $h^6$, etc. also wiederholen wir statt 4 mit 16, 64, 256, etc.

1. neuer grösster Fehler ist $h^4$
2. **h halbieren**   $\left(\frac h2\right)^4 = \frac{h^4}{16}.$
3. **also** $R_2(h)=\frac{16R_1(h/2)-R_1(h)}{15}$  

```python
# Richardson extrapolation; fixed level for vectorisation
def diffRichardsonV(f,x, h0, rtol=1e-12, atol=1e-12):
    nit = 30 # max depth of iterations
    h = h0/2**np.arange(nit)
    y = np.zeros(nit)
    y, _ = diffd2(f,x,h0)
    y = y[:nit]
    
    for k in range(1, nit):
      fact = 4**k
      y[k:] = (fact*y[k:] - y[k-1:-1]) / (fact-1)
      
      errest = abs(y[k] - y[k-1])
      if errest < atol and errest < rtol * abs(y[k]):
          break
    
    return y[:k+1], h[:k+1] 
```

**Laufzeit:** $O(\text{nit})$ Auswertungen von $f$ (für die zentralen Differenzen in `diffd2`) plus $O(\text{nit}^2)$ arithmetische Operationen für das Extrapolationsschema (Schritt $k$ aktualisiert $O(\text{nit}-k)$ Einträge). Bricht die Schleife nach $K$ Stufen ab, sind es nur $O(K\cdot\text{nit})$ Operationen.

