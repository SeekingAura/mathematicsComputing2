# matrix appilcations transformations

## Scaling
El escalado para puntos en 2D, los valores de la matriz identidad toma efecto en los ejes, pero los otros valores de la matriz debe ser cero

```python
[
    [3/2, 0],
    [0, 1/2]
]
```
La matriz anterior escala en x al 3/2 y en y al 1/2

## Shearing
El shearing su definición es el trasquilado el cual  toma efecto dependiendo del número superior de la derecha se haga, la diagonal debe ser 1 para que no tenga efectos de escalado
```python
[
    [1, 1],# el segundo valor es el shearing
    [0, 1]
]
```
La imagen ilustra el efecto

![Image](/images/shearing&#32;matrix.jpeg)
shearing matrix.jpeg


# Traslación

Las traslaciones se realiza con una dimensión adicional y se coloca lo que se va desplazar respecto a la posición actual por ejemplo, si se quiere pasar del origen a desplazarse en 30 grados se ilustra en la siguiente imagen

![Image](/images/translation.jpeg)

# Ortogonalidad en matrices
la ortogonalidad entre vectores es que formen un angulo recto entre si, pero en el de matrices es que si su transpuesta es igual a su inversa
![Image](/images/example&#32;of&#32;orthogonal&#32;matrix.jpeg)

Dado una matrix que es orotogonal de nxn y **x** y **y** pertenecen al plano R^n

# Householder matrix
Esta matrix permite obtener una reflección de un plano en el efecto de un juego seria el efecto espejo

# Change of basis and linear operators
Está el universo de las matrices mxn esa matric puede ser itnerpretada como una transformación lineal que va de vectores de dimensión R^n (columnas d el amatrix) a vectores de dimensión R^m (filas d ela matrix), a su vez tambien se puede pasar de una transofmriacón lineal a matrices mxn, pero es muy importante tener en cuenta la **base**...


![Image](/images/change&#32;of&#32;basis.jpeg)


# El rango y el núcleo de una tranformación
El kernel de una tranformación se define como el conjunto de todos los vectores que dan como resultado cero.

Es el conjunto de vectores que al aplicar una transformación se convierte en un vector de ceros

Se calcula aplicando gauss jordan a la matriz correspondiente de transformación (obtenida de alguna operación de base)

![Image](/images/kernel&#32;part&#32;1.jpeg)

La ecuación resultante y los vectores con sus co mbionaciones nieales que dan para ste caso corresponden al kernel
![Image](/images/kernel&#32;part&#32;2.jpeg)

## Range
Es el conjunto de los vectores transformados que son imagen de los vectores sin tranformar, es decir que de un vector sin transformar al trasnformarlo se llega a esos vectores transformados, uno de los valores de ese range es el vector transformado al quitarle la transformación


Para su calculo se toma el resultado de la reducción gauss jordan y se miran las columnas que tienen pivote (columnas marcadas de rojo)
![Image](/images/range&#32;part&#32;1.jpeg)

Luego en esas posiciones correspondientes se toman las columnas de la matriz base (a la uqe se hizo el gauss jordan)
![Image](/images/range&#32;part&#32;2.jpeg)

Finalmente esas columnas se toman como vectores y las combinaciones lineales de estas son el range
![Image](/images/range&#32;part&#32;3.jpeg)


