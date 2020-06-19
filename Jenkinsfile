pipeline {
   agent any

   stages {
      stage('Hello') {
         steps {
            echo 'Hello World'
         }
      }
      
      stage('Set git build status') {
         steps {
            step([$class: 'GitHubCommitStatusSetter'])
         }
      }
   }
}