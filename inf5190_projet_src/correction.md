# Rapport de correction pour le travail de session INF5190 - Automne 2021

## Identification

- Nom : Jacob-Simard
- Prénom : Raphaël
- Code permanent : JACR26038907
- Cours : INF5190
- Groupe : 30

## Fonctionnalités

### Présentation

Les fonctionnalités réalisée pour ce travail sont les suivantes :

- A1, A2, A3, A4, A5, A6
- B1, B2
- E1, E2, E3, E4

Comme la base de données va devoir être créée et remplie lors du départ de l'application et que ces opérations vont être réalisées automatiquement, il serait préférable de changer les configurations nécessaires(Changer l'adresse courriel de l'envoyant pour le cas B1 et le compte Twitter si nécessaire) pour les tests avant de partir l'application. Gardez en tête que la table source garde en mémoire la date de la dernière mise-à-jours.

De plus, suite à la création et au téléchargement des données à partir des fichiers externes, une bonnes partie des fonctionnalités(A1, A2, B1, B2, E3) pourront être testées sans avoir à faire des modification supplémentaires.

### A1

On peut lancer l'application avec `make` et se déplacer sur la page de l'application(le back-end doit recevoir une requête pour commancer le téléchargement). Si la base de données n'existe pas, elle sera créée à app/src/db/data.db et les informations obtenues seront stockées à l'intérieur. Les quatres tables concernées sont :

- piscine
- patinoire
- glissade
- arrondissement

Il n'est pas nécessaire de créer la base de données au préalable ou d'ajouter les tables, l'application le fait automatiquement.

fichiers concernés :

- `app/src/planificateur/planificateur.py` : Organise tous le processus
- `app/src/planificateur/telechargeur.py` : Télécharge et parse les données des différentes sources
- `app/src/planificateur/parser/` : Contient les fichiers des différents parsings
- `app/src/db/base_donnees.py` : Communique avec la base de données

### A2

Il n'y a pas vraiment de moyens de tester cette fonctionnalité à moins de changer les paramètres du 'cron' à une autre heure. On peut regarder dans le code pour s'assurer que ce sont les bons paramètres. Comme l'horloge de la machine virtuelle est en UTC, le cron l'est aussi. Dans app/src/planificateur/planificateur.py, dans la fonction 'run', on peut voir que la version 'cron' du travail est planifiée pour l'heure zéro, qui est minuit.

fichiers concernés :

- `app/src/planificateur/planificateur.py`

### A3

Lancez l'application avec `make` à la racine du travail. Ouvrez une page à l'adresse `127.0.0.1:5000/doc`. La documentation devrait être affichée. Si elle ne l'est pas, c'est que le fichier n'a pas été généré, il faut donc entrer la commande `make doc` pour résoudre ce problème. Il faut que le logiciel 'raml2html' soit installé sur votre machine.

fichiers concernés :

- `app/src/fichier/doc.raml` : Fichier de configuration
- `app/src/templates/documentation.html` : La page générée

### A4

Lancez l'application avec `make` à la racine du travail. Ouvrez une page à l'adresse `127.0.0.1:5000/installations?arrondissement=Verdun`, ce qui envoit une requête asynchrone à `/api/installations`. Vous devriez voir une liste de dictionnaires s'afficher représentant les différentes installations de l'arrondissement Verdun.

fichiers concernés:

- `app/src/app.py` : route '/api/installations'
- `app/src/service/service.py` : Pour la logique d'affaire
- `app/src/db/base_donnees.py` : Pour chercher les données

### A5

Lancez l'application avec `make` à la racine du travail. Ouvrez une page à l'adresse `127.0.0.1:5000/`. Vous devriez voir un formulaire s'afficher à l'écran. Le champ qui permet d'écrire quelque chose est celui qui envoit une
requête à A4. Vous pouvez écrire ce que vous voulez, l'application va vous retourner une liste des noms d'arrondissements valides. Entrez un des nom et les différentes installations devraient apparaitres. Il faut bien entendu que le téléchargement des sources ait eu lieu pour que ce point fonctionne.

fichiers concernés :

- Même que A4

### A6

Lancez l'application avec `make` à la racine du travail. Ouvrez une page à l'adresse `127.0.0.1:5000/`. Vous devriez voir un formulaire s'afficher à l'écran. Le champ 'select' est celui qui envoit une requête à `/api/installation`, choisissez donc un nom d'installation et l'installation devrait apparaitre. Il faut bien entendu que le téléchargement des sources ait eu lieu pour que ce point fonctionne.

fichiers concernés :

- `app/src/app.py` : route '/api/installation'
- `app/src/service/service.py` : Pour la logique d'affaire
- `app/src/db/base_donnees.py` : Pour chercher les données

### B1

Suite à la création initiale de la base de données, il ne devrait pas être nécessaire de faire des modification. Toutes les installations devraient être considérées comme étant de nouvelles installations et, par conséquent, être envoyées dans un courriel aux adresses contenues dans le fichier FICH_YAML(app/src/fichier/dest_courriel.yaml). Vous pouvez soit ajouter une adresse à laquelle vous avez accès dans ce fichier(en respectant le format) ou simplement utiliser la première adresse du fichier. Cette adresse est celle qui envoit tous les courriels et elle s'envoie aussi chaque courriel.

Vous pouvez aussi remplacer l'adresse courriel dans le fichier de configuration FICH_YAML (`app/src/fichier/dest_courriel.yaml`). L'objet 'courriel_cible' représente les profils qui vont potentiellement reçevoir des courriels, l'objet 'courriel_envoyant' représente l'adresse qui envera tous les courriels et l'objet 'compte_twitter' représente le compte qui va publier les tweets.

fichiers concernés :

- `app/src/fichier/dest_courriel.yaml` : Fichier de configuration
- `app/src/planificateur/maj.py` : Identifie les données modifiées
- `app/src/message/` : Contient le processus de construction et d'envois de notifications
- `app/src/db/base_donnees.py` : Pour chercher les données

### B2

Un compte d'application Twitter permet un nombre limité de requêtes(50 par 15 minutes) ce qui est largement dépassé lors du téléchargement initial suite à la création
de la base de données. Vous devriez voir des messages d'erreurs apparaitre sur la console pour vous informer que la limite est dépassée. Pour vous assurer que les tweets ont bien été publiés, vous pouvez vous rendre sur le compte twitter @INF5190Montreal.

fichiers concernés :

- `app/src/fichier/dest_courriel.yaml` : Fichier de configuration
- `app/src/planificateur/maj.py` : Identifie les données modifiées
- `app/src/message/` : Contient le processus de construction et d'envois de notifications
- `app/src/db/base_donnees.py` : Pour chercher les données

### E1

Le fichier de configuration utilisé pour les fonctionnalités 'E' est défini par la constante FICH_YAML(app/src/fichier/dest_courriel.yaml par défaut) dans le fichier app.py.

Le point E1 utilise le service REST `/api/profil` pour créé un profil dans le fichier yaml FICH_YAML à l'aide d'une requête POST avec un body contenant un
object json. ex :

{
"nom":"Jacque",
"email":"test@courrier.com",
"liste_arr": [
"Saint-Laurent",
"Verdun",
"Le Sud-Ouest"
]
}

Pour tester ce point, il faut simplement envoyer une requête selon les exigences énumérées plus haut.

fichiers concernés :

- `app/src/app.py` : route '/api/profil'
- `app/src/fichier/dest_courriel.yaml` : Fichier contenant la liste des adresses destinataires
- `app/src/service/service.py` : Logique d'affaire

### E2

Déplacez vous avec un fureteur sur la route `http:localhost:5000/profil`. Cette page fait exactement la même chose que le point E1 et est donc soumise aux même
exigences.

- `app/src/app.py` : route '/api/profil'
- `app/src/app.py` : route '/profil'
- `app/src/fichier/dest_courriel.yaml` : Fichier contenant la liste des adresses destinataires
- `app/src/service/service.py` : Logique d'affaire

### E3

Cette fonctionnalité peut-être vérifiée en même temps que B1 puisque le filtrage par rapport aux arrondissements se fait automatiquement basé sur
les noms d'arrondissements pour chaque profil du fichier de configuration FICH_RAML. Il faut simplement regarder le fichier FICH_YAML et prendre note
des liste d'arrondissements pour chaque profil(object yaml 'courriel_cible') et regarder si les courriels reçu correspondent.

- `app/src/fichier/dest_courriel.yaml` : Fichier de configuration
- `app/src/planificateur/maj.py` : Identifie les données modifiées
- `app/src/message/` : Contient le processus de construction et d'envois de notifications
- `app/src/db/base_donnees.py` : Pour chercher les données

### E4

Cette fonctionnalité utilise le service REST `/api/desabonnement/<token>` pour supprimer le profil du fichier FICH_YAML qui correspond au token dans le chemin.
Pour tester cette fonctionnalité, prenez note des profils dans le fichier FICH_YAML et cliquez sur le lien dans un des courriel que vous avez reçu. Ce lien vous amenera sur une page de l'application où vous devrez confirmer la supression. Vous pourrez ensuite vous assurer de la suppression en regardant le fichier FICH_YAML.

- `app/src/app.py` : route '/api/profil'
- `app/src/fichier/dest_courriel.yaml` : Fichier contenant la liste des adresses destinataires
- `app/src/service/service.py` : Logique d'affaire
