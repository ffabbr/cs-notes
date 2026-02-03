```java 
// Mehrere Methoden mit gleichem Namen und unterschiedlicher Signatur möglich
public class Main {

    // Erste Version: Addiert zwei int-Werte
    public static int add(int a, int b) {
        return a + b;
    }

    // Überladene Version: Addiert drei int-Werte
    public static int add(int a, int b, int c) {
        return a + b + c;
    }

    // Überladene Version: Addiert zwei double-Werte
    public static double add(double a, double b) {
        return a + b;
    }

    // Beispiel-Main-Methode zum Testen
    public static void main(String[] args) {
        System.out.println(add(2, 3));        // Ausgabe: 5
        System.out.println(add(1, 2, 3));     // Ausgabe: 6
        System.out.println(add(2.5, 3.5));    // Ausgabe: 6.0
    }
}
```
