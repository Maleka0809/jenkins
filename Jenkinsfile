pipeline {
    agent any
    
    tools {
        sonarQubeScanner 'sonar-scanner'
    }

    stages {
        stage('Clone Repository') {
            steps {
                echo 'Mengambil kode dari GitHub...'
                checkout scm
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    echo 'Memulai analisis SonarQube...'
                    sh 'sonar-scanner'
                }
            }
        }
    }
}
