### Kurz

- **Primitive Typen** → *Value semantics*: `a = b;` kopiert den **Wert**.  
- **Referenztypen (nicht primitiv)** → *Reference semantics*: `a = b;` kopiert die **Referenz**, beide zeigen auf dasselbe Objekt. Wie ein Pfeil den man legt und verschiebt. Änderungen an nicht primitiven Typen sind auch "nach außen sichtbar" (außerhalb der Funktion)

### Lang 

| **Kategorie**     | **Primitives**                     | **Objekte**                                              |
| ----------------- | ---------------------------------- | -------------------------------------------------------- |
| Speicherart       | speichern tatsächlichen Wert       | speichern Referenz auf Speicherort                       |
| Grösse            | sind von der Grösse begrenzt       | Grösse ist variabel                                      |
| Standardwert      | Standardwerte sind festgelegt      | Standardwert ist *NULL* (keine Referenz in den Speicher) |
| NULL-Wert möglich | Können niemals *NULL* sein         | Können *NULL* sein                                       |
| Beispiele         | `int`, `double`, `boolean`, `char` | `String`, `Array`, `Scanner`, benutzerdefinierte Klassen |

