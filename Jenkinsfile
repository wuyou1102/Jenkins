pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                sh "python ${env.WORKSPACE}/../${env.JOB_NAME}@script/Checkout.py"
            }
        }
        stage('Build') {
            steps {
                sh "python ${env.WORKSPACE}/../${env.JOB_NAME}@script/Build.py"
            }
        }
        stage('Test') {
            steps {
                sh "python ${env.WORKSPACE}/../${env.JOB_NAME}@script/Test.py"
             }
        }
        stage('Deploy') {
            steps {
                sh "python ${env.WORKSPACE}/../${env.JOB_NAME}@script/Deploy.py"
            }
        }
    }
}