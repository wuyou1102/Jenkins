node {
    // Clean workspace before doing anything
    deleteDir()
    git url: 'http://192.168.90.181:8090/#/admin/projects/9201_1'

    // Fetch the changeset to a local branch using the build parameters provided to the
    // build by the Gerrit plugin...
    def changeBranch = "change-${GERRIT_CHANGE_NUMBER}-${GERRIT_PATCHSET_NUMBER}"
    sh "git fetch origin ${GERRIT_REFSPEC}:${changeBranch}"
    sh "git checkout ${changeBranch}"
    try {
        stage('Checkout') {

            echo "Checkout"
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
