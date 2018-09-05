pipeline {
    agent any
    stages {
        stage('Checkout') {
            sh "python ${env.WORKSPACE}/../${env.JOB_NAME}@script/Checkout.py"
        }
        stage('Build') {
            sh "python ${env.WORKSPACE}/../${env.JOB_NAME}@script/Build.py"
        }
        stage('Test') {
            sh "python ${env.WORKSPACE}/../${env.JOB_NAME}@script/Test.py"
        }
        stage('Deploy') {
            sh "python ${env.WORKSPACE}/../${env.JOB_NAME}@script/Deploy.py"
        }
    }
}