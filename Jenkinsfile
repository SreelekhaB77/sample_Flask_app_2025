pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git credentialsId: 'github-ssh1', url: 'git@github.com:SreelekhaB77/sample_Flask_app_2025.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-app .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker stop flask || true'
                sh 'docker rm flask || true'
            }
        }

        stage('Run New Container') {
            steps {
                sh 'docker run -d --name flask -p 5000:5000 flask-app'
            }
        }

        stage('Reload NGINX') {
            steps {
                sh 'echo "yourpassword" | sudo -S systemctl reload nginx'
            }
        }
    }
}
