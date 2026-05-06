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
                    // Jalankan scanner dari lokasi instalasinya
                    sh "${SCANNER_HOME}/bin/sonar-scanner"
                }
            }
        }
    }
}
