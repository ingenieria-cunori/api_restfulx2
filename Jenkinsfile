pipeline {
    agent any

    environment {        
        SSH_KEY_ID = 'ssh-student-dell-server'        
        ENV_FILE_ID = 'api-restx-env-prod'
        COMPOSE_FILE_ID = 'api-restx-docker-compose-prod'
        SERVER_IP='dell-server-ip'
        PROJECT_NAME = 'api_restx'
    }

    stages {
        stage('1. Pre-Check & Pull') {
            steps {
                echo "Iniciando despliegue de ${env.PROJECT_NAME}..."                
            }
        }

        stage('2. Unit Tests') {
            agent {                
                docker { 
                    image 'python:3.13.11-alpine' 
                }
            }
            steps {
                sh '''
                    # 1. Definiendo ruta de trabajo
                    export HOME=/tmp
                    export PATH=$PATH:/tmp/.local/bin

                    # 2. Instalación de pequetes
                    pip install --no-cache-dir --user -r requirements.txt

                    # 3. Verificación e inicio de los tests
                    echo "Paquetes instalados. Iniciando pruebas..."
                    python3 -m pytest tests/ && exit 0
                '''
            }
        }

        stage('3. Deploy to Production') {
            steps {                
                withCredentials([
                    file(credentialsId: env.ENV_FILE_ID, variable: 'ENV_FILE'),
                    file(credentialsId: env.COMPOSE_FILE_ID, variable: 'COMPOSE_FILE'),
                    string(credentialsId: env.SERVER_IP, variable: 'TARGET_IP')
                ]) {
                                    
                ansiblePlaybook(
                    playbook: 'ci/playbook.yml',
                    inventory: 'ci/inventory.ini',
                    credentialsId: env.SSH_KEY_ID,                    
                    extraVars: [
                        env_file: "${ENV_FILE}",
                        repo_dir: "${WORKSPACE}",
                        compose_file: "${COMPOSE_FILE}",
                        ansible_host: "${TARGET_IP}"
                    ],
                    colorized: true
                    )
                }
            }
        }
    }

    post {
        success {
            echo "¡Despliegue exitoso!"
        }
        failure {
            echo "xxxxx El Pipeline falló. xxxxx"
        }
    }
}