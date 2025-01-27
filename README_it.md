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

# Libreria Python DBase III

Libreria Python pensata per manipolare i file di database DBase III. Consente di leggere, scrivere, aggiungere e aggiornare i record nel database.

A partire dalla versione 1.90. ... sono state aggiunte le classi Connection e Cursor, iniziando la strada verso la piena conformità con Python Database API Specification v2.0 (PEP 249).
A questo punto, sia Cursor che Connection supportano il metodo `execute`, che accetta i comandi `select, insert, update ed delete`. È in corso un ulteriore supporto per SQL (`create, ecc.`).
Queste funzionalità funzionano in modo stabile a partire dalla versione 1.98.3, anche se ci sono alcune limitazioni d'uso, principalmente il fatto che al momento le query sono ``table-centered'', il che significa che non funzionano su più di una tabella alla volta. Questo sarà affrontato nelle versioni future, poiché è un requisito per diventare completamente conforme.
Si spera che pybase3 venga elencato con gli altri moduli conformi a Python DB API (Sqlite3, MySQL, Postgre, ecc.)

Sebbene questo formato di file per database non sia più in uso, il presente lavoro è uno strumento utile per recuperare dati legacy, oltre che un omaggio a una bella parte della storia dei computer.

A partire dalle versioni aggiornate il 2025-01-04, `pybase3` supporta l'indicizzazione tramite file `.pmdx` (Python + .mdx), che si traduce in query sorprendentemente veloci. Vedi sotto per i dettagli.

## Caratteristiche

- Classi API DB: Connection e Cursor
- Leggi file di database DBase III
- Scrivi su file di database DBase III
- Aggiungi nuovi record
- Aggiorna record esistenti
- Filtra e cerca record
- Importa da/esporta in file `.csv`. (Novità nella v. 1.12.1) Vedere `import_from` e `export_to`
- Importa da/esporta in database `sqlite`. (Novità nella v. 1.13.1) Vedere `import_from` e `export_to`

## Installazione

Per installare la libreria, usa `pip` per scaricarla da Pypi. Questo è il metodo preferito:

```bash
pip install pybase3
```

oppure clona il repository e vai alla directory del progetto:

```bash
git clone https://github.com/sandy98/pybase3.git
cd pybase3
```

## Utilizzo

### Classe `Connection`

```python
import pybase3
from pybase3 import Connection

# Si connette alla directory 'db'. Saranno inclusi tutti i file .dbf al suo interno.
conn = Connection('db')
# Ottiene un oggetto Cursor dalla connessione eseguendo un comando SQL
curr = conn.execute('select id, nombre as name, titles from teams order by titles desc;')
# Passa il cursore a una funzione di formattazione dati
for line in pybase3.make_pretty_table_lines(curr):
print(line)
# oppure, in alternativa, richiama un metodo degli oggetti cursore per recuperare le righe
curr = conn.execute('select id, nombre as name, titles from teams order by titles desc;')
rows = curr.fetchall()
print(f"{len(rows)} record recuperati.")
```

### Classe principale

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

### utilità `dbfquery`

```bash
dbfquery <dbf_directory>

# Esempio di utilizzo

$ dbfquery db

Benvenuti in pybase3 SQL shell v. 1.98.7
SQL per dBase III+
Directory di lavoro: /home/ernesto/Programas/2025/python/pybase3 / 22 tabelle trovate.
Digita 'help' per la guida.

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

### Utilità di navigazione del database

```bash
python3 dbfview.py <dbf_file>
```

o, ancora meglio, se pybase3 è installato usando pip, installerà dbfview come uno script, in questo modo e possibile di fare così:

```bash
dbfview <dbf_file>
```

Una comoda utilità basata su CLI curses per esplorare i file .dbf.

### Utilità di test

```bash
python3 dbftest.py [-r|-d]
```

o, ancora meglio, se pybase3 è installato tramite pip, installerà dbftest come script, quindi:

```bash
dbftest [-r|-d]
```

Questo è un semplice script di test per il modulo pybase3.
Crea un database di test (`db/test.dbf`), aggiorna alcuni record e ne elimina uno.
Quindi scrive le modifiche nel file del database.
Lo script può essere eseguito con l'opzione -d per mostrare i risultati intermedi o con l'opzione -r per cancellare un test.dbf esistente.
Lo script creerà una directory 'db' nella directory corrente se non esiste.
Lo script creerà un file 'test.dbf' nella directory 'db' se non esiste.

### Utilizzo a livello di modulo

Emettendo il comando:

```bash
python3 -m pybase3 [-v|-i|-h]
```

viene richiamato il modulo stesso (più specificamente, __main__.py), con conseguente attraversamento del file system alla ricerca di file .dbf. Alla fine, se la ricerca ha esito positivo, all'utente viene offerto un menu numerato di file dbf esistenti, pronti per essere letti da dbfview.

A partire dalla versione 1.9.5 sono state aggiunte nuove opzioni: -v, --version per recuperare la versione corrente del software, -i, --info per ottenere informazioni complete e -h, --help per le istruzioni d'uso.

Un'opzione della riga di comando ``pybase3`` è stata aggiunta anche nella versione 1.9.5, che funziona allo stesso modo dell'invocazione del modulo, ad esempio:

```bash
pybase3 [-v|-i|-h]
```

### Commenti

Il modulo stesso, la classe DBaseFile e tutti i suoi metodi sono ampiamente documentati, quindi dovrebbe essere facile da seguire.

In sostanza, ogni istanza di DBaseFile, sia essa istanziata tramite un file DBase III esistente, o creata tramite il metodo factory DBaseFile.create(filename), è un oggetto simile a un elenco con capacità di indicizzazione, che funge anche da iteratore attraverso i record presenti nel file .dbf. Supporta anche il metodo 'len', che segnala il numero di record presenti nel database, anche quelli contrassegnati per l'eliminazione.
Oltre a ciò, c'è un gruppo di metodi pensati per la manipolazione dei dati (add_record per gli inserimenti, update_record per gli aggiornamenti e del_record per contrassegnare/deselezionare le eliminazioni).
C'è anche un gruppo di metodi (search, index, find, filter) per aiutare a recuperare i dati selezionati.

Nella fase attuale di sviluppo, non c'è supporto per i campi memo o indice, anche se questo è pianificato per le versioni future, qualora dovesse sorgere abbastanza interesse. La versione 1.14.2 aggiunge il metodo `execute` per eseguire istruzioni SQL, restituendo un oggetto Cursor.
Per ulteriori informazioni, vedere la documentazione di seguito:

<a href="docs/pybase3.md">Pybase3 Docs</a>

## Contributi

I contributi sono benvenuti! Si prega di aprire un issue o inviare una richiesta di pull.

## Licenza

Questo progetto è concesso in licenza con la licenza MIT. Per i dettagli, vedere il file LICENSE.

## Contatto

Per qualsiasi domanda o suggerimento, contattare [Domingo E. Savoretti](mailto:esavoretti@gmail.com).
