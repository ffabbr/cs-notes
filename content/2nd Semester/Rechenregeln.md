## 1. Potenzen 

- $a^m \cdot a^n = a^{m+n}$
- $\frac{a^m}{a^n} = a^{m-n}$
- $(a^m)^n = a^{m \cdot n}$
- $(ab)^n = a^n \cdot b^n$
- $\left(\frac{a}{b}\right)^n = \frac{a^n}{b^n}$
- $a^{-n} = \frac{1}{a^n}$
- $a^{0} = 1 \quad (a \neq 0)$

---

## 2. Wurzeln

- $\sqrt[n]{a} = a^{\tfrac{1}{n}}$
- $\sqrt[n]{a^m} = a^{\tfrac{m}{n}}$
- $\sqrt{ab} = \sqrt{a} \cdot \sqrt{b} \quad (a,b \geq 0)$
- $\frac{\sqrt{a}}{\sqrt{b}} = \sqrt{\tfrac{a}{b}} \quad (b \neq 0)$

---

## 3. Logarithmen

- Definition: $\log_a(b) = x \iff a^x = b$
- $\log_a(1) = 0$
- $\log_a(a) = 1$
- $\log_a(bc) = \log_a(b) + \log_a(c)$
- $\log_a\!\left(\tfrac{b}{c}\right) = \log_a(b) - \log_a(c)$
- $\log_a(b^n) = n \cdot \log_a(b)$
- Basiswechsel: $\log_a(b) = \tfrac{\ln(b)}{\ln(a)}$
- $\ln\left(\frac{a}{b}\right) = \ln\left(\left(\frac{b}{a}\right)^{-1}\right) = -\ln\left(\frac{b}{a}\right)$

---

## 4. Natürlicher Logarithmus & Exponentialfunktion

- $\ln(e) = 1$
- $\ln(1) = 0$
- $e^{\ln(a)} = a$
- $\ln(e^x) = x$
- $e^{a+b} = e^a \cdot e^b$
- $e^{-x} = \tfrac{1}{e^x}$
- $\ln\left(\frac{a}{b}\right) = \ln\left(\left(\frac{b}{a}\right)^{-1}\right) = -\ln\left(\frac{b}{a}\right)$

---

## 6. Sonderfälle & nützliche Identitäten

- $\ln(ab) = \ln(a) + \ln(b)$
- $\ln\!\left(\tfrac{a}{b}\right) = \ln(a) - \ln(b)$
- $\ln(a^n) = n \ln(a)$
- $\ln\!\left(\sqrt[n]{a}\right) = \tfrac{1}{n} \ln(a)$
- $\sqrt[n]{a} = e^{\tfrac{1}{n}\ln(a)}$

---

## 6. Limes-Regeln

- $\lim_{x \to x_0} (c \cdot f(x)) = c \cdot \lim_{x \to x_0} f(x)$
- $\lim_{x \to x_0} (f(x) \cdot g(x)) = \left( \lim_{x \to x_0} f(x) \right) \cdot \left( \lim_{x \to x_0} g(x) \right)$
- $\lim_{x \to x_0} (f(x) \pm g(x)) = \lim_{x \to x_0} f(x) \pm \lim_{x \to x_0} g(x) = A \pm B$
- $\lim_{x \to x_0} \frac{f(x)}{g(x)} = \frac{\lim_{x \to x_0} f(x)}{\lim_{x \to x_0} g(x)} = \frac{A}{B} \quad (\text{für } B \neq 0)$
- $\lim_{x \to x_0} (f(x))^n = (\lim_{x \to x_0} f(x))^n = A^n$

- $\lim_{x \to \infty} \tfrac{1}{x} = 0$
- $\lim_{x \to \infty} \tfrac{1}{x^n} = 0 \quad (n>0)$
- $\lim_{x \to \infty} \left(1+\tfrac{1}{x}\right)^x = e$
- $\lim_{x \to 0} \tfrac{\sin x}{x} = 1$
- $\lim_{x \to 0} \tfrac{1 - \cos x}{x^2} = \tfrac{1}{2}$
- $\lim_{x \to 0} \tfrac{\ln(1+x)}{x} = 1$

---

## 8. Wachstum und co. 

- $ln(n!) \leq O(n*ln(n))$
- $n! \leq n^n$

**Wachstumsvergleich** für $x \to \infty$:  
$\ln(x) \ll x^a \ll a^x \ll x! \ll x^x$


---


![[Formelheft Ableitungen.png]]