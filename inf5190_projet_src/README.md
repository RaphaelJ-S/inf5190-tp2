# Projet réalisé pour le cours INF5190 - Automne 2021, UQAM

## Auteur

- Nom : Jacob-Simard
- Prénom : Raphaël
- Code permanent : JACR26038907
- Cours : INF5190
- Groupe : 30

## Table des matières

1. [Présentation du projet](#Présentation-du-projet)
2. [Détails du projet](#Détails-du-projet)
   - [Exécution](#Exécution)
   - [Particularités](#Particularités)
3. [Dépendances](#Dépendances)
4. [Structure du projet](#Structure-du-projet)

## Présentation du projet

Cette application vise à permettre aux utilisateurs de rester informé à propos des piscines, patinoire et glissades des arrondissement de Montréal. Pour les utilisateurs humains, elle offre des services de recherche par nom d'installation ou par arrondissement, de création de profil pour les notifications et d'envois de notifications pour avertir des mises-à-jours.

Ces services sont aussi offerts comme service REST.

## Détails du projet

### Exécution

Si vous avez accès aux commandes des Makefiles, entrez `make` pour partir le projet à partir de la racine(dans le dossier INF5190_PROJET_SRC).
Sinon, entrez `python -m app.src.app` pour faire la même chose. Il est très important d'entrer exactement cette commande parce que toutes les importations sont écrites avec des chemins absolus.

Pour générer la page de documentation raml, entrez `make doc`. Le fichier .html sera généré dans app/src/templates/documentation.html.

Pour exécuter pycodestyle sur tous les fichier python, entrez `make pep8`.

Pour exécuter tous les tests, entrez `make test`. Il n'y en a vraiment pas beaucoup.

Par défaut, l'application s'exécute sur `http://127.0.0.1:5000/`.

### Particularités

- Le projet utilise FlaskSQLAlchemy pour les intéraction avec la base de données sqlite. Vous n'avez pas besoin d'exécuter un script sql avant de partir le projet, l'application s'occupe de créer les tables et d'insérer les url nécessaires pour le téléchargement des données source.

- À noter que la table `source` garde en mémoire la dernière date des modifications ce qui veut dire que si vous faites des modifications directement dans la base de données alors que les dates sont à jours, l'application ne se rendra pas compte qu'il faut faire une vérification. Si vous voulez que le planificateur effectue toujours une vérification des données, regardez la fonction mise_a_jour dans le ficheir app/src/planificateur/planificateur.py et effectuez le changement décrit avant de lancer l'application.

- Le planificateur(la partie du projet qui s'occupe du téléchargement des données) commence dès que vous partez l'application et ses deux 'jobs' sont intialalisée: immédiatement(une seule fois) et à chaque jour à minuit.

- Le fichier de configuration pour les comptes courriel et twitter se trouve à `app/src/fichier/dest_courriel.yaml`. Vous devriez modifier les valeurs de `compte_twitter` et `courriel_envoyant` avant de démarrer l'application.

## Dépendances

Ce projet est une application web qui utilise Flask en back-end et du html/javascript en front-end.

- aniso8601==9.0.1
- APScheduler==3.8.1
- attrs==21.2.0
- Authlib==0.15.5
- BareNecessities==0.2.8
- bcrypt==3.2.0
- blinker==1.4
- boto3==1.19.12
- botocore==1.22.12
- certifi==2021.10.8
- cffi==1.15.0
- charset-normalizer==2.0.7
- click==8.0.3
- cryptography==35.0.0
- csvalidate==1.1.1
- dataclasses==0.6
- dicttoxml==1.7.4
- dnspython==2.1.0
- docutils==0.18
- dominate==2.6.0
- email-validator==1.1.3
- filelock==3.3.2
- Flask==2.0.2
- Flask-Bcrypt==0.7.1
- Flask-Bootstrap==3.3.7.1
- Flask-CSV==1.2.0
- Flask-json-schema==0.0.5
- Flask-Login==0.5.0
- Flask-Mail==0.9.1
- flask-marshmallow==0.14.0
- Flask-RESTful==0.3.9
- Flask-SQLAlchemy==2.5.1
- Flask-WTF==0.15.1
- greenlet==1.1.2
- idna==3.3
- importlib-metadata==4.8.1
- iniconfig==1.1.1
- itsdangerous==2.0.1
- Jinja2==3.0.2
- jmespath==0.10.0
- jsonschema==4.2.1
- Mail==2.1.0
- MarkupSafe==2.0.1
- marshmallow==3.14.0
- marshmallow-sqlalchemy==0.26.1
- numpy==1.21.4
- oauthlib==3.1.1
- packaging==21.2
- pandas==1.3.4
- pluggy==1.0.0
- py==1.11.0
- pycodestyle==2.8.0
- pycparser==2.20
- pycryptodome==3.11.0
- pyparsing==2.4.7
- pyrsistent==0.18.0
- pytest==6.2.5
- python-dateutil==2.8.2
- python-dotenv==0.19.1
- pytz==2021.3
- pytz-deprecation-shim==0.1.0.post0
- PyYAML==6.0
- requests==2.26.0
- requests-oauthlib==1.3.0
- s3transfer==0.5.0
- secret==0.8
- six==1.16.0
- SQLAlchemy==1.4.26
- tabulate==0.8.9
- toml==0.10.2
- tweepy==4.3.0
- twython==3.9.1
- tzdata==2021.5
- tzlocal==4.1
- urllib3==1.26.7
- visitor==0.1.3
- Werkzeug==2.0.2
- WTForms==2.3.3
- zipp==3.6.0

Autres dépendances au niveau système

- npm
- sqlite
- raml2html
- Makefile

## Structure du projet

- app/ : Racine du code
  - src/ : Dossier source du projet
    - app.py : Le point d'entrée du projet - routes & REST
    - db/ : Dossier database
      - base_donnees.py : Classe qui communique avec la db sqlite
      - data.db : La base de données sqlite
      - init_db.py : Fichier d'initialisation pour empêcher les importations circulaires
    - fichier/ : Dossier de fichiers de configuration
      - dest_courriel.yaml : Configuration pour les envois de courriel et de tweets
      - doc.raml : Configuration pour la documentation à générer avec raml2html
    - message/ : Dossier de fichiers pour la messagerie(courriel & tweets)
      - messagerie.py : Organisateur du processus de création et d'envois des notifications
      - builder/ : Dossier de création de notifications
        - courriel_builder.py : Builder d'une liste de courriels
        - tweet_builder.py : Builder d'une liste de tweets
        - notification_builder.py : Interface de builders de notifications
      - notification/ : Dossier des types de notifications
        - courriel.py : Représentation d'un courriel
        - tweet.py : Représentation d'un tweet
        - notification.py : interface d'un notification
    - model/ : Dossier des modélisation des tables de la base de données
      - arrondissement.py : La table arrondissement
      - glissade.py : La table glissade
      - patinoire.py : La table patinoire
      - piscine.py : La table piscine
      - source.py : La table source
    - planificateur/ : Dossier des opérations automatisées
      - maj.py : Organisateur des opérations suite à une mise-à-jour des données
      - planificateur.py : Organisateur du processus complet
      - telechargeur.py : Organisateur du téléchargement des données
      - parser/ : Dossier des parsers de données
        - parser.py : Interfaces de parsers
        - glissade_parser.py : Le parser pour les glissades
        - patinoire_parser.py : Le parser pour les patinoires
        - piscine_parser.py : Le parser pour les piscines
    - schema/ : Dossier des schemas
      - schema.py : JSON schema
    - service/ : Dossier des services
      - service.py : Contient la logique d'affaire pour les différents services
    - static/ : Dossier pour le front-end
      - css/ : Le style du projet
      - js/ : Les scripts du projets
      - vendor/ : Bootstrap et fontawesome
    - templates/ : Les pages web du projet
    - util/ : Dossier des fonctions utiles
      - conversion.py : Conversion entre les models et des listes
      - dates.py : Conversion de dates
  - tests/ : Dossier test du projet
    - message/ : Les quelques tests sur la messagerie et les notifications
    - planificateur/ : Les quelques tests sur le planificateur
- scripts/ : Contient des scripts nécessaire pour des commandes du Makefile
  - pycode.py : Exécute pycodestyle sur tous les fichiers pythons du projet.
- correction.md : Les explications pour la correction du projet
- Makefile
- README.md
