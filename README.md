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








