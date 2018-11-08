pipeline {
   
    agent any
    environment {
      PACKAGE_NAME = 'dragons'
      CONDA_HOME = '$WORKSPACE/miniconda'
      PYENV_HOME = '$WORKSPACE/.pyenv'
    }
    stages {
        stage('Build') {
            steps {
                sh 'echo $PATH'
                sh 'echo "Hello World"'
                sh '''
                    echo "Multiline shell steps works too"
                    ls -lah
                    echo $CONDA_HOME
                '''
            }
        }
    }

}
