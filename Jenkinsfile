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
        stage('Stage 0') {
            steps {
                echo "Checkout code"
            }
        }
        stage("Stage 1") {
            parallel {
                stage("Parallel Stage 1.1") {
                    steps {
                        echo "Step 1.1.1"
                        echo "Step 1.1.2"
                    }
                }
                stage("Parallel Stage 1.2") {
                    steps {
                        echo "Step 1.2.1"
                        echo "Step 1.2.2"
                    }
                }
                stage("Parallel Stage 1.3") {
                    steps {
                        echo "Step 1.3.1"
                        echo "Step 1.3.2"
                        echo "Step 1.3.3"
                    }
                }
            }
        }
        stage('Stage 2') {
            parallel {
                stage("Parallel Stage 2.1") {
                    steps {
                        echo "Step 2.1.1"
                        echo "Step 2.1.2"
                        echo "Step 2.1.3"
                    }
                }
                stage("Parallel Stage 2.2") {
                    steps {
                        echo "Step 2.2.1"
                        echo "Step 2.2.2"
                        echo "Step 2.2.3"
                        echo "Step 2.2.4"
                    }
                }
            }
        }
        stage('Stage 3') {
            steps {
                echo "Step 3.1"
                echo "Step 3.2"
                echo "Step 3.3"
            }
        }
    }
    post {
        failure {
            echo "Send e-mail, when failed"
        }
    }
}
