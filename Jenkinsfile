pipeline{
    agent { node { label 'mohan'}}
    stages{
        stage('install the dependencies'){
            steps{
                echo 'hello this is mohan'
               sh 'sudo yum install -y nodejs'

                sh 'sudo npm install'
            }
        }
        stage('sonar-scanner'){
            steps{
                
                sh 'sonar-scanner'
            }
        }
        
    }

}