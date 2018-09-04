node {

    try {
        stage('Checkout') {
            sh "python ${env.WORKSPACE}/../${env.JOB_NAME}@script/Checkout.py"
        }
        stage('Build') {
            sh "python Build.py"
        }
        stage('Test') {
            sh "python Test.py"
        }
        stage('Deploy') {
            sh "python Test.py"
        }
    } catch (err) {
        currentBuild.result = 'FAILED'
        throw err
    }
}
