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
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Serve Flask App') {
            steps {
                sh 'nohup python $FLASK_APP &'
                sleep(time: 10, unit: "SECONDS") // Allow Flask time to start
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
