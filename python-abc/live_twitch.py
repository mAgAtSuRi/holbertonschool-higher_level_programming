from abc import ABC, abstractmethod

class Media(ABC):
	"""classe abstraite pour tout type de média"""
	@abstractmethod
	def info(self):
		pass

class Livre(Media):
	__total_livres = 0

	def __init__(self, titre, auteur):
		self.__total_livres += 1
		self.__titre = titre
		self.__auteur = auteur
		self.__disponible = True

		@property
		def titre(self):
			return self.__titre
		
		@property
		def auteur(self):
			return self.__auteur
		
		@property
		def disponible():
			return self.__disponible
		
		@disponible.setter
		def disponible(self, value):
			if isinstance(value, bool):
				self.__disponible = value
			else:
				print("La disponibilité doit être True ou False")

	def emprunter(self):
		if self.__disponible:
			self.__disponible = False
			print(f"{self.__titre} a été emprunté")
		else:
			print(f"{self.__titre} n'est pas disponible")
		
	def rendre(self):
		self.__disponible = True
		print(f"{self.__titre} a été rendu")

	def __str__(self):
		dispo = "disponible" if self.__disponible else "emprunté"
		return dispo
	

	
	# Méthodes de classe
	@classmethod
	def total_livres(cls):
		return cls.__total_livres

class LivreAudio(Livre):
	def __init__(self, titre, auteur, duree):
		super().__init__(titre, auteur)
		self.__duree = duree
	
	@property
	def duree(self):
		return self.__duree
	
	@duree.setter
	def duree(self, value):
		if isinstance(value, int) and value > 0:
			self.__duree = value
	
	# polymorphisme
	def __str__(self):
		dispo = "disponible" if self.__disponible else "emprunté"
		return f"{self.titre} écrit par {self.auteur} - {self.duree} minutes"
	
	def info(self):
		print("methode info impélmentée")


class Bibliotheque:
	"""classe gerant une collection de livres"""
	def __init__(self, nom):
		self.__nom = nom
		self.__livres = []
	
	@property
	def nom(self):
		return self.__nom
	
	@property
	def livres(self):
		return self.__livres
	
	def ajouter(self, livre):
		if isinstance(livre, Livre):
			self.__livres.append(livre)
			print(f"{livre.titre} a été ajouté à {self.nom}")
		else:
			print("merci d'ajouter uniquement des livres")
	
	def afficher(self):
		if not self.__livres:
			"La bibliotheque est vide"
		else:
			for livre in self.__livres:
				print(livre)
	def trouver_par_titre(self, titre):
		return [livre for livre in self.__livres if livre.titre.lower() == titre.lower()]
	def emprunter_livre(self, titre):
		livres = self.trouver_par_titre(titre)
		if livres:
			livres[0].emprunter()
		else:
			print("Le livre {titre} est non trouvé")

	def rendre_livre(self):
		livres = self.trouver_par_titre(titre)
		if livres:
			livres[0].rendre()
		else:
			print("Le livre {titre} est non trouvé")

my_book = Livre("Tristan", "Holberton")

my_bibliotheque = Bibliotheque("Bibli frejus")
my_bibliotheque.ajouter(my_book)