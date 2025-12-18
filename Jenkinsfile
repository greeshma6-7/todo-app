pipeline {
    agent { label 'host-agent' }

    environment {
        REGISTRY   = "docker.io"
        IMAGE_NAME = "greeshma258/todo-app"
        IMAGE_TAG  = "${BUILD_NUMBER}"
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build Image') {
            steps {
                sh '''
                  echo "Building image"
                  podman build -t ${REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG} .
                '''
            }
        }

        stage('Login to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh 'podman login ${REGISTRY} -u ${DOCKER_USER} -p ${DOCKER_PASS}'
                }
            }
        }

        stage('Push Image') {
            steps {
                sh 'podman push ${REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG}'
            }
        }

        stage('Deploy to RKE2') {
            steps {
                sh '''
                  sed -i "s|IMAGE_TAG|${IMAGE_TAG}|g" k8s/deployment.yaml
                  kubectl apply -f k8s/deployment.yaml
                  kubectl apply -f k8s/service.yaml
                '''
            }
        }
    }
}
