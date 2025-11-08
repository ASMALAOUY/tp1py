class Contact:
    def __init__(self, nom: str, telephone: str, email: str):
        self.nom = nom
        self.telephone = telephone
        self.email = email

    @property
    def initiale(self):
        return self.nom[0].upper()

    def __str__(self):
        return f"{self.nom} — {self.telephone} — {self.email}"
