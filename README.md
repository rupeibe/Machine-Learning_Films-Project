**OBJETIVO**

Mi trabajo de Machine Learning se centra en tratar de predecir la nota que puede tener una película basándome en el "rating" de los usuarios de Filmaffinity.

**HIPÓTESIS QUE SE PLANTEAN**

Quiero obtener datos relacionados con las películas y poder enriquecerlos de tal forma que sirvan para entrenar un algoritmo de Machine Learning y tratar de predecir la nota que se le asignaría en la web Filmaffinity y así determinar qué nota tiene cada película.

**EXPLORACIÓN DE LAS FUENTES DE DATOS**

Comienzo por un sondeo de webs dedicadas al análisis sobre películas y ver dónde puedo obtener información referente a fichas de las películas, lo más completo posible.

Algunas de las webs donde reviso dicha información son: 
- [IMDb](https://www.imdb.com/)
- [Rotten Tomatoes](https://www.rottentomatoes.com/)
- [Filmaffinity](https://www.filmaffinity.com/es/main.html)

Finalmente me decanto por la web de Filmaffinity ya que tiene una sección en la que se puede obtener información sobre los premios de diferentes festivales de cine y academias cinematográficas de diferentes países, además de obtener gran cantidad de información de las películas (ficha técnica, ficha artística, datos propios de la película como año, duración, país, géneros entre otros).

- [Filmaffinity - Premios](https://www.filmaffinity.com/es/all_awards.php)

La propia web me permite realizar una serie de filtros para desestimar algunos de los registros que pretendo analizar, como películas de animación, documentales y de una duración determinada.

**EXTRACCIÓN DE LOS DATOS**

### FICHAS DE PELÍCULAS

Comienzo cargando todo el listado de todas las películas que están en la web, ayudado de las librerías de Python, Selenium y Beautiful Soup. De esta forma, obtengo los más de 15.000 enlaces a cada una de las películas y posteriormente almaceno la información de la ficha de cada película.

- [Filmaffinity - Top películas](https://www.filmaffinity.com/es/topgen.php)

### PREMIOS DE PELÍCULAS EN FESTIVALES

Primeramente, obtengo los enlaces de cada uno de los más de 45 festivales de cine para después acceder a todas las categorías de premios de cada uno de los festivales y almaceno el histórico de ganadores de cada una de las categorías de premios de cada uno de los festivales.

- [Filmaffinity - Top festivales](https://www.filmaffinity.com/es/topgen.php)

**TRATAMIENTO/ PREPROCESAMIENTO DE LOS DATOS**

Tras el tratamiento y posterior preprocesamiento de los datos, paso de tener 14 columnas de dos dataframes (mayormente categóricas) a tener 33 columnas en un único dataframe (exclusivamente numéricas).

### FICHAS DE PELÍCULAS

Obtengo 10 columnas con toda la información de la película. La mayoría de las columnas son categóricas y necesitarán un preprocesamiento para transformarlas en numéricas y así permitir que el modelo de Machine Learning pueda buscar patrones para poder

 predecir la nota. En cuanto al preprocesamiento de los datos, algunas de las estrategias que he empleado son las siguientes:

- Generar una columna por cada género de las películas, con un total de 15 géneros. En cada columna se establece un 1 (pertenece a ese género) o un 0 (no pertenece a ese género).
- Discretizar las columnas país (por frecuencia), duración y año (por agrupación).

### PREMIOS DE PELÍCULAS EN FESTIVALES

Obtengo un dataframe con más de 3500 registros que comprenden todos los premios que se han otorgado en todos los festivales durante su historia y todas sus categorías de premios. Esta información la utilizaré para obtener nuevas columnas y así enriquecer el dataframe original. Algunas de las nuevas columnas son:

- Premios totales que ha obtenido una película.
- Premios totales en los Razzie Awards (premios que dan un reconocimiento a las películas con categorías que evalúan las peores películas, interpretaciones, etc.).
- Premios que ha logrado el equipo artístico (5 actores principales de cada película) o premios técnicos (dirección, guión, música o fotografía). Esta información me servirá para sustituir el nombre del equipo artístico y técnico de cada película por el número de premios que haya obtenido (cero si no ha obtenido ninguno).

**SELECCIÓN DE ALGORITMOS**

Establezco 4 grupos de modelos (regresión, regularización, basados en árboles y otros tipos) según la naturaleza del propio algoritmo y observo la eficacia de cada uno para poder tener una primera visión de cuáles son los que están funcionando mejor en cuanto a las predicciones.

**EVALUACIÓN DE MODELOS**

Para la evaluación de los diferentes modelos utilizaré las siguientes métricas:

- R2 score: Para establecer de los 16 modelos que se prueban en un principio cuáles de ellos están dando una mayor precisión en sus predicciones.
- MAE: En una segunda fase de optimización de modelos y hasta el final del trabajo, tendré en cuenta la métrica MAE, ya que me indica la medida del error absoluto en las predicciones, que es lo que más me interesa, que las predicciones sean lo más precisas posibles.
- RMSE: En la fase final del trabajo y ya sabiendo dónde se están produciendo las mayores desviaciones de las predicciones con respecto a los datos de prueba, estaré observando qué configuración de los modelos está mejorando los resultados.

**OPTIMIZACIÓN DE MODELOS**

Una vez tengo claro qué modelo en concreto me está dando mejores resultados, me planteo la optimización del mismo. Establezco varias estrategias para ello, algunas de ellas son:

- Voting: De entre los 4 grupos de modelos, elijo el que mejor métrica R2 me proporciona y genero un voting.
- Bagging: Establezco como estimador el modelo que mejor "performance" me ofrece para aplicar la técnica del "bootstrap aggregating".
- Gridsearch: Con el propio modelo seleccionado, busco los mejores hiperparámetros del mismo mediante la técnica de Gridsearch.
- Ponderación de modelos: Busco la ponderación de los modelos que presentan

 mejores resultados en sus predicciones.
- Feature Selection: Me fijo en la importancia que el modelo asigna a las columnas y pruebo a eliminar las de menor importancia utilizando tres métodos diferentes (Importancia de características, Select KBest y Eliminación recursiva de características).

### CONCLUSIONES

Destaco la importancia del "Feature Engineering", ya que la verdadera ganancia en cuanto a la eficacia de un modelo predictivo de Machine Learning está en el tratamiento y preprocesamiento de los datos. Posteriormente, considero importante presentar varios modelos en una primera fase y comparar sus resultados para saber cuáles de ellos son los más efectivos. A partir de este punto, si se realiza una optimización, se puede obtener una mejora, aunque en menor medida.

De las técnicas de optimización utilizadas, destaco la ponderación de modelos y el Bagging como las más efectivas. En cuanto a la "Feature Selection", no se encontró una mejora significativa en este caso, aunque es interesante explorar estas técnicas.
