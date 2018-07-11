
node {
    // Clean workspace before doing anything
    deleteDir()

    try {
        stage('Clone') {
            sh "pwd"
            sh "ls"
            def Learn =load 'Learn.groovy'
            Learn.Groovy()
        }
        stage('Build') {
            sh "echo 'building ${config.projectName} ...'"
        }
        stage('Tests') {
            parallel 'static': {
                sh "echo 'shell scripts to run static tests...'"
            },
                    'unit': {
                        sh "echo 'shell scripts to run unit tests...'"
                    },
                    'integration': {
                        sh "echo 'shell scripts to run integration tests...'"
                    }
        }
        stage('Deploy') {
            sh "echo 'deploying to server ${config.serverDomain}...'"
            sh "echo Itai ganot"
            sh "echo Itai"
        }
    } catch (err) {
        currentBuild.result = 'FAILED'
        throw err
    }
}
