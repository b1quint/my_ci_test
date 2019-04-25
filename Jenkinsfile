#!/usr/bin/env groovy
/*
 * Jenkins Pipeline for DRAGONS
 *
 * by Bruno C. Quint
 *
 * Required Plug-ins:
 * - Cobertura Plug-in
 */

pipeline {

    agent any

    triggers {
        pollSCM('H/20 * * * 1-5')
    }

    options {
        skipDefaultCheckout(true)
        buildDiscarder(logRotator(numToKeepStr: '20'))
        timestamps()
    }

    environment {
        PATH = "$JENKINS_HOME/anaconda3/bin:$PATH"
    }

    stages {
        stage('Checkout') {
            steps {
                echo "Checkout code"
            }
        }
        stage("Build") {
            parallel {
                stage("CentOS 6") {
                    steps {
                        echo "build on ${env.NODE_NAME}"
                    }
                }
                stage("CentOS 7") {
                    steps {
                        echo "build on ${env.NODE_NAME}"
                    }
                }
                stage("MacOs 10.10") {
                    steps {
                        echo "build on ${env.NODE_NAME}"
                    }
                }
                stage("MacOs 10.11") {
                    steps {
                        echo "build on ${env.NODE_NAME}"
                    }
                }
                stage("MacOs 10.12") {
                    steps {
                        echo "build on ${env.NODE_NAME}"
                    }
                }
                stage("MacOs 10.13") {
                    steps {
                        echo "build on ${env.NODE_NAME}"
                    }
                }
                stage("MacOs 10.14") {
                    steps {
                        echo "build on ${env.NODE_NAME}"
                    }
                }
            }
        }
        stage('Pre-Deploy') {
            parallel {
                stage("linux-64") {
                    steps {
                        echo "build on ${env.NODE_NAME}"
                    }
                }
                stage("osx-64") {
                    steps {
                        echo "build on ${env.NODE_NAME}"
                    }
                }
            }
        }
        stage('Test') {
            parallel {
                stage("linux-64") {
                    steps {
                        echo "pull build"
                        echo "install build"
                        echo "run tests"
                    }
                }
                stage("osx-64") {
                    steps {
                        echo "pull build"
                        echo "install build"
                        echo "run tests"
                    }
                }
                stage('static metrics') {
                    steps {
                        echo "run PyLint and PyDocStyle"
                    }
                }
            }
        }
        stage('Deploy') {
            parallel {
                stage('deploy linux-32') {
                    steps {
                        echo "deploy linux-32"
                    }
                }
                stage('deploy linux-64') {
                    steps {
                        echo "deploy linux-64"
                    }
                }
                stage('deploy noarch') {
                    steps {
                        echo "deploy noarch"
                    }
                }
                stage('deploy osx-64') {
                    steps {
                        echo "deploy osx-64"
                    }
                }
            }
        }
        stage('Report') {
            steps {
                echo "Report on something"
            }
        }
    }
    post {
        failure {
            echo "Send e-mail, when failed"
        }
    }
}
