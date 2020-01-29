pipeline {
    agent {
        docker 
        { 
            image 'node:7-alpine' 
            } 
            }
    stages {
        stage('test') {
            steps {
                sh 'pytest -v -cov'
            }
        }
        /*stage('build') {
            steps {
                sh 'python --version'
            }
        }*/
    }
}
