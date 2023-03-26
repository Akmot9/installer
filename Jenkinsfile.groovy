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
                withCredentials([usernamePassword(credentialsId: 'd6ec43f6-17ef-4301-a800-f3367e26cbc4', usernameVariable: 'GITHUB_USERNAME', passwordVariable: 'GITHUB_PASSWORD')]) {
                    sh '''
                        git config --global user.email "avicocyprien@yahoo.fr"
                        git config --global user.name "akmot9"
                        git add .
                        git commit -m "Automated build"
                        git push https://${GITHUB_USERNAME}:${GITHUB_PASSWORD}@github.com/akmot9/installer.git HEAD:main
                    '''
                }
            }
        }
    }
}
