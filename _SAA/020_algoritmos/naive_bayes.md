Algoritmos Naive Bayes
Los modelos de Naive Bayes son un tipo de algoritmos de aprendizaje automático basados, como su nombre indica, en el teorema de Bayes. En ellos, se asume que las variables de entrada son independientes entre sí. Esto es simplificar mucho, pero de ahí viene el nombre "naive" o inocente. 

Sus principales ventajas son:

Es una manera fácil y rápida de predecir clases, para problemas de clasificación binarios y multiclase.
En los casos en que sea apropiada una presunción de independencia, el algoritmo se comporta mejor que otros modelos de clasificación, incluso con menos datos de entrenamiento.
El desacoplamiento de las distribuciones de características condicionales de clase significan que cada distribución puede ser estimada independientemente como si tuviera una sola dimensión. Esto ayuda con problemas derivados de la dimensionalidad y mejora el rendimiento.
Y sus desventajas son:

Aunque son unos clasificadores bastante buenos, los algoritmos Naive Bayes son conocidos por ser pobres estimadores. Por ello, no se deben tomar muy en serio las probabilidades que se obtienen.
La presunción de independencia Naive muy probablemente no reflejará cómo son los datos en el mundo real.
Cuando el conjunto de datos de prueba tiene una característica que no ha sido observada en el conjunto de entrenamiento, el modelo le asignará una probabilidad de cero y será inútil realizar predicciones. 