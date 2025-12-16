pipeline {
    agent any

    environment {
        IMAGE_NAME = "docker.io/greeshma6-7/todo-app"
        IMAGE_TAG  = "1.0"
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build Image with Podman') {
            steps {
                sh '''
                  echo "Building image using Podman..."
                  docker build -t $IMAGE_NAME:$IMAGE_TAG .
                '''
            }
        }

        stage('Push Image with Podman') {
            steps {
                sh '''
                  echo "Pushing image using Podman..."
                  docker push $IMAGE_NAME:$IMAGE_TAG
                '''
            }
        }

        stage('Deploy to RKE2 Kubernetes') {
            steps {
                sh '''
                  echo "Deploying to RKE2..."
                  kubectl apply -f k8s/deployment.yaml
                  kubectl apply -f k8s/service.yaml
                '''
            }
        }
    }
}
