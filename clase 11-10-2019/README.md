# Matematicas 2
Capitulo 2 del libro matrix algebra.
# Machine learning
Por medio del algebra lineal se tratan diferentes problemas de la computación, entre esos está el *machine learning* este se basa en utilizar un conjunto de datos de entreanmiento para pasarlo a un algoritmo de aprendizaje el cual extrae una serie de predictores y clasificadores los cuales permita a razón de estos para que el algoritmo sea capaz de dar respuesta a razón del "analisis" de estos datos.

## Datos de entrenamiento
Los datos de entrenamiento son los que la maquina se basa o utiliza para influenciar en los procesos de decisión o entrega de de resultados, los datos suelen provenir del ambiente, un dato es una representación de algo cuantificable o algo representativo, estos requeiren de un *tratamiento* para que una maquina pueda interpretarlo y procesarlo correctamente, los datos genrralmente son acumulados y agrupados en varios elementos los cuales para la matematica y la computación se almacena en un **vector caracteristico**.

## La "información"
En la actualidad hay muchas fuentes de información de los cuales pueden realizarse varios procesos de analisis, dependiendo de la necesidad particular será la forma en qeu han de procesarse los datos. Una de las fuentes más convencionales es **codingthematrix**

---

# Espacios métricos y espacios vectoriales


## Similitud
Hace referencia a lo similar, lo parecido que son dos eleemntos entre si

## Medidas de similitud
Dado una función
S:HxH --> R  
Un conjunto de parejas ordenadas que retornan un número real que cumpla  
i) Exista algún número S0 de tla manera que el parecido entre dos elementos nunca supere el valor de s_0




## Distancia
Es la medición de que tan lejos están dos objetos entre si

# Similitud

1. <img src="https://latex.codecogs.com/png.latex?\large&space;\exists&space;s_{0}&space;\&space;s(x,y)\leq&space;s_{0}&space;\&space;\forall&space;x,y\epsilon&space;H" title="\large \exists s_{0} \ s(x,y)\leq s_{0} \ \forall x,y\epsilon H" />
2. <img src="https://latex.codecogs.com/png.latex?\large&space;s(x,x)=s_{0}" title="\large s(x,x)=s_{0}" />
3. <img src="https://latex.codecogs.com/png.latex?\large&space;s(x,y)=s(y,x)" title="\large s(x,y)=s(y,x)" /> (simetría)

### Ejemplo
R^n Espacio Euclidiano de dimensión **n**.  
<img src="https://latex.codecogs.com/png.latex?\large&space;\mathbb{R}^{n}" title="\large \mathbb{R}^{n}" />. Espacio Euclidiano de dimensión n

<img src="https://latex.codecogs.com/png.latex?\large&space;\mathbb{R}^{n}=&space;\begin{Bmatrix}&space;\begin{pmatrix}&space;x_{1}&space;\\&space;x_{2}&space;\\&space;\vdots&space;\\&space;x_{i}&space;\\&space;\vdots&space;\\&space;x_{n}&space;\\&space;\end{pmatrix}&space;&&space;:&space;&&space;x_{i}\epsilon&space;\mathbb{R}&space;\end{Bmatrix}" title="\large \mathbb{R}^{n}= \begin{Bmatrix} \begin{pmatrix} x_{1} \\ x_{2} \\ \vdots \\ x_{i} \\ \vdots \\ x_{n} \\ \end{pmatrix} & : & x_{i}\epsilon \mathbb{R} \end{Bmatrix}" />


producto interno  
<img src="https://latex.codecogs.com/png.latex?\large&space;x=\begin{pmatrix}&space;x_{1}&space;\\&space;\vdots&space;\\&space;x_{i}&space;\\&space;\vdots&space;\\&space;x_{n}&space;\\&space;\end{pmatrix}" title="\large x=\begin{pmatrix} x_{1} \\ \vdots \\ x_{i} \\ \vdots \\ x_{n} \\ \end{pmatrix}" />
<img src="https://latex.codecogs.com/png.latex?\large&space;y=\begin{pmatrix}&space;y_{1}&space;\\&space;\vdots&space;\\&space;y_{i}&space;\\&space;\vdots&space;\\&space;y_{n}&space;\\&space;\end{pmatrix}" title="\large y=\begin{pmatrix} y_{1} \\ \vdots \\ y_{i} \\ \vdots \\ y_{n} \\ \end{pmatrix}" />

<img src="https://latex.codecogs.com/png.latex?\large&space;x\cdot&space;y=x_{1}*y_{1}&plus;\cdots&space;&plus;x_{n}*y_{1}=\sum_{i=1}^{n}x_{i}y_{i}" title="\large x\cdot y=x_{1}*y_{1}+\cdots +x_{n}*y_{1}=\sum_{i=1}^{n}x_{i}y_{i}" />

Un caso es medir el la similitud o bien el angulo (eel angulo indica que tan diferente son) que hay entre dos vectores, la formula es.

<img src="https://latex.codecogs.com/png.latex?\large&space;cos\Theta&space;=\frac{x\cdot&space;y}{\left&space;\|&space;x&space;\right&space;\|\left&space;\|&space;y&space;\right&space;\|}" title="\large cos\Theta =\frac{x\cdot y}{\left \| x \right \|\left \| y \right \|}" /> 
-
<img src="https://latex.codecogs.com/png.latex?\large&space;\left&space;\|&space;x&space;\right&space;\|=\sqrt{x_{2}^{1}&plus;\cdots&space;&plus;x_{n}^{2}}=\left&space;(&space;\sum_{i=1}^{n}x_{i}^{2}\right&space;)^{\frac{1}{2}}" title="\large \left \| x \right \|=\sqrt{x_{2}^{1}+\cdots +x_{n}^{2}}=\left ( \sum_{i=1}^{n}x_{i}^{2}\right )^{\frac{1}{2}}" />

### Ejemplo sistemas de recomendación
Se puede medir la similitud que tiene un cliente con otro por medio de la técnica del coseno, por ejemplo un sistema vende varios productos y le pide a sus clientes una calificación de cada uno de estos, entonces para determinar si un client tiene gustos similares utiliza la formula del coseno anterior de la siguiente manera.

|Usuario/producto|P_1|P_2|P_3|P_4|P_5|...|Pm
|-|-|-|-|-|-|-|-|
|C_1|3|5|-|2|3|-|2|
|C_2|4|5|4|-|4|-|3|
|...|
|Cn|

De esta tabla de datos para determinar que similitud tiene estos dos clientes se aplica lo siguiente:  
C_1: (3,5,3,2)  
C_2:(4,5,4,3)

cos(C_1, C_2) >= *u*

Si *u* es mayor que 0.7 tienen gustos muy similares, si tienen gustos muy diferentes va a ser cercano a 0

# Algoritmos supervisado de clasificación
Los algoritmos de clasificación colocan los datos en diferentes grupos de acuerdo a una serie de caracteristicas o formas en clasificar, asi como en el caso de clustering es acomodar lo similares que son


## Algoirmo K-NN
El problema trata de que determinar sus vecinos K proximos y clasificar los grupos.
Se tiene un conjunto de datos clasificados
Para un nuevo dato **x**:
* encontrar los 5 vectors en el conjunto de datos con mayor **similutd** con **x**
* Cada vecino da un voto por su clase
* **x** se clasificaca en el grupo con mayor número de votos


# Problema de los datos
Los datos muchas veces no son percetibles o captables