pipeline {
    agent any
    
    environment {
        
        EC2_INSTANCE_IP = 'your-ec2-instance-ip'
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
                    sh "scp -i /path/to/ssh/key.pem -r ./your-python-app ec2-user@${EC2_INSTANCE_IP}:/path/to/destination"

                    // SSH into EC2 and deploy the application
                    sh "ssh -i /path/to/ssh/key.pem ec2-user@${EC2_INSTANCE_IP} 'cd /path/to/destination && git pull && pip install -r requirements.txt && systemctl restart your-app-service'"
                }
            }
        }
    }


