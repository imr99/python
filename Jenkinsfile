pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE_NAME = 'mypython'
        DOCKER_HUB_CREDENTIALS = 'dockerhub_id'
        DOCKER_HUB_REPO = 'imr99/mypython'  // The full Docker Hub repository name
    }
    
    stages {
        stage('Clone Git Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/imr99/python.git'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${DOCKER_IMAGE_NAME} ."
                }
            }
        }
        
        stage('Push to Docker Hub') {
            steps {
                script {
                    withDockerRegistry(credentialsId: "${DOCKER_HUB_CREDENTIALS}", url: '') {
                        sh "docker tag ${DOCKER_IMAGE_NAME} ${DOCKER_HUB_REPO}:${BUILD_NUMBER}"
                        sh "docker push ${DOCKER_HUB_REPO}:${BUILD_NUMBER}"
                    }
                }
            }
        }
        stage('Docker Run') {
            steps {
                script {
                    def dockerImage = docker.image("${DOCKER_HUB_REPO}:${BUILD_NUMBER}")
                    sh 'docker stop $mypythonappContainer || true'
                    sh 'docker rm $mypythonappContainer || tru
                    dockerImage.run("-p 81:80 --rm --name mypythonappContainer")
                }
            }
        }
    }
}
