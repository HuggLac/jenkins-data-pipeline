pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                script {
                    // Choisissez la commande en fonction de votre script
                    sh 'pip install pandas' // Installer les dépendances
                    sh 'python data_analysis.py' // Exécuter le script Python
                }
            }
        }
    }
}
pipeline {
    agent any
    environment {
        PYTHON_HOME = '/usr/bin'
        PATH = "${env.PATH};${PYTHON_HOME}"
    }
  
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/HuggLac/jenkins-data-pipeline.git'
            }
        }
        stage('Build') {
            steps {
                script {
					sh 'echo "Running on Linux"'
					sh 'pip install pandas' // Installer les dépendances
					sh 'python3 --version'
					sh 'python3 hello.py'					
                }
            }
        }
    }
}