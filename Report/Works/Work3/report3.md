# Работа №3
## a) $\quad F = -8x_1 + 3x_2 \to \min (\max)$ 
$$
\begin{align*}
& \begin{cases}
x_1 + 2x_2 \leq 14 \\
-4x_1 + 3x_2 \leq 12 \\
x_1 \leq 6 \\
x_1 \geq 0, \quad x_2 \geq 0
\end{cases}
\end{align*}
$$
#### Решим сначала на максимум:
**Решение исходной задачи**:
   $x_{max}=(0, 4)$
##### Формулировка двойственной задачи:

1. **Целевая функция**:
   $F^* = 14y_1 + 12y_2 + 6y_3 \to \min$
2. **Ограничения**:
$$
   \begin{cases}
   y_1 - 4y_2 + y_3 \geq -8 \\
   2y_1 + 3y_2 \geq 3 \\
   y_1 \geq 0, \quad y_2 \geq 0, \quad y_3 \geq 0
   \end{cases}
$$
##### Решение
$$
\begin{cases}
(x_1 + 2x_2 - 14) y_1^* = 0 \\
(-4x_1 + 3x_2 - 12) y_2^* = 0 \\
(x_1 - 6) y_3^* = 0 \\
\end{cases}
$$
$$
\begin{cases}
(0 + 2*4 - 14) y_1^* = 0 => y_1^* = 0 \\
(-4 * 0 + 3 * 4 - 12) y_2^* = 0 => y_2^* > 0 \\
(0 - 6) y_3^* = 0 => y_3^* = 0\\
\end{cases}
$$
###### Теорема о дополняющей нежесткости:
Если $x_1$ и $x_2$ — оптимальное решение прямой задачи, а $y_1$, $y_2$, $y_3$ — оптимальное решение двойственной задачи, то:

1. $x_1(y_1 - 4y_2 + y_3 + 8) = 0$
2. $x_2(2y_1 + 3y_2 - 3) = 0$

Из решения прямой задачи:
$$
\begin{cases}
0 \cdot (y_1 - 4y_2 + y_3 + 8) = 0 \\
4 \cdot (2y_1 + 3y_2 - 3) = 0 \\
\end{cases}
=> y^*=(0, 1, 0) \text{ - Оптимальное решение двойственной задачи} \\
$$
$$
F^* = 14 \cdot 0 + 12 \cdot 1 + 6 \cdot 0 = 12
$$

#### Решим на максимум через теорему 3
Берем данных из последней таблицы решения этого номера в работе 2
$$
y^* = 
\begin{pmatrix}
0 & 3 & 0
\end{pmatrix}
\cdot
\begin{pmatrix}
1 & -0.67 & 0 \\
0 & 0.33 & 0 \\
0 & 0 & 1
\end{pmatrix}
= (0, 1, 0)
$$
Получили то же самое
#### Решим теперь на минимум. Решим так же, находя максимум функции G=-F.
**Решение исходной задачи**:
   $x_{max}=(6, 0)$
##### Прямая задача:
$$
G = 8x_1 - 3x_2 \to \max
$$
$$
\begin{cases}
x_1 + 2x_2 \leq 14 \\
-4x_1 + 3x_2 \leq 12 \\
x_1 \leq 6 \\
x_1 \geq 0, \quad x_2 \geq 0
\end{cases}
$$
##### Двойственная задача:
1. **Целевая функция**:
   $G^* = 14y_1 + 12y_2 + 6y_3 \to \max$
2. **Ограничения**:
$$
   \begin{cases}
   y_1 - 4y_2 + y_3 \geq 8 \\
   2y_1 + 3y_2 \geq -3 \\
   y_1 \geq 0, \quad y_2 \geq 0, \quad y_3 \geq 0
   \end{cases}
$$
##### Решение
$$
\begin{cases}
(x_1 + 2x_2 - 14) y_1^* = 0 \\
(-4x_1 + 3x_2 - 12) y_2^* = 0 \\
(x_1 - 6) y_3^* = 0 \\
\end{cases}
$$
$$
\begin{cases}
(6 + 2 * 0 - 14) y_1^* = 0 => y_1^* = 0 \\
(-4 * 6 + 3 * 0 - 12) y_2^* = 0 => y_2^* = 0 \\
(6 - 6) y_3^* = 0 => y_3^* > 0 \\
\end{cases}
$$
###### Теорема о дополняющей нежесткости:
Если $x_1$ и $x_2$ — оптимальное решение прямой задачи, а $y_1$, $y_2$, $y_3$ — оптимальное решение двойственной задачи, то:

1. $x_1(y_1^* - 4y_2^* + y_3^* + 8) = 0$
2. $x_2(2y_1^* + 3y_2^* - 3) = 0$

Из решения прямой задачи $x_1 = 6$ и $x_2 = 0$:

$$
\begin{cases}
6 \cdot (y_1^* - 4y_2^* + y_3^* - 8) = 0 \\
0 \cdot (2y_1^* + 3y_2^* + 3) = 0 \\
\end{cases}
=> y^*=(0, 0, 8) \text{ - Оптимальное решение двойственной задачи} \\
$$
$$
G^* = 14 \cdot 0 + 12 \cdot 0 + 6 \cdot 8 = 48  => 
F^* = -G^* = -48
$$



## b) $\quad F = 2x_1 + x_2 \to \min (\max)$
$$
\begin{align*}
& \begin{cases}
2x_1 + x_2 \geq 10 \\
-4x_1 + x_2 \leq 8 \\
x_1 \geq 0, \quad x_2 \geq 0
\end{cases}
\end{align*}
$$
$\nexists F_{max}$
#### Решим теперь на минимум. Решим так же, находя максимум функции G=-F.
**Решение исходной задачи**:
   $x_{max}=(5, 0)$
#### Прямая задача:
$$
G = -2x_1 - x_2 \to \max
$$
$$
\begin{align*}
& \begin{cases}
-2x_1 - x_2 \leq -10 \\
-4x_1 + x_2 \leq 8 \\
x_1 \geq 0, \quad x_2 \geq 0
\end{cases}
\end{align*}
$$
#### Двойственная задача:
1. **Целевая функция**:
   $G^* = -10y_1 + 8y_2 \to \max$
2. **Ограничения**:
$$
   \begin{cases}
   -2y_1 - 4y_2 \geq -2 \\
   -y_1 + y_2 \geq -1 \\
   y_1 \geq 0, \quad y_2 \geq 0
   \end{cases}
$$
##### Решение
$$
\begin{align*}
& \begin{cases}
(-2x_1 - x_2 + 10)y_1^*=0 \\
(-4x_1 + x_2 - 8)y_2^*=0 \\
\end{cases}
\end{align*}
$$
$$
\begin{align*}
& \begin{cases}
(-2 \cdot 5 - 0 + 10)y_1^*=0 => y_1^* > 0 \\
(-4 \cdot 5 + 0 - 8)y_2^*=0 => y_2^* = 0 \\
\end{cases}
\end{align*}
$$
###### Теорема о дополняющей нежесткости:
1. $x_1(-2y_1 - 4y_2 + 2) = 0$
2. $x_2(-y_1 + y_2 + 1) = 0$

Из решения прямой задачи:
$$
\begin{cases}
5 \cdot (-2y_1 - 4y_2 + 2) = 0 \\
0 \cdot (-y_1 + y_2 + 1) = 0 \\
\end{cases}
=> y^*=(1, 0) \text{ - Оптимальное решение двойственной задачи} \\
$$
$$
G^* = -10 \cdot 1 + 8 \cdot 0 = -10  => 
F^* = -G^* = 10
$$
## c) $\quad F = 2x_1 - x_2 \to \min (\max)$
$$
\begin{align*}
& \begin{cases}
3x_1 - x_2 \geq 21 \\
x_1 \leq 2 \\
x_1 \geq 0, \quad x_2 \geq 0
\end{cases}
\end{align*}
$$
$\nexists F_{min}$, $\nexists F_{max}$,