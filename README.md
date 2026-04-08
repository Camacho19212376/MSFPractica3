[![Open in MATLAB Online](https://www.mathworks.com/images/responsive/global/open-in-matlab-online.svg)](https://matlab.mathworks.com/open/github/v1?repo=Camacho19212376/MSFPractica3)

# Práctica: Sistema musculoesqueletico

## Información de la estudiante

Tchandra Yahoel Camacho Llanes \[19212376]; L19212376@tijuana.tecnm.mx

Modelado de Sistemas Fisiológicos

Ingeniería Biomédica

## Docente

Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx

Departamento de Ingeniería Eléctrica y Electrónica, Tecnológico Nacional de México/IT Tijuana, Blvd. Alberto Limón Padilla s/n, Tijuana, C.P. 22454, B.C., México.

## Descripción de la asignatura

El modelizado de sistemas fisiológicos es una herramienta importante en Ingeniería Biomédica, permite comprender el funcionamiento del cuerpo humano, así como diseñar y evaluar terapias y dispositivos médicos; se define como el proceso de formular modelos matemáticos o computacionales que representan el comportamiento y la interacción de los sistemas biológicos y fisiológicos. Esta asignatura pretende aportar al perfil del Ingeniero Biomédico la capacidad de realizar investigación científica en el área de Biología de Sistemas con la finalidad de dirigir y participar en equipos de trabajo interdisciplinarios en contextos nacionales e internacionales, así como de proporcionar soluciones informáticas para resolver problemas en el campo de la Ingeniería Biomédica con ética profesional; lo anterior al proporcionar al estudiante bases sólidas para modelizar sistemas y diseñar controladores para la solución de problemas en las áreas de atención médica y del sector industrial médico. La construcción de analogías entre circuitos eléctricos y sistemas fisiológicos para la formulación de modelos matemáticos y el diseño de controladores mediante la experimentación in silico brindan herramientas de gran aplicación en el quehacer profesional del Ingeniero Biomédico.

La asignatura de Modelado de Sistemas Fisiológicos forma parte del plan de estudios de la carrera en Ingeniería Biomédica con la siguiente competencia general del curso: Utiliza las propiedades de los circuitos RLC para describir la dinámica de sistemas fisiológicos, obtener modelos matemáticos y aplicar el control clásico, esto con el objetivo de integrar los principios de la Ingeniería de Control, la Electrónica Analógica y las Ciencias de la Computación con la Anatomía y Fisiología del cuerpo humano para proporcionar descripciones cuantitativas y cualitativas de sistemas fisiológicos complejos con el objetivo de modelizar, analizar, controlar, ilustrar y predecir su dinámica tanto en el corto como en el largo plazo.

## Objetivos

1. Convertir el diagrama mecánico al diagrama eléctrico.

2. Calcular la función de transferencia aplicando el principio de superposición.

3. Calcular el error en estado estacionario y la estabilidad en lazo abierto.

4. Emular y simular la respuesta del circuito en Simulink/Simscape a la señal impulso unitario.

5. Sintonizar las ganancias de un controlador PID para eliminar el error entre la entrada y la salida del sistema control-caso.

6. Obtener la respuesta en lazo abierto y en lazo cerrado con el controlador PID en Spyder/Python con la función de transferencia.

## Descripción detallada del sistema

El símbolo F se utiliza para describir la fuerza generada por el componente activo contráctil del músculo, mientras que F(t) corresponde a la fuerza efectiva que se obtiene al considerar las características mecánicas del tejido muscular. Se establece que ambas están relacionadas mediante la expresión F = αF(t), donde 0 < α < 1. Por otra parte, R representa la resistencia viscosa propia del tejido, en tanto que Cp (elemento elástico en paralelo) y Cs (elemento elástico en serie) modelan la capacidad de almacenamiento de energía elástica del sarcolema y de los tendones, respectivamente.

La disposición en paralelo se plantea con el fin de incluir las limitaciones mecánicas que afectan a los elementos del modelo. Cuando el resorte Cp experimenta un alargamiento de magnitud Fs(t), el conjunto en serie formado por R y Cs también se deforma en la misma proporción. Asimismo, la suma de las fuerzas que circulan por ambas ramas del arreglo en paralelo debe ser equivalente a F(t). Aunque la elongación total de Cs y R debe coincidir con Fs(t), cada uno de estos elementos no necesariamente contribuye en igual medida. Así, si se supone que Cs se extiende una cantidad Fs₁(t), entonces la deformación correspondiente en la rama paralela que incluye R será Fs(t) − Fs₁(t). La rapidez de deformación del amortiguador asociado a R se determina derivando la expresión Fs(t) − Fs₁(t) con respecto al tiempo, es decir, d[Fs(t) − Fs₁(t)]/dt.

Palabras clave: músculo, fuerza, resistencia, modelo, amortiguación.

## Lista de archivos incluidos en el repositorio

1. Cuaderno computacional de MATLAB [.mlx].
2. Modelo de Simulink [.slx].
3. Archivos de Spyder [.py].
4. Imagen con los parámetros del controlador.
5. Imágenes de las simulaciones [.pdf y .png].
6. Evidencia del análisis matemático: función de transferencia, modelo de ecuaciones integro-diferenciales, error en estado estacionario y estabilidad en lazo abierto.
7. Modelo fisiológico en Biorender o BioArt.

## Referencias

\[1] P. A. Valle, Syllabus para Modelado de Sistemas Fisiológicos, Tecnológico Nacional de México / Instituto Tecnológico de Tijuana, Tijuana, B.C., México, 2025. Permalink: https://biomath.xyz/course/

\[2] M. C. Khoo, Physiological Control Systems Analysis Simulation, and Estimation, 2nd ed. Piscataway, New Jersey, USA: IEEE Press, 2018, Section 4, Page 93.

\[3] N. S. Nise, Control Systems Engineering, 8th ed. Hoboken, New Jersey, USA: John Wiley \& Sons, 2020.

\[4] T. Kind, T. J. Faes, J. W. Lankhaar, A. Vonk-Noordegraaf \& M. Verhaegen, "Estimation of three-and four-element Windkessel parameters using subspace model identification", IEEE Transactions on Biomedical Engineering, vol. 57, issue 7, pp. 1531-1538, Jul 2010. https://doi.org/10.1109/TBME.2010.2041351


