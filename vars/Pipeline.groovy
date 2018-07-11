import com.wuyou.Learn
node {
    stage('Checkout') {
        echo "Checkout"
    }

    stage('Build') {
        echo "Build"
        Learn.Groovy()
    }

    stage('Test') {
        echo "Test"
    }

    stage('Deploy') {
        echo "Deploy ......"
    }
}