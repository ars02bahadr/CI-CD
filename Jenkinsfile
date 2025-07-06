pipeline {
    agent any

    environment {
        IMAGE_NAME = "bahadir02ars/ci-cd"
        TAG = "${GIT_COMMIT}"
    }

    stages {
        stage('Kodu Klonla') {
            steps {
                checkout scm
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t $IMAGE_NAME:$TAG .'
            }
        }

        stage('Docker Push') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh '''
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker push $IMAGE_NAME:$TAG
                    '''
                }
            }
        }

        stage('Deploy (opsiyonel)') {
            steps {
                sh 'kubectl apply -f k8s/deployment.yaml'
            }
        }
    }
}
