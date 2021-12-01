# Présentation

## Fonctionnalités

### A1

Ce point est essentiellement gérer par la classe "Planificateur". Pour tester ce point, il faut remplacer la ligne 30 du fichier app/src/app.py `planificateur = Planificateur(get_db())` par `planificateur = Planificateur(get_db(), 5)` ce qui change les paramètres du BackgroundScheduler pour être lancé immédiatement. La valeur n'a pas d'importance.

On peut ensuite lancer l'application avec `make` et se déplacer sur la page de l'application(le back-end doit recevoir une requête pour commancer le téléchargement). Si la base de données n'existe pas, elle sera créée à app/src/db/data.db et les informations obtenues seront stockées à l'intérieur. Les quatres tables concernées sont :

- piscine
- patinoire
- glissade
- arrondissement

Il n'est pas nécessaire de créer la base de données au préalable ou d'ajouter les tables, l'application le fait automatiquement.

### A2

Il n'y a pas vraiment de moyens de tester cette fonctionnalité à moins de changer les paramètres du 'cron' à une autre heure. On peut regarder dans le code pour s'assurer que ce sont les bons paramètres. Comme l'horloge de la machine virtuelle est en UTC, le cron l'est aussi. Dans app/src/planificateur/planificateur.py, dans la fonction 'run', on peut voir que la version 'cron' du travail est planifiée pour l'heure zéro, qui est minuit.

### A3

Lancez l'application avec `make` à la racine du travail. Ouvrez une page à l'adresse `127.0.0.1:5000/doc`. La documentation devrait être affichée. Si elle ne l'est pas, c'est que le fichier n'a pas été généré, il faut donc entrer la commande `make doc` pour résoudre ce problème. Il faut que le logiciel 'raml2html' soit installé sur votre machine.

### A4

### B1

Suite à la création initiale de la base de données, il ne devrait pas être nécessaire de faire des modification. Toutes les installations devraient être considérées comme étant de nouvelles installations et, par conséquent, être envoyées dans un courriel aux adresses contenues dans le fichier app/src/fichier/dest_courriel.yaml. Vous pouvez soit ajouter une adresse à laquelle vous avez accès dans ce fichier(en respectant le format) ou simplement utiliser la première adresse du fichier. Cette adresse est celle qui envoit tous les courriels et elle s'envoie aussi chaque courriel.

Pour se connecter à l'adresse notifiante.

- adresse: raphy.inf5190.labo@gmail.com
- mot de passe: Mhs89pz6zrmfhCg

### B2

Un compte d'application Twitter permet un nombre limité de requêtes(50 par 15 minutes) ce qui est largement dépassé lors du téléchargement initial suite à la création
de la base de données. Vous devriez voir des messages d'erreurs apparaitre sur la console pour vous informer que la limite est dépassée. Pour vous assurer que les tweets ont bien été publiés, vous pouvez vous rendre sur le compte twitte @INF5190Montreal.
