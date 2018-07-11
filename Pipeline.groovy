node {
    // Clean workspace before doing anything
    deleteDir()

    try {
        stage('Checkout') {
            echo "Checkout"
            checkout changelog: false, poll: false, scm: [$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'a22ba1a8-6275-4fdf-baf9-018211d45248', url: 'ssh://jenkins@192.168.90.181:29418/9201_1']]]

            // Fetch the changeset to a local branch using the build parameters provided to the
            // build by the Gerrit plugin...
            def changeBranch = "change-${GERRIT_CHANGE_NUMBER}-${GERRIT_PATCHSET_NUMBER}"
            sh "git fetch origin ${GERRIT_REFSPEC}:${changeBranch}"
            sh "git checkout ${changeBranch}"
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
