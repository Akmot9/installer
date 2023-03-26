pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'pyinstaller --onefile installer.py'
            }
        }
    }
}