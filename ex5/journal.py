from datetime import datetime

class JournalTaches:
    def __enter__(self):
        
        self.fichier =  open("journal.txt", "w", encoding="utf-8")
        return self

    def enregistrer(self, tache: str):
       
        timestamp = datetime.now().isoformat()
        self.fichier.write(f"{timestamp} - {tache}\n")

    def __exit__(self, exc_type, exc, tb):
       
        self.fichier.close()
