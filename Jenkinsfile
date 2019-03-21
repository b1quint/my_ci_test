#!/usr/bin/env groovy
pipeline {

    agent any

    triggers {
        pollSCM('*/5 * * * 1-5')
    }

    options {
        skipDefaultCheckout(true)
        // Keep the 10 most recent builds
        buildDiscarder(logRotator(numToKeepStr: '10'))
        timestamps()
    }

    environment {
        PATH="$JENKINS_HOME/anaconda3/bin:$PATH"
    }

    stages {

        stage ("Code pull"){
            steps{
                checkout scm
            }
        }

        stage ("Download and Install Anaconda") {
            steps {
                sh '''
                    if [ ! "$(command -v conda)" ]; then
                        echo "Conda is not installed - Downloading and installing"

                        curl https://repo.anaconda.com/archive/Anaconda3-5.3.1-Linux-x86_64.sh \\
                            --output anaconda.sh --silent

                        chmod a+x anaconda.sh
                        ./anaconda.sh -u -b -p $JENKINS_HOME/anaconda3

                        conda config --add channels http://ssb.stsci.edu/astroconda
                        conda update --quiet conda
                    else
                        echo "Conda is already installed. Skipping fresh installation"
                    fi
                    '''
            }
        }

        stage ("Build Environment") {
            steps {
                sh  '''
                    if [ ! -d "${WORKSPACE}/venv" ]; then
                        conda create -p ./venv -y
                        fi

                    source activate ./venv
                    pip install --upgrade pip
                    pip install -U coverage pylint
                    pip install --force-reinstall pytest==3.10.1
                    pip install pydocstyle
                    '''
            }
        }

        stage('Test environment') {
            steps {
                sh  '''
                    source activate ./venv
                    which pip
                    which python
                    '''
            }
        }

        stage('Code quality with PyLint') {
            steps {
                sh  '''
                    source activate ./venv
                    if [ ! -d "reports" ]; then
                        mkdir reports
                        fi

                    pylint --exit-zero --rcfile=.pylintrc dummy_package > reports/pylint.log
                    '''
            }
            post {
                always {
                    echo 'Doing something after running PyLint'
                    recordIssues enabledForFailure: true, tool: pyLint(pattern: '**/reports/pylint.log')
                }
            }
        }

        stage('Checking docstrings') {
            steps {
                sh  '''
                    source activate ./venv
                    pydocstyle --add-ignore D400,D401,D205,D105,D105 dummy_package > 'reports/pydocstyle.log' || exit 0
                    '''
            }
            post {
                always {
                    echo 'Doing something after running PyLint'
                    recordIssues enabledForFailure: true, tool: pyDocStyle(pattern: '**/reports/pydocstyle.log')
                }
            }
        }

        stage('Unit tests and code coverage #1') {
            steps {
                sh  '''
                    source activate ./venv
                    which python
                    which pytest
                    coverage run -m pytest dummy_package/subpackage1 --junit-xml reports/TEST_1.xml
                    '''
                }
            post {
                always {
                    junit (allowEmptyResults: true,
                        testResults: 'reports/TEST_*.xml')
                }
            }
        }

        stage('Unit tests 2') {
            steps {
                sh  '''
                    source activate ./venv
                    coverage run -m pytest dummy_package/subpackage2 --junit-xml reports/TEST_2.xml
                    '''
            }
            post {
                always {
                    junit (allowEmptyResults: true,
                        testResults: 'reports/TEST_*.xml')
                }
            }
        }

        stage('Code coverage') {
            steps {
                sh  '''
                    source activate ./venv
                    coverage xml -o ./reports/coverage.xml
                    '''
            }
            post {
                always {
                    echo 'Report on code coverage'
                }
            }
        }
    }
    post {
        always {
            echo 'Finished pipeline'
        }
        failure {
            echo "Send e-mail, when failed"
        }
    }
}
