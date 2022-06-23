from statistics import mode
from django.contrib.auth.models import User
from django.db import models



class Association(models.Model):
    nom = models.CharField(max_length=200)
    type = models.CharField(max_length=300)
    adresse = models.CharField(max_length=200)
    tel = models.CharField(max_length=20)
    fixe = models.CharField(max_length=20)
    facebook = models.CharField(max_length=300)
    twitter = models.CharField(max_length=300)

    def __str__(self):
        return self.nom


class Douateur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    tel = models.CharField(max_length=20)
    email = models.EmailField()


    def __str__(self):
        return self.nom + " " + self.prenom



class DouateurAss(models.Model):
    association = models.ForeignKey(Association, on_delete=models.CASCADE)
    douateur = models.ForeignKey(Douateur, on_delete=models.CASCADE)
    montant = models.FloatField()
    date = models.DateTimeField(auto_now=True)


class Depense(models.Model):
    category = models.CharField(max_length=100)
    montant = models.FloatField()
    date = models.DateTimeField(auto_now=True)



class Cours(models.Model):
    intitule = models.FloatField()
    value_aoraire = models.TimeField()
    description = models.TextField()
    cible = models.CharField(max_length=100)
    association = models.ForeignKey(Association, on_delete=models.CASCADE)



class Group(models.Model):
    intitule = models.FloatField()
    nbr_etudient = models.IntegerField()
    date_debut = models.DateTimeField()
    date_fine = models.DateTimeField()
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE)


class Mumbre(models.Model):
    nome = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    nationalite = models.CharField(max_length=60)
    email = models.EmailField()
    photo = models.ImageField(upload_to='photos')
    tel = models.CharField(max_length=20)
    fixe = models.CharField(max_length=20)
    date_naissance = models.DateTimeField()
    association = models.ForeignKey(Association, on_delete=models.CASCADE)


class Tache(models.Model):
    association = models.ForeignKey(Association, on_delete=models.CASCADE)
    mumbre = models.ForeignKey(Mumbre, on_delete=models.CASCADE)



class Evenement(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    date_debut = models.DateTimeField()
    date_fine = models.DateTimeField()
    heu =  models.CharField(max_length=100)
    nbr_particip = models.IntegerField()
    tarif = models.FloatField()
    image = models.ImageField(upload_to='EvenementEmage')

class Participant(models.Model):
    email = models.ImageField()


class EvenementParticipant(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    evenement = models.ForeignKey(Evenement, on_delete=models.CASCADE)


class Session(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    heure_debut = models.TimeField()
    heure_fine = models.TimeField()
    evenement = models.ForeignKey(Evenement, on_delete=models.CASCADE)

















