import os
import getpass
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import sys
import libreria_ai_per_tutti as ai
import pypdf
import time
import warnings # Necessario per evitare un warning di deprecation in FAISS

# Ignora i warning di deprecation in FAISS
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Se OPENAI_API_KEY esiste come variabile d'ambiente, la usa, altrimenti chiede con getpass
if not os.getenv("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Chiave API di Openai non rilevata. Inseriscila qui: ")

PATH = sys.argv[1] if len(sys.argv) > 1 else input("Inserisci il path del file con cui vuoi chattare (.pdf e .txt supportati): ")

def extract_pdf(url:str) -> str:
    pdf_text = ""
    with open(url, "rb") as pdf_file:
        pdf_reader = pypdf.PdfReader(pdf_file)
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text is not None:
                pdf_text += page_text
    return pdf_text

# Se è un .pdf, chiama la funzione extract_pdf, altrimenti usa il testo direttamente
if PATH.lower().endswith(".pdf"):
    text = extract_pdf(PATH)
elif PATH.lower().endswith(".txt"):
    with open(PATH, "r", encoding="utf-8") as file:
        text = file.read()
else:
    raise Exception("Formato non supportato. Carica un documento .pdf o .txt")

# Messaggio iniziale
print("Benvenuto!")
print("Questo è un chatbot che usa le API di ChatGPT per rispondere alle domande sul documento che hai caricato.")
print("In altre parole, puoi 'chattare' con il documento.")
print("")
time.sleep(2)

# Scelta del motore di gpt
print("Scegli il modello da utilizzare:")
print("1. gpt-3.5-turbo")
print("2. gpt-4")
input_model = input("Inserisci il numero del modello: ")
if input_model == "1" or input_model == "":
    MODEL = "gpt-3.5-turbo"
elif input_model == "2":
    MODEL = "gpt-4"
else:
    raise Exception("Scelta non esistente. Scegli 1 o 2 (o lascia vuoto per scegliere 1). Ricomincia.")


# Dividi in blocchi da 500 caratteri
def get_context(query) -> str:
    texts = ai.token_text_splitter(text=text, chunk_size=500, overlap=50)

    embeddings = OpenAIEmbeddings()

    db = FAISS.from_texts(texts, embeddings)
    docs = db.similarity_search(query)

    context = ""
    context += "*** " + docs[0].page_content

    # Se c'è più di 1 risultato, aggiungi 2 contesti
    if len(docs) > 1:
        context += "\n" + "*** " + docs[1].page_content
    return context

# CHAT
messages = []

def define_system_message(context:str) -> dict:
    return {"role": "system", "content": f"Sei un chatbot e il tuo obiettivo è rispondere alle domande dell'utente basandoti sul database che ti è stato fornito. Se la risposta non è presente nel database, dì all'utente che la sua risposta non è presente nel documento.\n\nDATABASE:\n\n{context}"}

def add_to_messages(role:str, content:str) -> dict:
    messages.append({"role": role, "content": content})

def get_message_history() -> str:
    """Questa funzione estrai tutti i 'content' dai vari messaggi e li mette in una stringa. usato per il contesto"""
    message_history = ""
    for message in messages:
        message_history += message["content"] + "\n"
    return message_history

while True:
    user_input = input("Tu: ")
    print("")
    add_to_messages(role="user", content=user_input)
    message_history = get_message_history()
    context = get_context(message_history)
    system_message = define_system_message(context)
    messages.insert(0, system_message)
    print("Assistente:")
    assistant = ai.gpt_call(engine=MODEL, messages=messages, temperature=0.4, stream=True)
    print("")
    add_to_messages(role="assistant", content=assistant)
    messages.pop(0)