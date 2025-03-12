Installation
============

Ce guide décrit comment installer et configurer le projet **Python-OC-Lettings-FR** en environnement de développement et en production.

Pré-requis
----------
- **Python 3.10** ou version compatible
- **Git**
- **Virtualenv** (recommandé pour le développement)
- **Docker** (pour le déploiement en conteneur)

Clonage du repository
---------------------
Pour cloner le projet depuis GitHub :

.. code-block:: bash

    git clone https://github.com/LuuNa-JD/Python-OC-Lettings-FR.git
    cd Python-OC-Lettings-FR

Création de l'environnement virtuel (Développement)
-----------------------------------------------------
Créez un environnement virtuel et activez-le :

.. code-block:: bash

    python3 -m venv venv
    source venv/bin/activate

Installation des dépendances
----------------------------
Installez les dépendances :

.. code-block:: bash

    pip install -r requirements.txt

Configuration de l'environnement
----------------------------------
Créez un fichier **`.env`** (qui ne doit pas être poussé sur GitHub) et configurez-y les variables essentielles. Par exemple, pour le développement :

.. code-block:: text

    DJANGO_SECRET_KEY=VotreCléSecrète
    DJANGO_DEBUG=True
    DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost
    DJANGO_CSRF_TRUSTED_ORIGINS=http://127.0.0.1,http://localhost
    SENTRY_DSN=Votre_Sentry_DSN

Pour la production, adaptez ces valeurs (notamment en passant à HTTPS) et assurez-vous d'avoir :

.. code-block:: text

    DJANGO_SECRET_KEY=VotreCléSecrèteDeProd
    DJANGO_DEBUG=False
    DJANGO_ALLOWED_HOSTS=yourdomain.com
    DJANGO_CSRF_TRUSTED_ORIGINS=https://yourdomain.com,https://www.yourdomain.com
    DOMAIN=yourdomain.com
    SENTRY_DSN=Votre_SENTRY_DSN

Base de données
---------------
En développement, la base SQLite est stockée localement dans ``oc-lettings-site.sqlite3``.
En production, on configure Docker pour persister la base via un volume.

Migrations et Collecte des fichiers statiques
-----------------------------------------------
Exécutez les migrations et collectez les fichiers statiques :

.. code-block:: bash

    python manage.py makemigrations
    python manage.py migrate
    python manage.py collectstatic --noinput

Utilisation de Docker (optionnel)
----------------------------------
Pour déployer l’application en conteneur :

.. code-block:: bash

    docker compose up -d --build
