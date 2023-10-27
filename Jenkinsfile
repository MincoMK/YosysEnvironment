pipeline {
    agent { dockerfile true}
    stages {
        stage("YoSys") {
            steps {
                sh "python3 synthgen.py"
            }
        }
        stage("Image Process") {
            steps {
                sh "python3 imageprocess.py"
            }
        }
        stage("Send") {
            steps {
                sh "python3 webhook.py"
            }
        }
    }
}