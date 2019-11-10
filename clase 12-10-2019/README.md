# Metrics and distances
existen diferentes distrancias que está relacionado al de similaridad diciendo que tan lejos están.

## Distancia de Euclidiana
Es  la distancia que común que se utiliza para determinar 

<img src="https://latex.codecogs.com/png.latex?\large&space;x=\begin{pmatrix}&space;x_{1}&space;\\&space;\vdots&space;\\&space;x_{i}&space;\\&space;\vdots&space;\\&space;x_{n}&space;\\&space;\end{pmatrix}" title="\large x=\begin{pmatrix} x_{1} \\ \vdots \\ x_{i} \\ \vdots \\ x_{n} \\ \end{pmatrix}" />  
<img src="https://latex.codecogs.com/png.latex?\large&space;y=\begin{pmatrix}&space;y_{1}&space;\\&space;\vdots&space;\\&space;y_{i}&space;\\&space;\vdots&space;\\&space;y_{n}&space;\\&space;\end{pmatrix}" title="\large y=\begin{pmatrix} y_{1} \\ \vdots \\ y_{i} \\ \vdots \\ y_{n} \\ \end{pmatrix}" />

## Distancia Minkovski

caso <img src="https://latex.codecogs.com/png.latex?\large&space;p\geq&space;1" title="\large p\geq 1" />

<img src="https://latex.codecogs.com/png.latex?\large&space;\Delta&space;(x,y)=\left&space;(&space;\sum_{i=1}^{n}\left&space;|&space;x_{i}-y_{i}&space;\right&space;|&space;^{P}&space;\right&space;)&space;^{\frac{1}{p}}" title="\large \Delta (x,y)=\left ( \sum_{i=1}^{n}\left | x_{i}-y_{i} \right | ^{P} \right ) ^{\frac{1}{p}}" />  

Caso para 
<img src="https://latex.codecogs.com/png.latex?\large&space;p=1" title="\large p=1" />

<img src="https://latex.codecogs.com/png.latex?\large&space;\Delta&space;_{1}=\sum_{i=1}^{n}\left&space;|&space;x_{i}-y_{i}&space;\right&space;|" title="\large \Delta _{1}=\sum_{i=1}^{n}\left | x_{i}-y_{i} \right |" />

## Metrica manhattan



Dependiendo de la distancia como varia el modo de medir tambien varia su resultado, por ejemplo hacer una circunferencia con distnacia euclidiana de radio **r**, resulta una circunferia de curva fina, pero en cambio una circunferencia de radio **r** con distancia minkovski infinita resulta un cuadrado del tamaño **r** de la circunferencia


# Espacios euclidiano n-dimensional
Las operaciones con vectores tienen una serie de convenciones para escribir su operación:

## Suma
<img src="https://latex.codecogs.com/png.latex?\large&space;x=\begin{pmatrix}&space;x_{1}&space;\\&space;\vdots&space;\\&space;x_{i}&space;\\&space;\vdots&space;\\&space;x_{n}&space;\end{pmatrix}" title="\large x=\begin{pmatrix} x_{1} \\ \vdots \\ x_{i} \\ \vdots \\ x_{n} \end{pmatrix}" />

<img src="https://latex.codecogs.com/png.latex?\large&space;y=\begin{pmatrix}&space;y_{1}&space;\\&space;\vdots&space;\\&space;y_{i}&space;\\&space;\vdots&space;\\&space;y_{n}&space;\end{pmatrix}" title="\large y=\begin{pmatrix} y_{1} \\ \vdots \\ y_{i} \\ \vdots \\ y_{n} \end{pmatrix}" />

<img src="https://latex.codecogs.com/png.latex?\large&space;x&plus;y=\begin{pmatrix}&space;x_{1}&plus;y_{1}&space;\\&space;\vdots&space;\\&space;x_{i}&plus;y_{i}&space;\\&space;\vdots&space;\\&space;x_{n}&plus;y_{n}&space;\end{pmatrix}" title="\large x+y=\begin{pmatrix} x_{1}+y_{1} \\ \vdots \\ x_{i}+y_{i} \\ \vdots \\ x_{n}+y_{n} \end{pmatrix}" />


## Producto por escalar
<img src="https://latex.codecogs.com/png.latex?\large&space;a\begin{pmatrix}&space;x_{1}&space;\\&space;\vdots&space;\\&space;x_{i}&space;\\&space;\vdots&space;\\&space;x_{n}&space;\end{pmatrix}&space;=&space;\begin{pmatrix}&space;\alpha&space;x_{1}&space;\\&space;\vdots&space;\\&space;\alpha&space;x_{i}&space;\\&space;\vdots&space;\\&space;\alpha&space;x_{n}&space;\end{pmatrix}" title="\large a\begin{pmatrix} x_{1} \\ \vdots \\ x_{i} \\ \vdots \\ x_{n} \end{pmatrix} = \begin{pmatrix} \alpha x_{1} \\ \vdots \\ \alpha x_{i} \\ \vdots \\ \alpha x_{n} \end{pmatrix}" />


axpy es la operación de z=ax+y, el libro principal utiliza como notación que a, b, c son escalares y x, y, z son vectores.

### Combinación lineal
Si se puede tomar todos los vectores y hacer una combinación lineal (multiplicarlos todos por un escalar) si eso se cumple se dice que el conjunto es linealmente depeendiente. En otras palabras es que hay por lo menso un valor con el cual puede construir todos los demas elementos que hay en el conjunto


## Dependencia e independencia lineal



## Dimensión del espacio vectorial
Número maximo de vectores que sea linealmente independiente

# Definiciones

## Basis Sets
Cada vector del espacio V, puede expresarse como una combinación lineal de un conjunto G donde G es generado como un set span de v (o G es un conjunto generado por el conjunto V), y ademas todas las combionaciones de los elementos de G estan en V.

Es decir en el caso de los colores, los colores R, G y B son colore sprimarios y no se pueden generar entre si, pero los colores que son generados por los primerarios, es decir lso secundarios, pueden formar otros colores secundarios.

## Inner Products - Producto interno
Es el producto punto entre los vectores
<img src="https://latex.codecogs.com/png.latex?\large&space;\left&space;\langle&space;x,y&space;\right&space;\rangle=\sum_{i}^{n}=x_{i}y_{i}" title="\large \left \langle x,y \right \rangle=\sum_{i}^{n}=x_{i}y_{i}" />


### propiedades
![Image](/images/inner&#32;product&#32;properties.png)

## norma del vector
Es la "distnacia euclideana" de los vectores
![Image](/images/norm&#32;vector&#32;properties.png)







# Lp Norms
Las lp norms me establece las diferentes medidas de las distancias dependiendo del caso, por ejemplo
![Image](/images/lp&#32;norms&#32;vector.png)




# Definiciones

**cerradura:** Es la propiedad de que al relaizar una operación resulte un vector y que
 sus valores internos esten en el conjunto de rango de numeros sea valido