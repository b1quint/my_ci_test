pipeline {
   
    agent any
    environment {
      PACKAGE_NAME = 'dragons'
      CONDA_HOME = 'miniconda'
      PYENV_HOME = '.pyenv'
    }
    stages {
        stage('Build') {
            steps {
                sh 'echo $PATH'
                sh 'echo "Hello World"'
                sh '''
                    echo "Multiline shell steps works too"
                    ls -lah
                    echo $WORKSPACE/$CONDA_HOME
                '''
            }
        }
    }

}
