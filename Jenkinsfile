node {

    try {
        stage('Checkout') {
            sh "Checkout.py"
        }
        stage('Build') {
            sh "Build.py"
        }
        stage('Test') {
            sh "Test.py"
        }
        stage('Deploy') {
            sh "Test.py"
        }
    } catch (err) {
        currentBuild.result = 'FAILED'
        throw err
    }
}
