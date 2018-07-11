node {
    // Clean workspace before doing anything
    deleteDir()
    try {
        stage('Checkout') {
            echo "Checkout"
        }
        stage('Build') {
            echo "build"
        }
        stage('Tests') {
            echo "build"
        }
        stage('Deploy') {
            echo "build"
        }
    } catch (err) {
        currentBuild.result = 'FAILED'
        throw err
    }
}
