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
   agent { docker { image 'chrissayon/python3.7_alpine:0.1' } }
   // agent any

   stages {
      stage('Test') {
         steps {
            dir('backend') {
               sh "flake8"
               sh "pytest backend/tests"
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