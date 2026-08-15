pipeline {
    agent any

    environment {
        AWS_REGION = 'us-east-2'
        APP_NAME   = 'quickbite'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Terraform Validate') {
            steps {
                sh '''
                    cd terraform
                    terraform fmt -check
                    terraform init -backend=false
                    terraform validate
                '''
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t ${APP_NAME}:${BUILD_NUMBER} ./app'
            }
        }

        stage('Trivy Scan') {
            steps {
                sh 'trivy image --exit-code 0 --severity HIGH,CRITICAL ${APP_NAME}:${BUILD_NUMBER}'
            }
        }

        stage('Terraform Plan') {
            steps {
                sh '''
                    cd terraform
                    terraform init -backend=false
                    terraform plan
                '''
            }
        }
    }

    post {
        always {
            echo 'QuickBite CI pipeline completed.'
        }
    }
}
