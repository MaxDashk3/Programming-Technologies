pipeline {
    options {timestamps()}
    agent none
    environment{
        DOCKER_CREDS = credentials('docker_hub')
    }
    stages{
        stage ('Check scm'){
            agent any
            steps {
                checkout scm
            }
        }
        stage ('Build') {
            steps {
                echo "Building ... ${BUILD_NUMBER}"
                echo "Build completed"
            }
        }
        stage ('Test') {
            agent { docker { image 'alpine' 
                            args '-u=\"root\"'}
                    }
            steps {
                sh 'apk add --update python3 py-pip'
                sh 'python3 -m venv /venv'
                sh 'source /venv/bin/activate && pip install unittest-xml-reporting'
                sh 'source /venv/bin/activate && python3 Tests.py'
            }
            post {
                always {
                    junit 'test-reports/*.xml'
                }
                success {
                    echo "Testing successful"
                }
                failure {
                    echo "Tests failed"
                }
            }
        }
        stage('Publish image') {
            agent any
            steps{
                sh 'echo $DOCKER_CREDS_PSW | docker login --username $DOCKER_CREDS_USR --password-stdin'
                sh 'docker build -t maxdashk3/news_queue:latest --push .'
            }
            post {
                always {
                    sh 'docker logout'
                }
            }
        }
    }
}