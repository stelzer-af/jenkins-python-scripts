pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python3 --version'
      }
    }
    stage('hello') {
      steps {
        script {
          // Install boto3
          sh 'pip3 install boto3'

          // Run the Python script
          sh 'python3 hello.py'
        }
      }
    }
  }
}