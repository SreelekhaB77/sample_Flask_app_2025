pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    credentialsId: 'github-ssh1',
                    url: 'git@github.com:SreelekhaB77/sample_Flask_app_2025.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-app .'
            }
        }

        stage('Run Flask Container') {
            steps {
                sh '''
                docker stop flask || true
                docker rm flask || true
                docker run -d --name flask -p 5000:5000 flask-app
                '''
            }
        }
    }
}
