# projet_11

Ce projet est un clone du projet d'application développé pour Güdlft, via le framework Flask, dans lequel sont implémentés plusieurs tests.

Afin de faire fonctionner, puis de tester cette application en local, veuillez suivres les indications suivantes.

## Clônage du projet

Tout d'abord, clônez en local le dépôt distant via la commande suivante dans votre terminal :

    $ git clone https://github.com/Benoitrenou/projet_11.git

## Création de l'environnement virtuel

Pour créer un environnement virtuel, depuis votre terminal de commande, effectuez les commandes suivantes :

### Sous Linux/ MAC OS

    $ python -m venv <environment_name>
    exemple : python -m venv venvAPI
    
### Sous Windows:
    
    $ virtualenv <environment_name>
    exemple : virtualenv venvAPI 
    
## Activation de l'environnement virtuel 

### Sous Linux / MAC OS:

    $ source <environment_name>/bin/activate
    exemple : source venvAPI/bin/activate
   
### Sous Windows:

    $ source <environment_name>/Scripts/activate
    exemple : source venvAPI/Scripts/activate
    
## Installation des packages : 

Afin que les packages nécessaires au fonctionnement de l'application soient installés sur l'environnement virtuel, entrez la commande suivante :

    $ pip install -r requirements.txt

## Lancement de l'application

Flask demande à ce que vous définissez un fichier python comme variable d'environnement. Vous devez définir le fichier <code>server.py</code> comme étant ce fichier. Suivez les instructions données via ce lien [here](https://flask.palletsprojects.com/en/2.0.x/quickstart/) pour plus de détails.

Puis depuis le répertoire Python_Testing, lancez l'application via : 

    $ flask run

## Tests

Pour lancer l'ensemble des tests, ouvrez un second terminal et lancez depuis le répertoire Python_Testing :

    $ pytest

Pour lancer une session de tests de performance, placez vous dans le répertoire Python_Testing/tests/performance_tests et lancez la commande suivante :

    $ locust

Pour vérifier la couverture de tests et émettre un rapport concernant celle-ci, complémentez la commande pytest :

    $ pytest --cov=. --cov-report html

Les données de ces tests sont également disponibles dans le répertoire data_tests.
