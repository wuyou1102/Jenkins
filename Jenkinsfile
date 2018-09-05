node {

    try {

        env.TIME=${it.timestampString}
        env.TIMESTAMP=''
        env.COMPILER_FOLDER = '/home/bspserver/sda/G4_SourceCode/'
        env.DEPLOY_FOLDER = '/home/bspserver/sda/G4_DailyBuild/'
        stage('Checkout') {
            sh "python ${env.WORKSPACE}/../${env.JOB_NAME}@script/Checkout.py"
        }
        stage('Build') {
            sh "python ${env.WORKSPACE}/../${env.JOB_NAME}@script/Build.py"
        }
        stage('Test') {
            sh "python ${env.WORKSPACE}/../${env.JOB_NAME}@script/Test.py"
        }
        stage('Deploy') {
            sh "python ${env.WORKSPACE}/../${env.JOB_NAME}@script/Deploy.py"
        }
    } catch (err) {
        currentBuild.result = 'FAILED'
        throw err
    }
}
