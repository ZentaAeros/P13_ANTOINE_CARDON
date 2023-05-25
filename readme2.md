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

1. Connectez-vous à votre compte GitLab sur le site web.

2. Accédez à votre projet OC Lettings.

3. Assurez-vous que les variables d'environnement requises sont configurées dans les paramètres du projet GitLab.

4. Lancez le pipeline 

5. GitLab exécutera les étapes de déploiement spécifiées dans le fichier `.gitlab-ci.yml`.

6. Une fois le pipeline de déploiement terminé avec succès, l'application OC Lettings sera déployée automatiquement sur Heroku.

Assurez-vous de suivre attentivement ces étapes pour garantir un déploiement sans problème en utilisant le CI/CD de GitLab. Si vous rencontrez des problèmes lors du déploiement, référez-vous à cette documentation.
