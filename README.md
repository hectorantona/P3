PAV - P3: detección de pitch
============================

Esta práctica se distribuye a través del repositorio GitHub [Práctica 3](https://github.com/albino-pav/P3).
Siga las instrucciones de la [Práctica 2](https://github.com/albino-pav/P2) para realizar un `fork` de la
misma y distribuir copias locales (*clones*) del mismo a los distintos integrantes del grupo de prácticas.

Recuerde realizar el *pull request* al repositorio original una vez completada la práctica.

Ejercicios básicos
------------------

- Complete el código de los ficheros necesarios para realizar la detección de pitch usando el programa
  `get_pitch`.

   * Complete el cálculo de la autocorrelación e inserte a continuación el código correspondiente. 

    void PitchAnalyzer::autocorrelation(const vector<float> &x, vector<float> &r) const {
      int N = x.size();
      for (unsigned int l = 0; l < r.size(); ++l) {
        r[l] = 0.0;
        for (int i = 0; i < N - l; i++) 
          r[l] += x[i]*x[i+l];
        r[l] /= N;
      }

      if (r[0] == 0.0F) //to avoid log() and divide zero 
        r[0] = 1e-10; 
    }

   * Inserte una gŕafica donde, en un *subplot*, se vea con claridad la señal temporal de un segmento de
     unos 30 ms de un fonema sonoro y su periodo de pitch; y, en otro *subplot*, se vea con claridad la
	 autocorrelación de la señal y la posición del primer máximo secundario.

  <img src="images/Grafica1.png" width="720" align="center">

  El código para la generación de la gráfica se encuentra en el fichero plot1.py.

	 NOTA: es más que probable que tenga que usar Python, Octave/MATLAB u otro programa semejante para
	 hacerlo. Se valorará la utilización de la librería matplotlib de Python.

   * Determine el mejor candidato para el periodo de pitch localizando el primer máximo secundario de la
     autocorrelación. Inserte a continuación el código correspondiente.

    ```cpp
    vector<float>::const_iterator iR = r.begin(), iRMax = iR;
    vector<float>::const_iterator iRpre = r.begin();
    vector<float>::const_iterator iRpost = r.begin() + 1;

    while (*iR > *iRpost || iR < r.begin() + npitch_min || *iR > 0.0F) {
      iR++;
      iRpost++;
    }

    iRMax = iR;

    while (iR < r.begin() + npitch_max) {
      if (*iR > *iRMax) {
        iRpre = iR - 1;
        iRpost = iR + 1;
        if (*iR > *iRpre && *iR > *iRpost)
          iRMax = iR;
      }
      ++iR;
    }

    unsigned int lag = iRMax - r.begin();
    ```

   * Implemente la regla de decisión sonoro o sordo e inserte el código correspondiente.

  ```cpp
   bool PitchAnalyzer::unvoiced(float pot, float r1norm, float rmaxnorm) const {
    if (pot < -50 || r1norm < 0.7 || rmaxnorm < 0.3 || (r1norm < 0.93 && rmaxnorm < 0.4))
      return true; //Unvoiced Sound
    else
      return false; //Voiced Sound
  }
  ´´´

- Una vez completados los puntos anteriores, dispondrá de una primera versión del detector de pitch. El 
  resto del trabajo consiste, básicamente, en obtener las mejores prestaciones posibles con él.

  * Utilice el programa `wavesurfer` para analizar las condiciones apropiadas para determinar si un
    segmento es sonoro o sordo. 
	
	  - Inserte una gráfica con la detección de pitch incorporada a `wavesurfer` y, junto a ella, los 
	    principales candidatos para determinar la sonoridad de la voz: el nivel de potencia de la señal
		(r[0]), la autocorrelación normalizada de uno (r1norm = r[1] / r[0]) y el valor de la
		autocorrelación en su máximo secundario (rmaxnorm = r[lag] / r[0]).

		Puede considerar, también, la conveniencia de usar la tasa de cruces por cero.

	    Recuerde configurar los paneles de datos para que el desplazamiento de ventana sea el adecuado, que
		en esta práctica es de 15 ms.

    <img src="images/Grafica2.png" width="720" align="center">

    El código para la generación de la gráfica se encuentra en el fichero plot2.py.


      - Use el detector de pitch implementado en el programa `wavesurfer` en una señal de prueba y compare
	    su resultado con el obtenido por la mejor versión de su propio sistema.  Inserte una gráfica
		ilustrativa del resultado de ambos detectores.

    <img src="images/Grafica3.png" width="720" align="center">

    El código para la generación de la gráfica se encuentra en el fichero plot3.py y tomando como ejemplo la señal sb014.wav


  * Optimice los parámetros de su sistema de detección de pitch e inserte una tabla con las tasas de error
    y el *score* TOTAL proporcionados por `pitch_evaluate` en la evaluación de la base de datos 
	`pitch_db/train`..

  <img src="images/Results.png" width="480" align="center">

   * Inserte una gráfica en la que se vea con claridad el resultado de su detector de pitch junto al del
     detector de Wavesurfer. Aunque puede usarse Wavesurfer para obtener la representación, se valorará
	 el uso de alternativas de mayor calidad (particularmente Python).
   
    <img src="images/Grafica4.png" width="720" align="center">

    Habiendo tomado por ejemplo sb018.wav


Ejercicios de ampliación
------------------------

- Usando la librería `docopt_cpp`, modifique el fichero `get_pitch.cpp` para incorporar los parámetros del
  detector a los argumentos de la línea de comandos.
  
  Esta técnica le resultará especialmente útil para optimizar los parámetros del detector. Recuerde que
  una parte importante de la evaluación recaerá en el resultado obtenido en la detección de pitch en la
  base de datos.

  * Inserte un *pantallazo* en el que se vea el mensaje de ayuda del programa y un ejemplo de utilización
    con los argumentos añadidos.

  <img src="images/Usage.png" width="720" align="center">

  Aquí se inserta el mensaje de ayuda del programa y a continuación se muestra un ejemplo de uso:

  scripts/run_get_pitch.sh 50.5 0.7 0.3

  Donde el 50.5 es el threshold de potencia, el cual debe introducirse en positivo, seguido de los thresholds de r1norm y rmaxnorm. Puede verse en el script run_get_pitch.sh la implementación para que acepte parámetros.

- Implemente las técnicas que considere oportunas para optimizar las prestaciones del sistema de detección
  de pitch.

  Entre las posibles mejoras, puede escoger una o más de las siguientes:

  * Técnicas de preprocesado: filtrado paso bajo, *center clipping*, etc.
  * Técnicas de postprocesado: filtro de mediana, *dynamic time warping*, etc.
  * Métodos alternativos a la autocorrelación: procesado cepstral, *average magnitude difference function*
    (AMDF), etc.
  * Optimización **demostrable** de los parámetros que gobiernan el detector, en concreto, de los que
    gobiernan la decisión sonoro/sordo.
  * Cualquier otra técnica que se le pueda ocurrir o encuentre en la literatura.

  Encontrará más información acerca de estas técnicas en las [Transparencias del Curso](https://atenea.upc.edu/pluginfile.php/2908770/mod_resource/content/3/2b_PS%20Techniques.pdf)
  y en [Spoken Language Processing](https://discovery.upc.edu/iii/encore/record/C__Rb1233593?lang=cat).
  También encontrará más información en los anexos del enunciado de esta práctica.

  Incluya, a continuación, una explicación de las técnicas incorporadas al detector. Se valorará la
  inclusión de gráficas, tablas, código o cualquier otra cosa que ayude a comprender el trabajo realizado.

  Center-clipping:

  ```cpp
  float cl_threshold = 0.0;
  float pow = 0.0;

  for (unsigned int i = 0; i < x.size(); i++) 
    pow += x[i] * x[i];
  pow /= x.size();

  cl_threshold = 0.8 * pow;

  for (unsigned int i = 0; i < x.size(); i++)
    if (x[i] >= cl_threshold)
      x[i] -= cl_threshold;
    else if (abs(x[i]) < cl_threshold)
      x[i] = 0;
    else 
      x[i] += cl_threshold;
  ```
  Ejemplo de uso del center clipping para un tramo sonoro.

  <img src="images/Clipping.png" width="720" align="center">

  Median filter

  ```cpp
  vector<float>window(3);

  for (unsigned int i = 1; i < f0.size() - 1; ++i) { 
    for (unsigned int p = 0; p < 3; ++p)
      window[p] = f0[i - 1 + p];
    sort(window.begin(), window.end());
    f0[i] = window[1];
  }
  ```


  También se valorará la realización de un estudio de los parámetros involucrados. Por ejemplo, si se opta por implementar el filtro de mediana, se valorará el análisis de los resultados obtenidos en función de la longitud del filtro.
   

Evaluación *ciega* del detector
-------------------------------

Antes de realizar el *pull request* debe asegurarse de que su repositorio contiene los ficheros necesarios
para compilar los programas correctamente ejecutando `make release`.

Con los ejecutables construidos de esta manera, los profesores de la asignatura procederán a evaluar el
detector con la parte de test de la base de datos (desconocida para los alumnos). Una parte importante de
la nota de la práctica recaerá en el resultado de esta evaluación.
