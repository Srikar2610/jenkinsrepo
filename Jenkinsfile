pipeline {
    agent any
    stages {
        stage('Install Python and Dependencies') {
            steps {
                sh 'python3 --version'  // Check Python version
                sh 'pip install -r requirements.txt || true'  // Install dependencies if requirements.txt exists
            }
        }
        stage('Run Python Script') {
            steps {
                sh 'python3 app.py'
            }
        }
        stage('Archive Output') {
            steps {
                archiveArtifacts artifacts: 'output.txt', fingerprint: true
            }
        }
    }
}
