#!/usr/bin/env groovy
pipeline {

  agent none
  stages {
    
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
    
  post {
    always {
      echo 'This will always run'
    }
    success {
      echo 'This will run only if successful'
    }
    failure {
      echo 'This will run only if failed'
    }
    unstable {
      echo 'This will run only if the run was marked as unstable'
    }
    changed {
      echo 'This will run only if the state of the Pipeline has changed'
      echo 'For example, if the Pipeline was previously failing but is now successful'
    }
  }
}
