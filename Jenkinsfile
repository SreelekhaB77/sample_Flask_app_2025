pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'flask-app'
        DOCKER_TAG = 'latest'
        DOCKER_REGISTRY = 'docker.io'
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    // Checkout the Git repository
                    git 'git@github.com:SreelekhaB77/sample_Flask_app_2025.git'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Use the Docker Pipeline plugin to build the Docker image
                    docker.build("${DOCKER_REGISTRY}/${DOCKER_IMAGE}:${DOCKER_TAG}")
                }
            }
        }

        stage('Stop Existing Container') {
            steps {
                script {
                    // Stop the existing container if running
                    sh 'docker stop flask || true && docker rm flask || true'
                }
            }
        }

        stage('Run New Container') {
            steps {
                script {
                    // Run the new Docker container using the image built in the previous stage
                    docker.run("${DOCKER_REGISTRY}/${DOCKER_IMAGE}:${DOCKER_TAG}", '-d -p 5000:5000 --name flask')
                }
            }
        }

        stage('Reload NGINX') {
            steps {
                script {
                    // Reload NGINX to apply any changes
                    sh 'sudo systemctl reload nginx'
                }
            }
        }
    }

    post {
        always {
            // Cleanup and finalize the build
            echo 'Cleaning up...'
            // Stop and remove the container after the job is finished
            sh 'docker stop flask || true && docker rm flask || true'
        }
    }
}
