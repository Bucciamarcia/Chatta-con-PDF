# Chatta con PDF

Benvenuto nel progetto "Chatta con PDF". Questo progetto ti permette di interagire con un documento PDF o TXT attraverso un chatbot basato su GPT-3 o GPT-4. Puoi fare domande al chatbot e lui risponderà basandosi sul contenuto del documento che hai caricato.

## Video Youtube

Video Youtube con una presentazione di questo script: https://youtu.be/PflkbGgbpJE

## Come iniziare

Prima di tutto, devi avere Python installato sul tuo computer. Se non l'hai già fatto, puoi scaricare Python da [qui](https://www.python.org/downloads/).

Dopo aver installato Python, scarica o clona questo repository sul tuo computer.

## Installazione delle dipendenze

Questo progetto richiede alcune librerie Python per funzionare correttamente. Tutte le librerie necessarie sono elencate nel file `requirements.txt` incluso in questo repository.

Per installare queste librerie, apri un terminale, naviga nella cartella del progetto e digita il seguente comando:

```
pip install -r requirements.txt
```

## Come utilizzare lo script

Per utilizzare lo script, avrai bisogno di una chiave API di OpenAI. Se non ne hai una, puoi richiederla [qui](https://beta.openai.com/signup/).

Una volta ottenuta la chiave API, puoi impostarla come variabile d'ambiente sul tuo computer o inserirla direttamente quando lo script te lo chiede.

Per avviare lo script, apri un terminale, naviga nella cartella del progetto e digita il seguente comando:

```
python main.py [PATH]
```

Dove `[PATH]` è il percorso del file con cui vuoi chattare. Il file può essere un documento .pdf o .txt. Ad esempio:

```
python main.py C:\Users\Stefano\Documents\testo.pdf
```

In alternativa, si può usare semplicemente `python main.py` e inserire il percorso nel passo successivo quando lo chiede lo script.

Dopo aver avviato lo script, ti verrà chiesto di scegliere il modello da utilizzare (GPT-3 o GPT-4). Puoi semplicemente digitare `1` per GPT-3 o `2` per GPT-4.

A questo punto, puoi iniziare a chattare con il tuo documento! Basta digitare la tua domanda e premere invio. Il chatbot risponderà basandosi sul contenuto del documento.

## Note

Se incontri problemi o hai domande, puoi chiedere qui o nei commenti del video Youtube.

Se hai tante domande molto diverse tra loro da fare, è meglio uscire dalla chat (con `ctrl+c`) e far ripartire lo script da zero. Se fai tante domande diverse fra loro nella stessa finestra, lo script potrebbe confondersi (è un problema tipico della ricerca vettoriale). Se invece fai domande correlate tra loro, come approfondimenti, non dovrebbero esserci troppo problemi.

C'è sempre il limite di token, quindi dopo una finestra di chat molto lunga, prima o poi lo script andrà in errore.

Se vi viene l'errore `Exception: Formato non supportato. Carica un documento .pdf o .txt`, ma siete sicuri che il file sia giusto, potrebbe essere che il nome file o una cartella del percorso abbia uno spazio, tipo `C:\Users\Mario Rossi\documento.pdf`. Questo darà errore se lo inserite come argomento di linea con `python main.py [PATH]`. Invece, utilizzare `python main.py` e inserire il path quando lo chiede lo script per risolvere il problema.