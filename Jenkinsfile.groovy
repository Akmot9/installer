pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                // Clone your code repository here
                // Install any necessary dependencies
            }
        }

        stage('Compile') {
            steps {
                sh '''
                    # Install PyInstaller
                    pip install pyinstaller

                    # Compile your Python script using PyInstaller
                    pyinstaller --onefile your_script.py
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    # Run the compiled executable
                    dist/your_script
                '''
            }
        }
    }
}