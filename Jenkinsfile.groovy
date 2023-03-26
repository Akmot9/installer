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
                withCredentials([string(credentialsId: 'a6de0d16-7485-4296-9f1d-09394672d515', variable: 'MY_TOKEN')]) {
                    sh '''
                        git config --global user.email "avicocyprien@yahoo.fr"
                        git config --global user.name "Akmot9"
                        git add .
                        git commit -m "Automated build"
                        git push https://USERNAME:TOKEN@github.com/akmot9/installer.git HEAD:main
                    '''
                }
            }
        }
    }
}
