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
                sh 'zip -r  catalogue.zip ./* --exclude=.git --exclude=.js'
        }
       }
       stage('nexus-artifact uploader'){
        steps{
            nexusArtifactUploader(
                nexusVersion: 'catalogue3',
                protocol: 'http',
                nexusUrl: '18.208.175.25:8081/',
                groupId: 'chiru.com',
                version: '11.1.0',
                repository: 'catalogue',
                credentialsId: 'nexus-auth',
                artifacts:[
                    [
                        artifactId: 'catalogue',
                        classifier: '',
                        file: 'catalogue.zip',
                        type: 'zip'
                    ]
                ]


            )
        }
       }
    }
    post{
        always{
            deleteDir()
        }
    }

}