# Ortogonalidad 2.1.7
Es cuando el producto punto entre los dos vectores es cero

La norma de que la norma al cuadrado de un vector es igual al producto punto de el mismo es a su vez tambien igual a al integral de 0 y 1 con la función al cuadrado

## Espacios vectoriales y ortogonalidad.
2 espacios vectoriales son ortogonales si todos los los vectores de un espacio son ortogonales a todos los vectores del espacio

# Complemento ortogonal
Si el plano es infinito en X y otro plano es infinito en Y al sumarlos de forma directa resultará que todo el plano R^2, si cumple para todo entonces se le conoce que tiene complemento ortogonal del otro y es simetrico

V2 es complemento ortogonal de V1  
![Image](/images/complement&#32;ortogonal.png)

## Cartesian coordinates and geomtrical properties of Vectors
Suponga que los vectores son como segmentos que tienen un punto en común, lo que importa de los vectores es su magnitud y su dirección

## Proyecciones 2.2.2
La proyección del vector y contra el vector x es:
![Image](/images/projection&#32;vector.png)

Proyectar quiere decir que de un vector con respecto a otro determinar otro vector que genere un angulo recto.

Esta definición es una interpretación geoemtra de dos vectores dirigidos

![Image](/images/projections&#32;and&#32;angles.png)

Para obtener un vector que sea ortogonal de otro es por medio de un vector residual

### Grand Smith
Una de las ortogonalizaciones es con este metodo por medio de la sumatoria de la sumatoria de las proyecciones (xi dot xk) por xi xk es el proyecto que se dsea proyectar dividido por su norma para que asi normalice

![Image](/images/ortonormalization&#32;grand&#32;smith.png)


## Orthonormal Basis sets 2.2.5
Base es que de un vector **x** dado puede obtenerse una combinación lineal de dicha base, la base de un vector orthonormal se le llama *coeficiente de Fourier*.

## Approximation of vectors 2.2.6
Es vectores de altas dimensiones, son complejos para hacer computo, para trabajarlos más facilmente se puede aplicar una especie de reducción de dimensión.

### Aproximacion forma 1
Una forma para aproximar el vector es
* Conseguir un conjunto de vectores que sea una **base** ortonormal para el plano que se requiere determinar (por medio de gran smith), normalmente este plano está delimitado por un conjunto de vectores. Esos vectores son de magnitud 1 (normalizados)
* Tomar el vector que se desea aproximar y se aplica producto punto contra el vector ortonormal, cada uno de los vectores obtiene los coeficientes de Fourier

### Aproximación choice of th e best basis subset
De un conjunto de sub-espacios ¿Cual será el mejor sub-espacio en la Dimensión R^n para elegir el mejor vector para aproximar.

Suponga que se tiene una expansión de x de un conjunto ortogonal con n bases, los mejores **k** vectores de ese conjunto son los elegidos, para elegirlos se utiliza los valores más representativos por medio de lso coeficientes de Fourier.



# Matrices Scalar-valued operators on Square matrices 3.1.4
## The trace
Se tiene una variedad de mapeos utiles de matrices de numeros reales, estos provienen de R^(n*m) a R.

La traza es la suma de los elementos diagonales de una matriz.

## El determinante
Considerese el producto de una permutación de la matrix A,

Se toma la permutación de una sola fila y se lee la fila elemento por elemento y por cada ocurrencia que sea menor este sumará +1 dependiendo del total se indicará si es par o impar

Se establece todas las permutaciones posibles (su valor es el indice) tal como se indica en la imagen es el proceso

![Image](/images/determinant&#32;permutation.jpeg)

Una propiedad del determinante es que el determinante de una matriz de una matroiz triangular es solo multiplicando su diagonal ya que sus permutaciones resultarán cero exceptuando su diagonal.

# Minors, Cofactors, and Adjugate Matrices

## Minors
Los minors son la obtención de los determinantes "eliminando" filas y columnas y calcular su determinante (quedando una matrix de menor tamaño).

## Cofactors
Los Cofactores son la detemrinación o detección del signo por medio de a_ij --> (-1)^(i+j), tambien se conoce como la expansión de laplace


# AXPY
Si se aplica un ax+y a una matrix, el determinante es el mismo siempre

AXPY no es mas que la multiplicación de una fila de la matriz y luego sumarla, el fin de est eproceos es reducir la matriz a unadiagonal (gaus jordan)

Toma la fila **x**, multipliquela por **a** y luego la suma a la fila **y**
E_yx(a)

Tome la fila 1 multipliquela por -2 y sumela a la fila 2
E21(-2)

De esta manera la matriz se va reduciendo.

---

En matematicas las funciones trigonometricas, logaritmaticas, exponenciales son funciones **trascendentales**