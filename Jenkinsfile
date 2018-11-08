pipeline {

  agent none
  stages {
    stage('Run Tests') {  
      parallel {
        
        stage('Python 2.7') {
          agent any
          environment {
            PYTHON_VERSION=2.7
          }
          stages {
            stage('build') {
              steps {
                sh 'echo "Building in python $PYTHON_VERSION"'
              }                
            }
            stage('test') {
              steps {
                sh 'echo "Testing with python $PYTHON_VERSION"'
              }  
            }
            stage('deploy') {
              steps {
                sh 'echo "Deploy python $PYTHON_VERSION"'
              }  
            }
          }
        } 
        
        stage('Python 3.6') {
          agent any
          environment {
            PYTHON_VERSION=3.6
          }
          stages {
            stage('build') {
              steps {
                sh 'echo "Building in python $PYTHON_VERSION"'
              }                
            }
            stage('test') {
              steps {
                sh 'echo "Testing with python $PYTHON_VERSION"'
              }  
            }
            stage('deploy') {
              steps {
                sh 'echo "Deploy python $PYTHON_VERSION"'
              }  
            }
          }
        }
      }
    }
  }
}
  
           
