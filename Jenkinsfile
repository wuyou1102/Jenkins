node {
    // Clean workspace before doing anything
        deleteDir()
        git url: 'ssh://jenkins@192.168.90.181:29418/9201_1'
        sh "git fetch origin ${GERRIT_REFSPEC}:${changeBranch}"
        sh "git checkout ${changeBranch}"
    try {
        stage('Checkout') {

        }
        stage('Build') {
            echo "build"
        }
        stage('Test') {
            echo "Test"
        }
        stage('Deploy') {
            echo "Deploy"
        }
    } catch (err) {
        currentBuild.result = 'FAILED'
        throw err
    }
}
