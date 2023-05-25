## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python configure_env.py`
- Configurez le nouveau fichier `.env` se trouvant à la racine du projet avec vos informations.
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`


## Déploiement

Le déploiement de l'application OC Lettings peut être automatisé en utilisant le CI/CD de GitLab. Le fichier `.gitlab-ci.yml` présent dans le repository est configuré pour gérer le processus de déploiement. Suivez les étapes ci-dessous pour effectuer le déploiement :

### Configuration requise

Avant de procéder au déploiement, assurez-vous d'avoir les éléments suivants :

- Un compte GitLab avec un projet créé.
- Un compte Heroku (https://www.heroku.com/) pour héberger l'application.
- Les variables d'environnement requises configurées dans les paramètres du projet GitLab :
  - `HEROKU_APP_NAME`: Le nom de votre application Heroku.
  - `HEROKU_API_KEY`: La clé API Heroku pour accéder à votre compte Heroku.
  - `DOCKER_USER`: Le nom d'utilisateur de votre compte Docker.
  - `DOCKER_PASSWORD`: Le mot de passe de votre compte Docker.
  - `SENTRY_DSN`: La clé DSN de Sentry pour la surveillance des erreurs.

### Étapes de déploiement

Suivez les étapes ci-dessous pour effectuer le déploiement de l'application en utilisant le CI/CD de GitLab :

1. Connectez-vous et créez une application en spécifiant le nom souhaité.

2. Connectez-vous à votre compte GitLab sur le site web.

3. Accédez à votre projet OC Lettings.

4. Assurez-vous que les variables d'environnement requises sont configurées dans les paramètres du projet GitLab.

5. Lancez le pipeline 

6. GitLab exécutera les étapes de déploiement spécifiées dans le fichier `.gitlab-ci.yml`.

7. Une fois le pipeline de déploiement terminé avec succès, l'application OC Lettings sera déployée automatiquement sur Heroku.

Assurez-vous de suivre attentivement ces étapes pour garantir un déploiement sans problème en utilisant le CI/CD de GitLab. Si vous rencontrez des problèmes lors du déploiement, référez-vous à cette documentation.

### Docker

#### Construire une image Docker de l'application

1. À la racine du projet, exécutez la commande suivante pour construire l'image Docker :

```shell
docker build -t nom_de_votre_image .
```

2. Une fois la construction terminée, vous pouvez exécuter le conteneur à partir de l'image créée en utilisant la commande suivante :

```shell
docker run -d -p 8000:8000 -e PORT=8000 nom_de_votre_image
```

3. Vous pouvez à présent accéder à l'application depuis votre navigateur internet à l'adresse : localhost:8000


#### Récupérez l'image de l'application depuis le Docker Hub

1. Executez la commande ci-dessous avec votre nom d'utilisateur, le nom de l'application ainsi que le hash du commit :

```shell
docker run -d -p 8000:8000 -e PORT=8000 nom_utilisateur/nom_application:hash
```

2. Vous pourrez ensuite aller sur votre navigateur internet à l'adresse : localhost:8000

#### Sentry
Sentry est une plateforme de gestion des erreurs en temps réel pour les applications. 
Suivez les étapes ci-dessous pour mettre en place Sentry dans votre projet :

1. Créez un compte sur Sentry (https://sentry.io/) si vous n'en avez pas déjà un.

2. Créez un nouveau projet dans Sentry pour votre application OC Lettings.

3. Dans le fichier `.env`, trouvez la ligne `SENTRY_DSN=`et définissez sa valeur sur la clé DSN fournie par Sentry.

4. Bravo ! Vous avez mis en place Sentry.
