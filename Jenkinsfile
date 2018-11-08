pipeline {

  agent any
  environment {
    PACKAGE_NAME = 'dragons'
    CONDA_HOME = 'miniconda'
    PYENV_HOME = '.pyenv'
  }
  
  stages {

    stage('Check variables') {
      steps {
        sh 'echo $PACKAGE_NAME'
        sh 'echo $CONDA_HOME'
        sh 'echo $PYENV_HOME'
      }
    }
    
    stage('Define new variable') {
      steps {
        sh '''
          NEW_ENV="my new env"
          echo $NEW_ENV
          '''
        sh 'echo $NEW_ENV'
      }
    }
    
    stage('Check variable persistensy') {
      steps {
        sh 'echo $NEW_ENV'
        }
    }  
  }
}
