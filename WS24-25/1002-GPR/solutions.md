# Task 1
1. Ausführbarkeit: Each step of the process can be executed in a real manufacturing environment by machines and workers.

2. Allgemeingültigkeit: The instructions are applicable to the production of various car models because they describe basic and universal steps.

3. Determiniertheit: The instructions are mostly specific, but there are some areas that could be further clarified, such as precisely how the body parts should be placed onto the frame or in what order certain assembly steps should occur. Despite these minor gaps, the process in automotive manufacturing is generally well-structured and clearly defined.

4. Determinismus: At any given time, there is exactly one way to continue the algorithm.

5. Statische Finitheit: The description of the algorithm is finite (see description).

6. Dynamische Finitheit: The amount of materials used is finite.

7. Terminiertheit: The process clearly ends with the final quality check and the completion of the car.

# Task 2

```
1. Lese zwei Zahlen a, b ∈ N ein
2. Solange b≠0:
3. Setze h = a mod b
4. Setze a=b, b=h
5. Gib a als Ergebnis aus
```
It terminates, determinate (same input same output), deterministic (at all times a clear execution of code)

```
1. Setze a auf eine zufällige Zahl zwischen −20 und 20.
2. Setze a = a · a.
3. Wenn a > 15:
4. Gib a als Ergebnis aus
5. Sonst: Gehe zu Zeile 2
```
I doesnt terminate for -1,0,1; also deterministic; determinate because a random number is determinate within the algorithm

```
1. Lese zwei Zahlen n, m ∈ N ein.
2. Setze das Ergebnis s = 0.
3. Solange n > 0:
    a. Wenn n mod 2 = 1, setze s = s + m.
    b. Setze n = n ÷ 2 (ganzzahlig) und m = m x 2
4. Gib s als Ergebnis aus
```
Terminating:
The algorithm is terminating because in each step, 
𝑛
n is halved as an integer. Since 
𝑛
n is a natural number and decreases with each step, 
𝑛
n will eventually reach the value 0. At this point, the algorithm ends.

Determinate:
The algorithm is determinate because for the same input values n and m, it always calculates the same result s. There are no random elements or indeterminate decisions that could alter the course of the algorithm.

Deterministic:
The algorithm is deterministic because each step is clearly defined. At any point in time, it is clear which calculation will be performed based on the current values of n and m. There are no random decisions or unclear instructions.