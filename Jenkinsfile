pipeline {
    agent { dockerfile true}
    stages {
        stage("YoSys") {
            steps {
                sh "python3 synthgen.py"
                sh "yosys synth.ys"
            }
        }
        stage("SVGify") {
            steps {
                sh "netlistsvg net.json -o net.svg"
            }
        }
        stage("ImageMagick") {
            steps {
                sh "convert -background white -alpha remove -alpha off net.svg net.png"
            }
        }
        stage("Send") {
            steps {
                sh "python3 webhook.py"
            }
        }
    }
}