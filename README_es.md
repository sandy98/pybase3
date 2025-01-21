<p align="center">
  <img src="https://raw.githubusercontent.com/sandy98/pybase3/main/img/pybase3t.png" alt="pybase3 logo">
</p>

<!--![PyPI - Current Version](https://img.shields.io/pypi/v/pybase3)-->

<p>
  <a href="https://pypi.org/project/pybase3">
    <img src="https://img.shields.io/pypi/v/pybase3" alt="PyPI - Current Version">
  </a>
  <img src="https://img.shields.io/pypi/dm/pybase3">
</p>

# Biblioteca Python para DBase III

Biblioteca de Python diseñada para manipular archivos de bases de datos DBase III. Permite leer, escribir, agregar y actualizar registros en la base de datos.

Aunque este formato de archivo para bases de datos ya no se utiliza en gran medida, el presente trabajo es una herramienta útil para recuperar datos antiguos, así como un homenaje a una hermosa parte de la historia de la informática.

A partir de las versiones actualizadas el 4 de enero de 2025, `pybase3` admite la indexación a través de archivos `.pmdx` (Python + .mdx), lo que da como resultado consultas sorprendentemente rápidas. Consulte a continuación para obtener más detalles.

## Características

- Leer archivos de bases de datos DBase III
- Escribir en archivos de bases de datos DBase III
- Agregar nuevos registros
- Actualizar registros existentes
- Filtrar y buscar registros
- Importación desde/exportación a archivos `.csv`. (Novedad en la versión 1.12.1) Consulte `import_from` y `export_to`
- Importación desde/ exportación a databases `sqlite`. (Novedad en la versión 1.13.1) Consulte `import_from` y `export_to`

## Instalación

Para instalar la biblioteca, clone este repositorio y navegue hasta el directorio del proyecto:

```bash
git clone https://github.com/sandy98/pybase3.git
cd pybase3
```

o

```bash
pip install pybase3
```

## Uso

### Clase principal

```python
from pybase3 import DBaseFile, FieldType
test = DbaseFile.create('db/test.dbf',
                    [('name', FieldType.CHARACTER.value, 50, 0),
                        ('age', FieldType.NUMERIC.value, 3, 0)])
test.add_record('John Doe', 30)
test.add_record('Jane Doe', 25)

print(test)
print(len(test))
print(test[:])
print(test.filter('name', 'ja', compare_function=self.istartswith))

```

### Utilidad de exploración de bases de datos

```bash
python3 dbfview.py <dbf_file>
```

o, mejor aún, si se instala pybase3 usando pip, instalará dbfview como un script, de esta manera:

```bash
dbfview <dbf_file>
```

Una práctica utilidad basada en CLI  curses para explorar archivos .dbf.

### Utilidad de prueba

```bash
python3 dbftest.py [-r|-d]
```

o, mejor aún, si pybase3 se instala usando pip, instalará dbftest como un script, de la siguiente manera:

```bash
dbftest [-r|-d]
```

Este es un script de prueba simple para el módulo pybase3.
Crea una base de datos de prueba (`db/test.dbf`), actualiza algunos registros y elimina uno.
Luego escribe los cambios en el archivo de base de datos.
El script se puede ejecutar con la opción -d para mostrar resultados intermedios o con la opción -r para borrar un test.dbf existente.
El script creará un directorio 'db' en el directorio actual si no existe.
El script creará un archivo 'test.dbf' en el directorio 'db' si no existe.

### Uso a nivel de módulo

Al emitir el comando:

```bash
python3 -m pybase3
```

se invoca el módulo en sí (más específicamente, __main__.py), lo que da como resultado un recorrido por el sistema de archivos en busca de archivos .dbf. Al final, si la búsqueda es exitosa, se le ofrece al usuario un menú numerado de archivos dbf existentes, listos para ser leídos por dbfview.

A partir de la versión 1.9.5 se agregaron nuevas opciones: -v, --version para recuperar la versión actual del software, -i, --info para obtener información completa y -h, --help para obtener instrucciones de uso.

También se agregó una opción de línea de comandos ``pybase3`` en la versión 1.9.5, que funciona de la misma manera que invocar el módulo, por ejemplo:

```bash
pybase3 [-v|-i|-h]
```

### Comentarios

El módulo en sí, la clase DBaseFile y todos sus métodos están completamente documentados, por lo que debería ser fácil seguirlo.

Básicamente, cada instancia de DBaseFile, ya sea instanciada a través de un archivo DBase III existente o creada a través del método de fábrica DBaseFile.create(filename), es un objeto tipo lista con capacidades de indexación, que también actúa como un iterador a través de los registros presentes en el archivo .dbf. También admite el método 'len', que informa la cantidad de registros presentes en la base de datos, incluso aquellos marcados para su eliminación.
Además de eso, hay un grupo de métodos destinados a la manipulación de datos (add_record para inserciones, update_record para actualizaciones y del_record para marcar/desmarcar eliminaciones).
También hay un grupo de métodos (búsqueda, índice, hallazgo, filtro) para ayudar a recuperar datos seleccionados.

En su etapa actual de desarrollo, no hay soporte para campos de memo o campos de índice, aunque esto está planeado para futuras versiones, en caso de que surja suficiente interés.
La versión 1.14.2 incorpora el método `execute` para ejecutar instrucciones SQL, devolviendo un objeto Cursor.

Para obtener más información, consulte la documentación a continuación.

## Documentación

### Clases

#### `DBaseFile`

Clase para manipular archivos de base de datos DBase III.

### Métodos 'Dunder' y 'privados'

- `__init__(self, filename: str)`: Inicializa una instancia de DBase3File desde un archivo dbf existente.
- `__del__(self)`: Cierra el archivo de base de datos cuando se destruye la instancia.
- `__len__(self)`: Devuelve la cantidad de registros en la base de datos, incluidos los registros marcados para eliminarse. Permite escribir: `len(dbasefileobj)`
- `__getitem__(self, key)`: Devuelve un único registro o una lista de registros (si se utiliza la notación de 'slices') de la base de datos. Permite: `dbasefileobj[3]` o `dbasefileobj[3:7]`
- `__iter__(self)`: Devuelve un iterador sobre los registros de la base de datos. Permite: `for record in dbasefileobj: ...`
- `__str__(self)`: Devuelve una representación de cadena de la base de datos.
- `_init(self)`: Inicializa la estructura de la base de datos leyendo el encabezado y los campos. Destinado para uso privado por parte de instancias de DBaseFile.
- `def _test_key(self, key)`: Comprueba si la clave está dentro del rango válido de índices de registros. Genera un error de índice si la clave está fuera del rango. Solo para uso interno.

### Métodos de clase

- `create(cls, filename: str, fields: List[Tuple[str, FieldType, int, int]])`: Crea un nuevo archivo de base de datos DBase III con los campos especificados. Devuelve un objeto DbaseFile que apunta al archivo dbase recién creado.

### Métodos de manipulación de datos

- `add_record(self, record_data: dict)`: Agrega un nuevo registro a la base de datos.
- `update_record(self, index: int, record_data: dict)`: Actualiza un registro existente en la base de datos.
- `save_record(self, key, record)`: Escribe un registro (diccionario con nombres de campos y valores de campos) en la base de datos en el índice especificado. Parámetros: la clave es el índice (posición basada en 0 en el archivo dbf). El registro es un diccionario que corresponde a un elemento en la base de datos. (i.e: {'id': 1, 'name': "Jane Doe"}) Usado internamente por `update_record`
- `del_record(self, key, value = True)`: Marca para su eliminación el registro identificado por el índice 'clave', o lo desmarca si `value == False`. Para borrar efectivamente el registro del disco, la eliminación debe confirmarse utilizando `dbasefileobj.commit()`
- `commit(self, filename=None)`: Anteriormente llamado `write`, escribe el archivo actual en el disco, omitiendo los registros marcados para su eliminación. Si se proporciona un nombre de archivo distinto del actual, se guarda el archivo de base de datos en el nuevo destino y se conserva el nombre de archivo anterior. Vale la pena señalar que `add_record` y `update_record` confirman los cambios en el disco inmediatamente, por lo que no es necesario llamar a `commit` después de usarlos. Igualmente, no genera problemas hacerlo.

### Métodos de búsqueda/filtrado de datos

- `search(self, fieldname, value, start=0, funcname="", compare_function=None)`: Escribe el archivo actual en el disco, omitiendo los registros marcados para su eliminación. Si se proporciona un nombre de archivo distinto del actual, se guarda el archivo de base de datos en el nuevo destino y se conserva el nombre de archivo anterior.
- `find(self, fieldname, value, start=0, compare_function=None)`: Contenedor para search() con funcname="find". Devuelve el primer registro (diccionario) encontrado, o None si no se encuentra ningún registro que cumpla los criterios dados.
- `index(self, fieldname, value, start=0, compare_function=None)`:  Contenedor para search() con funcname="index". Devuelve el índice del primer registro encontrado o -1 si no se encuentra ningún registro que cumpla los criterios dados.
- `filter(self, fieldname, value, compare_function=None)`: Devuelve una lista de registros (diccionarios) que cumplen los criterios especificados.
- `execute(self, sql_cmd:str)`: Diseñado para recuperar datos de forma personalizada, con consultas SQL.

### Métodos de listado de datos

- `list(self, start=0, stop=None, fieldsep="|", recordsep='\n', records:list=None)`: Devuelve una lista de registros de la base de datos, comenzando en 'start', terminando en 'stop' o EOF, con campos separados por 'fieldsep' y registros separados por '\n'. Si 'records' no es None, se utiliza la lista proporcionada en lugar de recuperar valores de la base de datos.
- `csv(self, start=0, stop=None, records:list = None)`: Envoltorio para 'list', usando ',' como fieldsep.
- `table(self, start=0, stop=None, records:list = None)`: Recupera registros seleccionados usando un formato ad-hoc, el mismo que proporciona la CLI de sqlite3 en modo .table.
- `pretty_table(self, start=0, stop=None, records:list = None)`: recupera los registros seleccionados utilizando un formato ad-hoc, como `table` pero con líneas más bonitas.
- `lines(self, start=0, stop=None, records:list = None)`: recupera los registros seleccionados con los valores de campo alineados con sus anchos.

Vale la pena señalar que estos últimos cinco métodos devuelven generadores en lugar de listas, lo que los hace mucho más livianos en el caso de conjuntos de registros voluminosos.

### Métodos estáticos (Funciones auxiliares para búsqueda/filtrado de datos)

- `istartswith(f: str, v: str) -> bool`: Comprueba si la cadena `f` comienza con la cadena `v`, ignorando mayúsculas y minúsculas.
- `iendswith(f: str, v: str) -> bool`: Comprueba si la cadena `f` termina con la cadena `v`, ignorando mayúsculas y minúsculas.

### Propiedades

- 'fields': recupera la lista de campos a partir de los cuales se ensamblan los registros de la base de datos. Cada objeto de campo de la lista tiene un nombre, un tipo (según la enumeración FieldType) y una longitud.
- 'field_names': recupera una lista con el nombre de cada campo de la base de datos.
- 'field_types': recupera una lista con el tipo de cada campo de la base de datos.
- 'field_lengths': recupera una lista con la longitud de cada campo de la base de datos.
- 'max_field_lengths': Devuelve la longitud máxima del campo especificado (incluida la longitud del nombre del campo) en la base de datos. Útil para recuperar líneas con el ancho ajustado para cada campo. Utiliza internamente `def max_field_length(self, field)`
- 'tmax_field_lengths': Igual que max_field_lengths, versión con threads, en un intento fallido de acelerar el proceso. Funciona, de todos modos.

## Contribuciones

¡Se aceptan contribuciones! Abra un issue o envíe una solicitud de incorporación de cambios.

## Licencia

Este proyecto está licenciado bajo la licencia MIT. Consulte el archivo LICENCIA para obtener más detalles.

## Contacto

Para cualquier duda o sugerencia, por favor contacte con nosotros. [Domingo E. Savoretti](mailto:esavoretti@gmail.com).
