# 🏡 Python-OC-Lettings-FR

**Site web de gestion de locations pour Orange County Lettings, optimisé avec CI/CD et déploiement automatisé.**

📖 **Documentation complète :** [Disponible sur Read The Docs](https://python-oc-lettings-jd.readthedocs.io/fr/latest/)

---

## Développement local

### Prérequis

- **GitHub** (accès en lecture au repository)
- **Git CLI**
- **Interpréteur Python 3.10+**
- **Docker & Docker Compose** (optionnel pour tester en conteneur)

---

### Installation et exécution (sans Docker)

#### 1️⃣ **Cloner le repository**
```bash
git clone https://github.com/LuuNa-JD/Python-OC-Lettings-FR.git
cd Python-OC-Lettings-FR
```

#### 2️⃣ **Créer l'environnement virtuel**
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
```

#### 3️⃣ **Installer les dépendances**
```bash
pip install -r requirements.txt
```

#### 4️⃣ **Lancer l'application**
```bash
python manage.py runserver
```
**Accès à l'application :** [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Déploiement en Production (Docker + Traefik + Authelia)

L'application est déployée avec **Docker Compose** en utilisant **Traefik** pour le reverse proxy et **Authelia** pour l'authentification.

### **Prérequis**
- Une **machine virtuelle (VM) sous Linux (ex : OVH, AWS, etc.)**
- **Docker & Docker Compose installés**
- Un **nom de domaine** configuré pour pointer sur la VM

### **Lancer l'application en production**
```bash
docker compose up -d --build
```
**Accès à l'application :** `https://votre-domaine.com`

**Authentification via Authelia** : L'authentification est requise pour accéder à certaines sections de l'application comme l'administration Django.

---

## **CI/CD avec Jenkins**
Un pipeline **Jenkins** est utilisé pour l'intégration et le déploiement continus.

🔹 **Étapes du pipeline :**
1. **Linting** avec `flake8`
2. **Tests unitaires** avec `pytest`
3. **Build Docker**
4. **Déploiement sur le serveur**

---

## **Monitoring & Logs**
L'application est intégrée avec **Sentry** pour le suivi des erreurs.

**Accéder au Dashboard Sentry :** `https://sentry.io/organizations/organisation-name/projects/project-name/`

---

## **Commandes utiles**

### **Linting**
```bash
flake8
```

### **Tests unitaires**
```bash
pytest
```

### **Gestion de la base de données**
```bash
python manage.py migrate
python manage.py createsuperuser
```

**Accès à l'administration Django :** [https://votre-domaine.com/admin](https://votre-domaine.com/admin)

login : `admin`
password : `Abc1234!`

---

## **Licence**
Projet sous licence MIT.

---

**Besoin d'aide ?** Contactez-moi sur GitHub !
