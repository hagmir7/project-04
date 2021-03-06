from django.contrib.auth.forms import forms
from .models import *


class CrateAssociationForm(forms.ModelForm):
    class Meta:
        model = Association
        fields = ('nom', 'type', 'adresse', 'tel', 'fixe', 'facebook', 'twitter', )



class CrateMemberForm(forms.ModelForm):
    class Meta:
        model = Membre
        fields = ('nom', 'prenom', 'nationalite', 'email', 'photo', 'tel', 'fixe', 'date_naissance', 'association',)


class CrateEventrForm(forms.ModelForm):
    class Meta:
        model = Evenement
        fields = ('titre', 'description', 'date_debut', 'date_fine', 'liue', 'nbr_particip', 'tarif', 'image',)



class CrateDonorsForm(forms.ModelForm):
    class Meta:
        model = Douateur
        fields = ('nom', 'prenom', 'tel', 'email', )


class CrateDouateurAssForm(forms.ModelForm):
    class Meta:
        model = DouateurAss
        fields = ('association', 'douateur', 'montant', 'date', )



class CrateDepenseForm(forms.ModelForm):
    class Meta:
        model = Depense
        fields = ('category', 'montant', 'date',)




class CrateCoursForm(forms.ModelForm):
    class Meta:
        model = Cours
        fields = ('intitule', 'value_aoraire', 'description','cible','association',)


class CrateGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('intitule', 'nbr_etudient', 'date_debut','date_fine','cours',)

class CrateTacheForm(forms.ModelForm):
    class Meta:
        model = Tache
        fields = ('association', 'mumbre',)


class CrateSessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ('titre', 'description', 'heure_debut','heure_fine','evenement',)


class CrateEvPaForm(forms.ModelForm):
    class Meta:
        model = EvenementParticipant
        fields = ('participant', 'evenement', )


class CrateParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ('email', )





