# The reduced row Echelon Form


# Rank and Nully of a mtraix
## Rank
Es rank es el numero de filas que no tienen valores cero (que tenga un valor por lo menos un valor cero) de la forma reducida de Echeleon

## Nullity
Es una matrix que su número de columnas que no tiene definido pivote (pivote es que tiene un 1 correspondiente cuando se hace el proceso de reducción)

## Max and min
la suma del rank y de la nullidad es igual al total de columnas de la matrix

## Full coluimn rank
Si el rango de una matrix es igual al número de columnas, la matrix es **full column rank**

## Consistency in terms of ranl
Se Obtiene el rank de la matrix y el de esa misma matrix pero aumentada (matrix aumentada es la matrix de un sistema lineal de ecucaciones junto con su lado del igual) con ello se peude determinar
```python
if rank(A)=n:
	print("Se tiene una unica solución")
elif rank(A)<n:
	print("Tiene infinitas soluciones")
elif rank(A)<rank(A~):
	print("es inconsistente")
```

* No hay solución -- Incosistente
* Unica solución -- Consistente
* Infinitas soluciones -- Consistente

Para verificar si un sistema tiene solución es verificando sus combinaciones lineales



# Tarea
## Punto 1
¿Cual es la eficiencia computacional de la eliminación gaussiana?

Mirar Computational Efficiency of Gaussian Elimination

Example 1.28

Leerlo y entenderlo

## Punto 2
Investigar si existen métodos más eficientes que gauss jordan para resolver sistemas de ecuaciones lineales?

Aplicaciones aritmeticas de la matrix


