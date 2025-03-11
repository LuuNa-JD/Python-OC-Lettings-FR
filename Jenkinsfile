pipeline {
    agent { label 'agent-ovh' }

    environment {
        DOCKER_IMAGE = "luunajd/django-lettings"
        PROJECT_DIR = "${env.WORKSPACE}"
        DEPLOY_DIR = "/var/lib/jenkins/prod/django-lettings"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'master', url: 'https://github.com/LuuNa-JD/Python-OC-Lettings-FR.git'
            }
        }

        stage('Set Docker Tag') {
            steps {
                script {
                    env.DOCKER_TAG = sh(script: "git rev-parse --short HEAD", returnStdout: true).trim()
                    echo "Docker Tag is set to: ${env.DOCKER_TAG}"
                }
            }
        }

        stage('Run Tests & Linting') {
            steps {
                script {
                    sh '''
                    docker run --rm -v $(pwd):/app -w /app python:3.10 bash -c "
                    python3 -m venv venv &&
                    source venv/bin/activate &&
                    pip install -r requirements.txt &&
                    flake8 .  &&
                    pytest --cov-report=term &&
                    coverage report --fail-under=80
                    "
                    '''
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} ${PROJECT_DIR}"
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                withDockerRegistry([credentialsId: 'DOCKER_HUB_CREDENTIALS', url: 'https://index.docker.io/v1/']) {
                    sh "docker push ${DOCKER_IMAGE}:${DOCKER_TAG}"
                }
            }
        }

        stage('Deploy to Production') {
            steps {
                withCredentials([file(credentialsId: 'DJANGO_ENV_FILE', variable: 'SECRET_ENV')]) {
                    sh """
                    echo "🚀 Déploiement de l'application..."

                    # Vérifie si DEPLOY_DIR existe, sinon le crée
                    mkdir -p ${DEPLOY_DIR}

                    # Vérification que docker-compose.yml contient bien TEMP_TAG avant de modifier
                    if grep -q "TEMP_TAG" docker-compose.yml; then
                        sed -i "s/TEMP_TAG/${DOCKER_TAG}/g" docker-compose.yml
                    fi

                    # Copie le docker-compose.yml mis à jour dans DEPLOY_DIR
                    cp docker-compose.yml ${DEPLOY_DIR}/docker-compose.yml

                    # Copie le fichier .env sécurisé depuis Jenkins Credentials
                    cp ${SECRET_ENV} ${DEPLOY_DIR}/.env

                    # Déploiement
                    cd ${DEPLOY_DIR}

                    # Arrêter et supprimer le conteneur s'il existe déjà
                    docker compose down || true
                    docker rm -f django-lettings || true

                    docker compose pull
                    docker compose up -d

                    # Forcer la collecte des fichiers statiques et vérifier SQLite
                    docker exec django-lettings python manage.py collectstatic --noinput
                    docker exec django-lettings python manage.py makemigrations
                    docker exec django-lettings python manage.py migrate

                    echo "🚀 Déploiement terminé avec succès !"
                    """
                }
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline terminé avec succès, application déployée !"
        }
        failure {
            echo "❌ Pipeline échoué, consultez les logs Jenkins."
        }
    }
}
