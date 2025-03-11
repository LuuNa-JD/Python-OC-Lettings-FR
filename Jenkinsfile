pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "luunajd/django-lettings"
        PROJECT_DIR = "${env.WORKSPACE}"
        DEPLOY_DIR = "/home/jenkins/prod/django-lettings"
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
                    flake8 . &&
                    pytest --cov-report=term"
                    '''
                }
            }
        }
        stage('Check Coverage') {
            steps {
                script {
                    def status = sh(script: "coverage report --fail-under=80", returnStatus: true)
                    if (status != 0) {
                        error("La couverture de test est inférieure à 80%")
                    }
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
            when { branch 'master' }
            steps {
                script {
                    sh """
                    mkdir -p ${DEPLOY_DIR}

                    sed -i "s/TEMP_TAG/${DOCKER_TAG}/g" docker-compose.yml
                    cp docker-compose.yml ${DEPLOY_DIR}/docker-compose.yml

                    cp /home/jenkins/secrets/django.env ${DEPLOY_DIR}/.env

                    # Déploiement
                    cd ${DEPLOY_DIR}
                    export DOCKER_TAG=${DOCKER_TAG}  # Assurer que DOCKER_TAG est défini
                    docker compose down
                    docker compose pull
                    docker compose up -d
                    """
                }
            }
        }
    }
    post {
        success {
            echo "🚀 Pipeline terminé avec succès, application déployée !"
        }
        failure {
            echo "❌ Pipeline échoué, consultez les logs Jenkins."
        }
    }
}
