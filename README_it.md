<p align="center">
  <img src="https://raw.githubusercontent.com/sandy98/pybase3/main/img/pybase3t.png" alt="pybase3 logo">
</p>

# Libreria Python DBase III

Libreria Python pensata per manipolare i file di database DBase III. Consente di leggere, scrivere, aggiungere e aggiornare i record nel database.

Sebbene questo formato di file per database non sia più in uso, il presente lavoro è un minitool utile per recuperare dati legacy, oltre che un omaggio a una bella parte della storia dei computer.

A partire dalle versioni aggiornate il 2025-01-04, `pybase3` supporta l'indicizzazione tramite file `.pmdx` (Python + .mdx), che si traduce in query sorprendentemente veloci. Vedi sotto per i dettagli.

## Caratteristiche

- Leggi file di database DBase III
- Scrivi su file di database DBase III
- Aggiungi nuovi record
- Aggiorna record esistenti
- Filtra e cerca record

## Installazione

Per installare la libreria, clonare questo repository e andare alla directory del progetto:

```bash
git clone https://github.com/sandy98/pybase3.git
cd pybase3
```

oppure

```bash 
pip install pybase3
```

## Utilizzo

### Classe principale

```python
from pybase3.dbase3 import DBaseFile, FieldType
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
Questo è un semplice script di test per il modulo dbase3.
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

Un'opzione della riga di comando ```pybase3``` è stata aggiunta anche nella versione 1.9.5, che funziona allo stesso modo dell'invocazione del modulo, ad esempio:
```bash
pybase3 [-v|-i|-h]
```
### Commenti

Il modulo stesso, la classe DBaseFile e tutti i suoi metodi sono ampiamente documentati, quindi dovrebbe essere facile da seguire.

In sostanza, ogni istanza di DBaseFile, sia essa istanziata tramite un file DBase III esistente, o creata tramite il metodo factory DBaseFile.create(filename), è un oggetto simile a un elenco con capacità di indicizzazione, che funge anche da iteratore attraverso i record presenti nel file .dbf. Supporta anche il metodo 'len', che segnala il numero di record presenti nel database, anche quelli contrassegnati per l'eliminazione.
Oltre a ciò, c'è un gruppo di metodi pensati per la manipolazione dei dati (add_record per gli inserimenti, update_record per gli aggiornamenti e del_record per contrassegnare/deselezionare le eliminazioni).
C'è anche un gruppo di metodi (search, index, find, filter) per aiutare a recuperare i dati selezionati.

Nella fase attuale di sviluppo, non c'è supporto per i campi memo o indice, anche se questo è pianificato per le versioni future, qualora dovesse sorgere abbastanza interesse. È anche pianificato un metodo `exec` per eseguire istruzioni di tipo SQL. Non funzionante al momento.

Per ulteriori informazioni, vedere la documentazione di seguito.

## Documentazione

### Classi

#### `DBaseFile`

Classe per manipolare i file di database DBase III.

### Metodi 'dunder' e 'privati'

- `__init__(self, filename: str)`: Inizializza un'istanza di DBase3File da un file dbf esistente.
- `__del__(self)`: Chiude il file del database quando l'istanza viene distrutta.
- `__len__(self)`: Recupera il numero di record nel database, inclusi i record contrassegnati per essere eliminati. Consente la scrittura: `len(dbasefileobj)`
- `__getitem__(self, key)`: Recupera un singolo record o un elenco di record (se si usa la notazione slice) dal database. Consente: `dbasefileobj[3]` or `dbasefileobj[3:7]`  
- `__iter__(self)`: Recupera un iteratore sui record nel database. Consente `for record in dbasefileobj: ...`
- `__str__(self)`:  Recupera una rappresentazione testuale del database.
- `_init(self)`: Iinizializza la struttura del database leggendo l'intestazione e i campi. Pensato per uso privato da parte di istanze DBaseFile.
- `def _test_key(self, key)`: Verifica se la chiave è compresa nell'intervallo valido degli indici dei record. Genera un IndexError se la chiave è fuori dall'intervallo. Pensato solo per uso interno.
    
### Metodi di classe.

- `create(cls, filename: str, fields: List[Tuple[str, FieldType, int, int]])`: Crea un nuovo file di database DBase III con i campi specificati. Recupera un oggetto DbaseFile che punta al file dbase appena creato.

### Metodi di manipolazione dei dati

- `add_record(self, record_data: dict)`: Aggiunge un nuovo record al database.
- `update_record(self, index: int, record_data: dict)`: Aggiorna un record esistente nel database.
- `save_record(self, key, record)`: Scrive un record (dizionario con nomi di campo e valori di campo) nel database all'indice specificato. Parametri: la chiave è l'indice (posizione basata su 0 nel file dbf). record è un dizionario corrispondente a un elemento nel database(i.e: {'id': 1, 'name': "Jane Doe"}) Utilizzato internamente da `update_record` 
- `del_record(self, key, value = True)`: Contrassegna per l'eliminazione il record identificato dall'indice 'key', o lo deseleziona se `value == False`. Per cancellare efficacemente il record dal disco, l'eliminazione deve essere confermata tramite `dbasefileobj.commit()`
- `commit(self, filename=None)`: Precedentemente denominato `write`, scrive il file corrente sul disco, saltando i record contrassegnati per l'eliminazione. Se viene fornito un nome file, diverso dal nome file corrente, salva il file del database nella nuova destinazione, mantenendo il nome file precedente così com'è. Vale la pena notare che `add_record` e `update_record` eseguono il commit delle modifiche su disco immediatamente, quindi non è necessario chiamare `commit` dopo averle usate. Non fa male farlo, comunque.

### Metodi di ricerca/filtraggio dei dati

-  `search(self, fieldname, value, start=0, funcname="", compare_function=None)`: Cerca un record con il valore specificato nel campo specificato, a partire dall'indice specificato, per il quale la funzione di confronto specificata Recupera True. Recupera una tupla con indice:int e record:dict
-  `find(self, fieldname, value, start=0, compare_function=None)`: Wrapper per search() con funcname="find". Recupera il primo record (dizionario) trovato oppure None se non viene trovato alcun record che soddisfi i criteri specificati.
-  `index(self, fieldname, value, start=0, compare_function=None)`:  Wrapper per search() con funcname="index". Recupera l'indice del primo record trovato, oppure -1 se non viene trovato alcun record che soddisfi i criteri specificati.
-  `filter(self, fieldname, value, compare_function=None)`:  Recupera un elenco di record (dizionari) che soddisfano i criteri specificati.
- `exec(self, sql_cmd:str)`: Pensato per recuperare dati in modo personalizzato. Non ancora operativo. L'invocazione genera un errore NotImplemented.

### Metodi di elencazione dei dati

- `list(self, start=0, stop=None, fieldsep="|", recordsep='\n', records:list=None)`: restituisce un elenco di record dal database, iniziando da 'start', terminando da 'stop' o EOF, con campi separati da 'fieldsep' e record separati da '\n'. Se 'records' non è None, viene utilizzato l'elenco fornito invece di recuperare i valori dal database.
- `csv(self, start=0, stop=None, records:list = None)`: wrapper per 'list', utilizzando ',' come fieldsep.
- `table(self, start=0, stop=None, records:list = None)`: recupera i record selezionati utilizzando il formato ad hoc, lo stesso fornito da sqlite3 CLI in modalità .table.
- `pretty_table(self, start=0, stop=None, records:list = None)`: Recupera i record selezionati utilizzando un formato ad hoc, come `table` ma con linee più graziose.
- `lines(self, start=0, stop=None, records:list = None)`: Recupera i record selezionati con i valori dei campi allineati alle loro larghezze.

Vale la pena notare che tutti questi ultimi cinque metodi restituiscono generatori anziché elenchi, il che li rende molto più leggeri in caso di recordset ingombranti.

### Metodi statici (funzioni ausiliarie per la ricerca/filtraggio)

- `istartswith(f: str, v: str) -> bool`: Controlla se la stringa `f` inizia con la stringa `v`, ignorando la distinzione tra maiuscole e minuscole.
- `iendswith(f: str, v: str) -> bool`: Controlla se la stringa `f` termina con la stringa `v`, ignorando la distinzione tra maiuscole e minuscole.

### Proprietà

- 'fields': Recupera l'elenco dei campi da cui vengono assemblati i record del database. Ogni oggetto campo nell'elenco ha un nome, un tipo (come da FieldType Enum) e una lunghezza.

- 'field_names': Recupera un elenco con il nome di ogni campo nel database.

- 'field_types': Recupera un elenco con il tipo di ogni campo nel database.

- 'field_lengths': Recupera un elenco con la lunghezza di ogni campo nel database.

- 'max_field_lengths': restituisce la lunghezza massima del campo specificato (inclusa la lunghezza del nome del campo) nel database. Utile per recuperare righe con larghezza regolata per ogni campo. Utilizza internamente `def max_field_length(self, field)`

- 'tmax_field_lengths': uguale a max_field_lengths, versione thread, in un tentativo non riuscito di accelerare il processo. In ogni caso, funziona.

## Contributi

I contributi sono benvenuti! Si prega di aprire un issue o inviare una richiesta di pull.

## Licenza

Questo progetto è concesso in licenza con la licenza MIT. Per i dettagli, vedere il file LICENSE.

## Contatto

Per qualsiasi domanda o suggerimento, contattare [Domingo E. Savoretti](mailto:esavoretti@gmail.com).


