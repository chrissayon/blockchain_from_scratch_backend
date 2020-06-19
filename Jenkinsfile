void setBuildStatus(String message, String state) {
  step([
      $class: "GitHubCommitStatusSetter",
      reposSource: [$class: "ManuallyEnteredRepositorySource", url: "https://github.com/chrissayon/blockchain_from_scratch_backend"],
      contextSource: [$class: "ManuallyEnteredCommitContextSource", context: "ci/jenkins/build-status"],
      errorHandlers: [[$class: "ChangingBuildStatusErrorHandler", result: "UNSTABLE"]],
      statusResultSource: [ $class: "ConditionalStatusResultSource", results: [[$class: "AnyBuildResult", message: message, state: state]] ]
  ]);
}

pipeline {
   agent { docker { image 'python:3.7.2' } }
   // agent any

   stages {
      stage('Test') {
         steps {
            sh 'pip install --user -r requirements.txt'
            dir('frontend') {
               sh "flake8"
            }
         }
      }  
   }
   post {
      success {
         setBuildStatus("Build succeeded", "SUCCESS");
      }
      failure {
         setBuildStatus("Build failed", "FAILURE");
      }
   }
}