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
       stage('zipping stage'){
             steps{
                echo 'building the package'
                sh 'zip -r ./* --exclude=.git --exclude=.js'
        }
       }
    }
    post{
        always{
            deleteDir()
        }
    }

}