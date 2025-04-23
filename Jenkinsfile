pipeline {
    agent any

    environment {
        FLASK_APP = 'backend.py'
        REPORT_DIR = 'reports'
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/SouravGharge/grype-jenkins-pipeline.git', branch: 'main'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install -r requirements.txt'

            }
        }

        stage('Serve Flask App') {
            steps {
                sh '''
                    echo "Starting Flask app..."
                    nohup python3 backend.py > flask.log 2>&1
                    echo "Flask log output:"
                    cat flask.log
                    sh 'sleep 300' // keep the process running for 5 min
                '''
            }
        }


        stage('Archive Reports') {
            steps {
                archiveArtifacts artifacts: "${REPORT_DIR}/*.html", fingerprint: true
            }
        }
    }

    post {
        success {
            echo "✅ Reports served via Flask and archived successfully!"
        }
        failure {
            echo "❌ Something went wrong in the pipeline."
        }
    }
}
