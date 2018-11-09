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
    PATH="~/miniconda3/bin:$PATH"
  }
  
  stages {
    stage ("Code pull"){
      steps{
        checkout scm
      }
    }
    stage ("Build Environment") {
      steps {
        sh '''conda create --yes -n ${BUILD_TAG} python
              source activate ${BUILD_TAG} 
              conda install coverage
        '''
      }
    }
    stage('Test environment') {
      steps {
        sh '''source activate ${BUILD_TAG} 
              pip list
              which pip
              which python
              '''
      }
    }
    stage('Static code metrics') {
      steps {
        echo "Raw metrics"
        sh  ''' source activate ${BUILD_TAG}
                radon raw --json irisvmpy/ > raw_report.json
                radon cc --json irisvmpy/ > cc_report.json
                radon mi --json irisvmpy/ > mi_report.json
                '''
        //TODO: add conversion and HTML publisher step  
      }
    }
    stage('Coverage metrics') {
      steps {
        echo "Code Coverage"
        sh  ''' source activate ${BUILD_TAG}
                coverage run rtd_test/greet_people.py
                python -m coverage xml -o ./reports/coverage.xml
                '''
      }
      post{
        always{
          step([$class: 'CoberturaPublisher',
              autoUpdateHealth: false,
              autoUpdateStability: false,
              coberturaReportFile: 'reports/coverage.xml',
              failNoReports: false,
              failUnhealthy: false,
              failUnstable: false,
              maxNumberOfBuilds: 10,
              onlyStable: false,
              sourceEncoding: 'ASCII',
              zoomCoverageChart: false])                    
        }
      }
    }  
  }
  post {
    always {
      sh 'conda remove --yes -n ${BUILD_TAG} --all'
    }
    failure {
      echo "Send e-mail, when failed"
    }
  }
}
