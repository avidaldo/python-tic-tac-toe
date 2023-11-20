# GPGPU

## Historia

El uso de Unidades de Procesamiento Gráfico (GPU) para la computación de propósito general, un concepto conocido como computación de propósito general en GPU (GPGPU), tiene una historia que se puede resumir de la siguiente manera:

### Primeros Días (década de 2000) 

A principios de la década de 2000, investigadores y desarrolladores comenzaron a explorar el uso de las GPUs para cálculos no relacionados con gráficos.
Las GPUs inicialmente se diseñaron para renderizar gráficos, pero se descubrió que tenían una capacidad de procesamiento en paralelo que se podía aprovechar para una amplia gama de aplicaciones científicas e ingenieriles.

### CUDA y Stream Computing (mediados de la década de 2000)

NVIDIA introdujo CUDA (Compute Unified Device Architecture) en 2006, lo que permitió a los desarrolladores escribir programas de propósito general que podían ejecutarse en las GPUs de NVIDIA.
AMD introdujo un concepto similar conocido como Stream Computing.
Estos marcos de programación proporcionaron las herramientas y API necesarias para la computación GPGPU, lo que permitió a los desarrolladores aprovechar las capacidades de cálculo de la GPU.

### Auge del Paralelismo (finales de la década de 2000 - principios de la década de 2010)

La computación GPGPU ganó popularidad en círculos científicos y académicos para tareas como simulaciones científicas, procesamiento de datos y aprendizaje automático.
Las GPUs se utilizaron para acelerar tareas que podían ser paralelizadas, aprovechando los cientos de núcleos disponibles en las GPUs modernas.

### Auge del *Deep Learning* (mediados de la década de 2010)

La aparición del aprendizaje profundo y las redes neuronales condujo a un impulso significativo en el uso de las GPUs.
Se comprobó que las GPUs eran altamente eficaces para entrenar redes neuronales profundas debido a su capacidad para realizar operaciones de algebra lineal en paralelo.

### Adopción en la Industria (década de 2010):

Muchas industrias, como la financiera, la atención médica y la automotriz, comenzaron a aprovechar la computación GPGPU para tareas como modelado financiero, imágenes médicas y conducción autónoma.

### Aceleradores Especializados (década de 2020)

Con la creciente necesidad de hardware especializado para la inteligencia artificial y el aprendizaje automático, aceleradores personalizados como las **Unidades de Procesamiento Tensorial (TPU)** y aceleradores de IA se volvieron prominentes.
Sin embargo, las GPUs siguen siendo ampliamente utilizadas para muchos tipos de tareas de cómputo en paralelo y continúan evolucionando con características y rendimiento mejorados.

## CUDA

CUDA es una plataforma de computación paralela y un modelo de programación creado por NVIDIA. Permite a los programadores utilizar un lenguaje de programación similar a C para crear algoritmos que utilizan la GPU para realizar cálculos intensivos de forma más eficiente que en una CPU.
