pipeline {

  agent none
  stages {
    stage('Run Tests') {  
      parallel {
        stage('Python 2.7') {
          agent any
          steps {
            sh '''
              python --version
            '''
          }
        }
        stage('Python 3.6') {
          agent any 
          steps {
            sh '''
              python --version
            '''
          }
        }
      }
    }
  }
}
  
           
