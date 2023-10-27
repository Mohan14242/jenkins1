pipeline{
    agent any
    stages{
        stage('install the dependencies'){
            steps{
                echo 'hello this is mohan'
               sh 'sudo yum install -y nodejs'

                sh 'sudo npm install'
            }
        }
        stage('getting the version'){
            steps{
                script[
                    def pversion= readJSON(file: 'package.json')
                    packageversion=pversion.version
                    echo "the version is $packageversion"
                ]
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
                nexusUrl: '18.208.175.25:8081/repository/catalogue/',
                groupId: 'chiru.com',
                version: '11.1.2',
                repository: 'catalogue',
                credentialsId: 'nexus-auth',
                artifacts:[
                    [
                        artifactId: 'catalogue',
                        classifier: '',
                        file: 'catalogue.zip',
                        type: 'zip12211211ww'
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