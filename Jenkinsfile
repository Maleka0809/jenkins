pipeline {
    agent any

    environment {
        SCANNER_HOME = tool 'sonar-scanner'
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
                    
                    sh "${SCANNER_HOME}/bin/sonar-scanner -Dsonar.projectKey=Tugas-NCC-Maleka -Dsonar.projectName='Tugas NCC Maleka'"
                }
            }
        }
    }
}
