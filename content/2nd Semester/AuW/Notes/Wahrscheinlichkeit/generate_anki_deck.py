from __future__ import annotations

import csv
from pathlib import Path


try:
    import genanki  # type: ignore
except ImportError:
    genanki = None


DECK_NAME = "AuW Wahrscheinlichkeit"
OUT_DIR = Path(__file__).resolve().parent
TSV_PATH = OUT_DIR / "AuW_Wahrscheinlichkeit_Anki.tsv"
APKG_PATH = OUT_DIR / "AuW_Wahrscheinlichkeit_Anki.apkg"


def card(front: str, back: str, tags: str) -> dict[str, str]:
    return {"front": front.strip(), "back": back.strip(), "tags": tags.strip()}


CARDS = [
    card("Was ist ein diskreter Wahrscheinlichkeitsraum?", "Eine Ergebnismenge $\\Omega$ von Elementarereignissen mit Wahrscheinlichkeiten, die alle $\\ge 0$ sind und zusammen 1 ergeben.", "grundlagen open"),
    card("Wie berechnet man in einem Laplace-Raum $P(E)$?", "$P(E)=\\frac{|E|}{|\\Omega|}$.", "grundlagen open"),
    card("Was ist die Definition von bedingter Wahrscheinlichkeit?", "$P(A\\mid B)=\\frac{P(A\\cap B)}{P(B)}$ für $P(B)>0$.", "bedingt open"),
    card("Was ist der Satz der totalen Wahrscheinlichkeit?", "$P(B)=\\sum_i P(B\\mid A_i)P(A_i)$ für eine disjunkte Zerlegung $A_i$ von $\\Omega$.", "bedingt open"),
    card("Was ist die Bayes-Formel?", "$P(A_i\\mid B)=\\frac{P(B\\mid A_i)P(A_i)}{\\sum_j P(B\\mid A_j)P(A_j)}$.", "bedingt open"),
    card("Wie prüft man Unabhängigkeit von zwei Ereignissen am schnellsten?", "Mit $P(A\\cap B)=P(A)P(B)$.", "unabhaengigkeit open"),
    card("Was ist eine Zufallsvariable?", "Eine Funktion, die jedem Versuchsausgang eine Zahl zuordnet.", "zufallsvariable open"),
    card("Wie lautet die gebräuchliche Formel für den Erwartungswert?", "$E(X)=\\sum_{\\alpha\\in W_X} \\alpha\\,P(X=\\alpha)$.", "erwartungswert open"),
    card("Was ist die Tail-Sum-Formula?", "Für $X\\in\\mathbb N_0$: $E(X)=\\sum_{i=1}^{\\infty} P(X\\ge i)$.", "erwartungswert open"),
    card("Wie lautet eine praktische Formel für die Varianz?", "$\\operatorname{Var}(X)=E(X^2)-(E(X))^2$.", "varianz open"),
    card("Wie lautet die Formel der Binomialverteilung?", "$P(X=k)=\\binom{n}{k}p^k(1-p)^{n-k}$.", "verteilungen open"),
    card("Wie lautet die Formel der geometrischen Verteilung?", "$P(X=k)=p(1-p)^{k-1}$ für $k\\ge1$.", "verteilungen open"),
    card("Wie lautet die Formel der negativen Binomialverteilung?", "$P(X=k)=\\binom{k-1}{n-1}p^n(1-p)^{k-n}$.", "verteilungen open"),
    card("Wie lautet die Formel der Poisson-Verteilung?", "$P(X=k)=\\frac{\\lambda^k e^{-\\lambda}}{k!}$.", "verteilungen open"),
    card("Wie lautet die Faltungsformel für $Z=X+Y$ bei unabhängigen diskreten Zufallsvariablen?", "$f_Z(\\alpha)=\\sum_{\\beta\\in W_X} f_X(\\beta)f_Y(\\alpha-\\beta)$.", "mehrerezv open"),
    card("Was sagt die Waldsche Identität?", "Für $Z=\\sum_{i=1}^{N}X_i$ mit unabhängigem $N$ gilt $E(Z)=E(N)\\,E(X)$.", "mehrerezv open"),
    card("Was ist die Markov-Ungleichung?", "Für nichtnegative $X$ und $t>0$: $P(X\\ge t)\\le \\frac{E(X)}{t}$.", "abschaetzungen open"),
    card("Was ist die Chebyshev-Ungleichung?", "Für $t>0$: $P(|X-E(X)|\\ge t)\\le \\frac{\\operatorname{Var}(X)}{t^2}$.", "abschaetzungen open"),
    card("Welche Verteilung passt zu: Anzahl Erfolge in $n$ unabhängigen Versuchen mit gleicher Erfolgswahrscheinlichkeit?", "Binomialverteilung.", "szenario open"),
    card("Welche Verteilung passt zu: Versuchsnummer des ersten Erfolgs?", "Geometrische Verteilung.", "szenario open"),
    card("Welche Verteilung passt zu: Versuchsnummer des $r$-ten Erfolgs?", "Negative Binomialverteilung.", "szenario open"),
    card("Welche Verteilung passt zu: Anzahl seltener Ereignisse pro Zeitintervall?", "Poisson-Verteilung.", "szenario open"),
    card("Wahr oder falsch: Für jedes Ereignis $A$ gilt $P(\\overline A)=1-P(A)$.", "Wahr.", "tf grundlagen"),
    card("Wahr oder falsch: In einem Laplace-Raum haben alle Elementarereignisse dieselbe Wahrscheinlichkeit.", "Wahr.", "tf grundlagen"),
    card("Wahr oder falsch: Für disjunkte Ereignisse $A,B$ gilt immer $P(A\\cup B)=P(A)+P(B)-P(A\\cap B)$, also hier einfach $P(A)+P(B)$.", "Wahr.", "tf grundlagen"),
    card("Wahr oder falsch: Wenn $A\\subseteq B$, dann ist immer $P(A)\\ge P(B)$.", "Falsch. Es gilt $P(A)\\le P(B)$.", "tf grundlagen"),
    card("Wahr oder falsch: Bei Formulierungen wie \"mindestens einmal\" ist das Komplement oft der einfachste Weg.", "Wahr.", "tf strategie"),
    card("Wahr oder falsch: Unabhängigkeit von $A$ und $B$ bedeutet $P(A\\mid B)=P(A)$.", "Wahr.", "tf unabhaengigkeit"),
    card("Wahr oder falsch: Disjunkte Ereignisse sind automatisch unabhängig.", "Falsch.", "tf unabhaengigkeit"),
    card("Wahr oder falsch: Für unabhängige Ereignisse gilt $P(A\\cap B)=P(A)P(B)$.", "Wahr.", "tf unabhaengigkeit"),
    card("Wahr oder falsch: Für alle Zufallsvariablen gilt $E(X+Y)=E(X)+E(Y)$.", "Wahr.", "tf erwartungswert"),
    card("Wahr oder falsch: Für $E(XY)=E(X)E(Y)$ braucht man im Allgemeinen Unabhängigkeit.", "Wahr.", "tf erwartungswert"),
    card("Wahr oder falsch: Für eine Indikatorvariable $I_A$ gilt $E(I_A)=P(A)$.", "Wahr.", "tf erwartungswert"),
    card("Wahr oder falsch: Die Tail-Sum-Formula gilt ohne weitere Voraussetzung für jede reellwertige Zufallsvariable.", "Falsch. In den Notizen nur für Wertebereich in $\\mathbb N_0$.", "tf erwartungswert"),
    card("Wahr oder falsch: $\\operatorname{Var}(aX+b)=a^2\\operatorname{Var}(X)$.", "Wahr.", "tf varianz"),
    card("Wahr oder falsch: Für alle Zufallsvariablen gilt $\\operatorname{Var}(X+Y)=\\operatorname{Var}(X)+\\operatorname{Var}(Y)$.", "Falsch. So in den Notizen nur bei Unabhängigkeit.", "tf varianz"),
    card("Wahr oder falsch: Eine Bernoulli-Zufallsvariable nimmt nur die Werte 0 und 1 an.", "Wahr.", "tf verteilungen"),
    card("Wahr oder falsch: Die geometrische Verteilung modelliert den Zeitpunkt des ersten Erfolgs.", "Wahr.", "tf verteilungen"),
    card("Wahr oder falsch: Die negative Binomialverteilung modelliert den Zeitpunkt des ersten Erfolgs.", "Falsch. Sie modelliert den Zeitpunkt des $n$-ten Erfolgs.", "tf verteilungen"),
    card("Wahr oder falsch: Für die Poisson-Verteilung gilt $E(X)=\\operatorname{Var}(X)=\\lambda$.", "Wahr.", "tf verteilungen"),
    card("Wahr oder falsch: Die Markov-Ungleichung setzt Nichtnegativität von $X$ voraus.", "Wahr.", "tf abschaetzungen"),
    card("Wahr oder falsch: Die Chebyshev-Ungleichung benutzt die Varianz, um Abweichungen vom Erwartungswert abzuschätzen.", "Wahr.", "tf abschaetzungen"),
]


def write_tsv() -> None:
    with TSV_PATH.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(["Front", "Back", "Tags"])
        for note in CARDS:
            writer.writerow([note["front"], note["back"], note["tags"]])


def write_apkg() -> bool:
    if genanki is None:
        return False

    model = genanki.Model(
        1744582101,
        "AuW Wahrscheinlichkeit Basic",
        fields=[
            {"name": "Front"},
            {"name": "Back"},
            {"name": "Tags"},
        ],
        templates=[
            {
                "name": "Karte 1",
                "qfmt": "{{Front}}",
                "afmt": "{{FrontSide}}<hr id=\"answer\">{{Back}}",
            }
        ],
        css="""
.card {
  font-family: Arial, sans-serif;
  font-size: 20px;
  text-align: left;
  color: black;
  background-color: white;
}
""",
    )

    deck = genanki.Deck(1312457812, DECK_NAME)
    for note in CARDS:
        deck.add_note(
            genanki.Note(
                model=model,
                fields=[note["front"], note["back"], note["tags"]],
                tags=note["tags"].split(),
            )
        )

    genanki.Package(deck).write_to_file(APKG_PATH)
    return True


def main() -> None:
    write_tsv()
    apkg_created = write_apkg()
    print(f"Wrote {len(CARDS)} cards to {TSV_PATH.name}")
    if apkg_created:
        print(f"Wrote {APKG_PATH.name}")
    else:
        print("Skipped .apkg packaging because genanki is not installed")


if __name__ == "__main__":
    main()
