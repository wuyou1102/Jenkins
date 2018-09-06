node {

    try {
        stage('Checkout') {
            echo "python ${env.WORKSPACE}/../${env.JOB_NAME}@script/${env.JOB_NAME}/Checkout.py"
        }
        stage('Build') {
            sh "python ${env.WORKSPACE}/../${env.JOB_NAME}@script/${env.JOB_NAME}/Build.py"
        }
        stage('Test') {
            sh "python ${env.WORKSPACE}/../${env.JOB_NAME}@script/${env.JOB_NAME}/Test.py"
        }
        stage('Deploy') {
            sh "python ${env.WORKSPACE}/../${env.JOB_NAME}@script/${env.JOB_NAME}/Deploy.py"
        }
    } catch (err) {
        currentBuild.result = 'FAILED'
        throw err
    }
}
