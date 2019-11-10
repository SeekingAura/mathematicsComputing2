# Rules of matrix

## Determinant of the Transpose of square matrices
El determinante de una matrix es igual al determinante de esa matriz transpuesta

Retoamndo..

una el determinante de una matriz es igual a la multiplicación de las diagonales unicamente si tiene una parte triangular con ceros.


El determinante tambien es igual al determinante de las sub-matrices como se indica en la siguiente imagen

![Image](/images/determinant&#32;partioned.png)

![Image](/images/determinant&#32;partioned&#32;example.jpeg)

sen^2(tetha)+cos^2(tetha)=1

Una de las utilidades del determinant ees que en el caso de un vector de 2D es el area y en el caso de vectores de dimensión 3 calcula el volumen.

# Multiplication on matrix

## Elementary operations on matrices

* The interchange of two rows (columns)
* A sacalar multiplication of a given row (column)
* Replacement of a given row (column) by the sum of that row and a scalar multiple of another row (column); that is, an axpy operation (the proocess of gauss jordan)

Elementary operator matrix se utiliza para llevar a cabo operaciones.


si se multiplica con la matriz identidad se obtienen diferentes intercambios de la matrix por ejemplo

x=np.array([
		[3, 1, -1],
		[2, 0, 4],
		[5, -2, 1],
	]
)
Esta multiplicación es una Post-multiplicaction
```python
x=np.array([
		[3, 1, -1],
		[2, 0, 4],
		[5, -2, 1],
	]
)

ident=np.array([
		[0, 0, 1],
		[0, 1, 0],
		[1, 0, 0],
	]

# x * ident
print(np.matmul(ident,x))

### Outputs
# [[ 5 -2  1]
# [ 2  0  4]
# [ 3  1 -1]] 
)
```
si se mira bien es como si hubiera itnercambiado el orden de las filas, si se hace la multiplciación contraria se invierte las columnas. 

Esta amultiplicación es una Pre-multiplicaction
```python
x=np.array([
		[3, 1, -1],
		[2, 0, 4],
		[5, -2, 1],
	]
)

ident=np.array([
		[0, 0, 1],
		[0, 1, 0],
		[1, 0, 0],
	]

# ident * x
print(np.matmul(x,ident))

### Outputs
# [[ 3 -2 -1]
#  [ 2  0  4]
#  [ 5  4  1]]

)
```
Siguiendo estas normas se puede llegar a lo siguiente cone l operador asxpy

![Image](/images/asxpy&#32;on&#32;elementary&#32;matrix.jpeg)



Si en la matrix hay una elemental inversa el determinante es cambiado de signo
```python
determ=np.array([
		[0, 0, 1, 0],
		[0, 1, 0, 0],
		[1, 0, 1, 0],
        [0, 0, 0, 1]
	]
)
print(np.linalg.det(determ))
# Output
# -1.0
```
método para multiplicar una fila de una matriz por medio de la matriz elemental
![Image](/images/multiply&#32;row&#32;matrix&#32;with&#32;matrix.jpeg)

Asi mismo hay una propiedad para determinar su fdeterminante si es que llega a ser multiplicado
![Image](/images/determinant&#32;of&#32;multiply&#32;row.jpeg)


## Inversa de una matriz
el proceso de gauss jordan para llegar a la matriz identidad son las operaciones necesarias para obtener la matriz inversa.

una propiedad que aplica en este caso es el siguiente
![Image](/images/propertie&#32;determinant&#32;matrix&#32;inverse.jpeg)



# Linear systems of equations
un sistem ade ecucaicones lienale sson aquellos sistemas devariables las cuales no tienen cuadrados, reaices, angulos nada de ese estilo, por ejemplo

a_11x_11+a_12x_12....

## Sistemas nxn
El caso más base es que la cantidad de ecuaciones sea la misma cantidad de variables, estos problemas tienen multiples formas de tratamiento.

### Homogeneas
los sistemas homogeneos son aquellos que su lado derecho de la igualdad sea 0, en este se puede presentar el caso de
* Unica solución donde todas las variables son cero
* Infinitas soluciones

Por medio de las reglas de las matrices se puede determinar si un sistema homogeneo tiene unica o infinitas solucion por medio del dterminante
* Si determinante es diferente de cero es unica solución
* Si el determinante es cero tiene infinitas soluciones

#### caso de infinitas
Con transformaciones elementales de reducción de gauss se llega a un row echelon form.

Si en proceso de reducción de gauss resultan filas que son cero, deben quedar de último.




### Una propiedad de los determinantes
|A\*B|=|A|\*|B|

