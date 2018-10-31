pipeline {
    
    agent any 
    stages {
        stage('Add docker to PATH') {
            steps {
                sh 'PATH=$PATH:/usr/local/bin/'
            }
        }
    }
    
    agent { docker { image 'python:3.5.1' } }
    stages {
        stage('Build') {
            steps {
                sh 'echo "Hello World"'
                sh '''
                    echo "Multiline shell steps works too"
                    ls -lah
                '''
            }
        }
    }

}
