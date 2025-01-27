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

A partir de la versión 1.90. ... se agregaron las clases Connection y Cursor, comenzando el camino hacia la conformidad total con la especificación de la API de base de datos de Python v2.0 (PEP 249).
Hasta este punto, tanto Cursor como Connection admiten el método `execute`, que acepta comandos `select, insert, update y delete`. Se está desarrollando un mayor soporte para SQL (`create, etc`).
Estas características funcionan de manera estable a partir de la versión 1.98.3, aunque existen algunas limitaciones de uso, principalmente el hecho de que, en este momento, las consultas están "centradas en la tabla", lo que significa que no funcionan en más de una tabla a la vez. Esto se abordará en futuras versiones, ya que es un requisito para alcanzar la conformidad total.
Con suerte, pybase3 se incluirá en la lista junto con los otros módulos compatibles con la API de base de datos de Python (Sqlite3, MySQL, Postgre, etc.)

Aunque este formato de archivo para bases de datos ya no se utiliza en gran medida, el presente trabajo es una herramienta útil para recuperar datos antiguos, así como un homenaje a una hermosa parte de la historia de la informática.

A partir de las versiones actualizadas el 4 de enero de 2025, `pybase3` admite la indexación a través de archivos `.pmdx` (Python + .mdx), lo que da como resultado consultas sorprendentemente rápidas. Consulte a continuación para obtener más detalles.

## Características

- Clases API DB: Connection y Cursor
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

### Clase `Connection`

```python
import pybase3
from pybase3 import Connection

# Se conecta al directorio 'db'. Se incluirán todos los archivos .dbf que contenga.
conn = Connection('db')
# Obtiene un objeto Cursor de la conexión ejecutando un comando SQL
curr = conn.execute('select id, nombre as name, title from team order by title desc;')
# Pasa el cursor a una función de formato de datos
for line in pybase3.make_pretty_table_lines(curr):
print(line)
# o, alternativamente, invoca un método del objetos cursor para recuperar las filas
curr = conn.execute('select id, nombre as name, title from team order by title desc;')
rows = curr.fetchall()
print(f"{len(rows)} records retrieved.")
```

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

### Utilidad `dbfquery`

```bash
dbfquery <directorio_dbf>

# Ejemplo de uso

$ dbfquery db

Welcome to pybase3 SQL shell v. 1.98.7
SQL for dBase III+
Working directory: /home/ernesto/Programas/2025/python/pybase3 / 22 tables found.
Type 'help' for help.

sql> select * from teams where titles > 40 order by titles desc;

┌────┬──────────────────────────────────────────────────┬──────┐
│ id │                      nombre                      │titles│
├────┼──────────────────────────────────────────────────┼──────┤
│   1│River Plate                                       │    77│
├────┼──────────────────────────────────────────────────┼──────┤
│   2│Boca Juniors                                      │    75│
├────┼──────────────────────────────────────────────────┼──────┤
│   3│Racing Club                                       │    47│
├────┼──────────────────────────────────────────────────┼──────┤
│  13│Independiente                                     │    43│
└────┴──────────────────────────────────────────────────┴──────┘

sql> quit 
Bye, thank you for using SQL with dBase III

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

Para obtener más información, consulte la documentación a continuación:

<a href="docs/pybase3.html">Pybase3 Docs</a>

## Contribuciones

¡Se aceptan contribuciones! Abra un issue o envíe una solicitud de incorporación de cambios.

## Licencia

Este proyecto está licenciado bajo la licencia MIT. Consulte el archivo LICENCIA para obtener más detalles.

## Contacto

Para cualquier duda o sugerencia, por favor contacte con nosotros. [Domingo E. Savoretti](mailto:esavoretti@gmail.com).
