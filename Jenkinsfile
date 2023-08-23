pipeline {
    agent any
    
    environment {
        
        EC2_INSTANCE_IP = '52.3.250.81'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Deploy to EC2') {
            steps {
                script {
                    // Copy application files to EC2
                    sh "scp -i /home/dell/Downloads/react.pem -r ./home/dell/python ec2-user@${EC2_INSTANCE_IP}:/home/ec2-user

                    // SSH into EC2 and deploy the application
                    sh "ssh -i /home/dell/Downloads/react.pem ec2-user@${EC2_INSTANCE_IP} 'cd /home/ec2-user && git pull && pip install -r requirements.txt && systemctl restart your-app-service'"
                }
            }
        }
    }


