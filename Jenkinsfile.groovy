pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                sh 'pyinstaller --onefile installer.py'
            }
        }
        
        stage('Publish to GitHub') {
            steps {
                withCredentials([string(credentialsId: 'd774d336-975d-4a79-85fa-9039891a9996', variable: 'MY_TOKEN')]) {
                    sh '''
                        git config --global user.email "avicocyprien@yahoo.fr"
                        git config --global user.name "Akmot9"
                        git add .
                        git commit -m "Automated build"
                        git push https://USERNAME:${MY_TOKEN}@github.com/akmot9/installer.git HEAD:main
                    '''
                }
            }
        }
    }
}

