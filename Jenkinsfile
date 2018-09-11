node {
    try {
        dir("${env.WORKSPACE}/../${env.JOB_NAME}@script/"){
            stage('Checkout') {
                echo "python Main.py Checkout"
            }
            stage('Build') {
                echo "python Main.py Build"
            }
            stage('Test') {
                sh "python Main.py Test"
            }
            stage('Deploy') {
                sh "python Main.py Deploy"
            }
        }
    } catch (err) {
        currentBuild.result = 'FAILED'
        throw err
    }
}
