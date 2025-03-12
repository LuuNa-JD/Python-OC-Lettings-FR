Utilisation
===========

Ce guide explique comment lancer et utiliser le projet **Python-OC-Lettings-FR** en
environnement de développement et en production. Il détaille également la configuration
de production qui utilise Docker, Traefik, Authelia et un pipeline CI/CD avec Jenkins, afin de
garantir un déploiement sécurisé et automatisé.

En Développement
----------------
Pour lancer le serveur de développement Django, exécutez la commande suivante dans le répertoire du projet :

.. code-block:: bash

    python manage.py runserver

Accédez ensuite à l’application via votre navigateur à l’adresse :

    http://127.0.0.1:8000

En mode développement, Django sert directement les fichiers statiques depuis le dossier ``static/``, et
le fichier de base de données est local (``oc-lettings-site.sqlite3``).

En Production (avec Docker, Traefik, Authelia et Jenkins CI/CD)
---------------------------------------------------------------
Pour lancer l’application en production, assurez-vous d’avoir configuré correctement votre fichier
**.env** pour la production. Par exemple, le fichier **.env** de production doit contenir :

.. code-block:: text

    DJANGO_SECRET_KEY=VotreCléSecrèteDeProd
    DJANGO_DEBUG=False
    DJANGO_ALLOWED_HOSTS=yourdomain.com
    DJANGO_CSRF_TRUSTED_ORIGINS=https://yourdomain.com,https://www.yourdomain.com
    DOMAIN=yourdomain.com
    SENTRY_DSN=Votre_SENTRY_DSN

L’application est déployée via Docker Compose. Pour construire et lancer l’application, exécutez :

.. code-block:: bash

    docker compose up -d --build

Configuration de Traefik et Authelia
-------------------------------------
En production, le reverse proxy **Traefik** est utilisé pour :

- Gérer le routage des requêtes HTTP/HTTPS.
- Fournir le SSL automatique via Let’s Encrypt.
- Rediriger les requêtes vers le conteneur Django sur le port 8000.

Par ailleurs, **Authelia** est intégré en tant que middleware de sécurité pour :

- Imposer une authentification forte (2FA) sur les accès sensibles, notamment l’interface d’administration.
- Contrôler l’accès en fonction du domaine et des règles définies.

Ces services (Traefik et Authelia) doivent être installés et configurés sur la machine de production.
Les extraits de configuration dans le fichier ``docker-compose.yml`` de production détaillent leur rôle et leurs paramètres.

Pipeline CI/CD avec Jenkins
---------------------------
Le déploiement en production est automatisé via un pipeline CI/CD géré par **Jenkins**. À chaque commit sur la branche master, Jenkins :

- Exécute les tests et le linting.
- Construit une image Docker de l’application.
- Pousse l’image sur Docker Hub.
- Déploie automatiquement l’application sur la VM de production à l’aide de Docker Compose.

Ainsi, toute modification apportée au code est rapidement déployée en production, garantissant ainsi
une mise à jour continue et fiable de l’application.

Accès à l’Administration
-------------------------
L’interface d’administration Django est accessible à l’adresse :

.. code-block:: text

    https://yourdomain.com/admin/

    login: admin
    password: Abc1234!

Pour éviter des erreurs de sécurité, assurez-vous que votre domaine figure dans **ALLOWED_HOSTS** et
que **CSRF_TRUSTED_ORIGINS** inclut les URLs en HTTPS.

Configuration de Production et Infrastructure
----------------------------------------------
Pour reproduire exactement cette configuration en production, votre VM devra être équipée des éléments suivants :

- **Docker et Docker Compose** : Pour exécuter l’application et gérer les volumes persistants (base de données et fichiers statiques).
- **Traefik** : Pour le reverse proxy, la gestion du SSL et le routage des requêtes.
- **Authelia** : Pour la sécurité des accès (authentification forte sur l’administration et services sensibles).
- **Jenkins CI/CD** : Pour automatiser les tests, la construction des images Docker et le déploiement continu de l’application.

Les fichiers de configuration (docker-compose.yml, .env, configuration de Traefik, configuration d’Authelia, Jenkinsfile) présents dans le dépôt décrivent en détail l’architecture complète et permettent une mise en place répétable.

Conclusion
----------
En résumé, le projet **Python-OC-Lettings-FR** est conçu pour fonctionner en mode développement et en production
avec une architecture modulaire. En production, Docker, Traefik, Authelia et un pipeline CI/CD Jenkins assurent
un déploiement sécurisé, automatisé et facilement maintenable. La documentation, hébergée sur Read the Docs, se met à jour
automatiquement à chaque commit, garantissant ainsi que les informations fournies sont toujours à jour.

Pour toute question ou pour obtenir de l’aide, veuillez consulter les ressources suivantes :

- [Read the Docs Documentation](https://docs.readthedocs.io/en/stable/)
- [Traefik Documentation](https://doc.traefik.io/traefik/)
- [Authelia Documentation](https://www.authelia.com/docs/)
- [Jenkins Documentation](https://www.jenkins.io/doc/)

---

Ce fichier `usage.rst` offre une vue d'ensemble claire du fonctionnement en développement et en production, en précisant les technologies utilisées et les prérequis pour reproduire cette architecture. Vous pouvez l'adapter en fonction de votre configuration précise et le compléter avec des captures d'écran ou des liens vers des tutoriels pour chaque composant si nécessaire.
