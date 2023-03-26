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
                    git push https://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@github.com/akmot9/installer.git HEAD:main
                '''
                }
            }
        }
    }
}

