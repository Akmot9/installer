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
                withCredentials([string(credentialsId: '051e60a0-4a9b-4f9d-bfff-fc15b059b2e3', variable: 'MY_TOKEN')]) {
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

