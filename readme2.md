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

Si vous souhaitez construire une image Docker de l'application, vous pouvez suivre ces étapes supplémentaires :

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
