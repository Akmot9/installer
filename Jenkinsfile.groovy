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
                
                sh '''
                    git config --global user.email "avicocyprien@yahoo.fr"
                    git config --global user.name "Akmot9"
                    git add .
                    git commit -m "Automated build"
                    git push https://github.com/akmot9/installer.git HEAD:main
                '''
                
            }
        }
    }
}

