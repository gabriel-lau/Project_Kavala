pipeline {
    agent { 
        dockerfile true
        }
    stages {
        stage('test') {
            steps {
                sh 'python --version'
                sh 'pytest -v --cov Test'
            }
        }
        /*stage('build') {
            steps {
                sh 'python --version'
            }
        }*/
    }
}

