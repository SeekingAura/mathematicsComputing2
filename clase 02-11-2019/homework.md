## Punto 1
¿Cual es la eficiencia computacional de la eliminación gaussiana?

Mirar Computational Efficiency of Gaussian Elimination

Example 1.28

Leerlo y entenderlo

**Flop:** Son opoeraciones de punto flotante que se requieren para resolver una función o ecucación, las operaciones basicas como +, -, \*, / son operaciones de punto flotante, cada operador requiere de dos operandos, es decir que la suma de 3+2 es 1 flop, ahora si la operación matematica tiene 2 operadores como 1+2*x dene resolverse primero la multiplicación sumando 1 flop quedando 1+result y luego el resultado de la multiplicación es sumado siendo asi 2 flops, teniendo encuenta esto las operaciones de punto flotante serian

```python
import math

1+math.pi()             # one flop
1*math.pi()             # one flop
1+math.pi()*27.1        # two flops
math.pi()**4            # three flops
1+math.pi()*math.exp(2) # three flops
1+math.pi()*math.exp(3) # fourth flops
```

se verificará cuantos flops la multiplicación una fila con otra, en la eliminación gausiana, dando filas con **n** elementos.


n-1 -> Es la cantidad de operaciones que se hace por fila para eliminar ceros

2n -> es la cantidad de operaciones que hace el axpi para multiplicartla fila

## Columnas
la primera columna require n-1 flops, la segunda requeire n-2 flops y asi hasta ser igual a la cantidad n

## Rows
Las operaciones de flops se da por los axpi con 2n+1, el +1 es para detemrinar lo que debe multipicar por el pivote para quitar el valor cero de su posición actual, como en cada fila se reduce la cantidad de columnas para la segunda seria 2(n-1)+1, tercera 2(n-2)+1 y asi

la sumatoria que representa este comportamiento es

sum((j-1)(2j+1))
para j=1 hasta n

las priemras iteraciones corresponen a las ultimas operaciones de la reducción gaussiana

# Punto 2
https://es.wikipedia.org/wiki/M%C3%A9todo_Montante

https://en.wikipedia.org/wiki/LU_decomposition

https://en.wikipedia.org/wiki/System_of_linear_equations

https://en.wikipedia.org/wiki/Jacobi_method
