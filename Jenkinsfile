pipeline {
    agent {
        dockerfile = true
    }
    stages {
        stage("YoSys") {
            steps {
                python3 synthgen.py
            }
        }
        stage("SVGify") {
            steps {
                netlistsvg net.json -o net.svg
            }
        }
        stage("ImageMagick") {
            steps {
                convert -background white -alpha remove -alpha off net.svg net.png
            }
        }
        stage("Send") {
            steps {
                python3 webhook.py
            }
        }
    }
}