## Ableitung mit imaginärem Schritt

Bekannt ist der Differenzenquotient:

$$
\boxed{
f'(x)\approx\frac{f(x+h)-f(x)}{h}
}
$$

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