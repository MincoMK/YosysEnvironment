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
                netlistsvg net.json
            }
        }
        stage("ImageMagick") {
            convert -background white -alpha remove -alpha off net.svg net.png
        }
    }
}