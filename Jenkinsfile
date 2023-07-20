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
          // sh 'python3 custom_data_transform_from_tsv.py'
          sh 'python3 custom_data_transform.py'
        }
      }
    }
  }
}