pipeline{
    agent any 
    options {
        timeout(time:1 ,unit:'MINUTES')
    }
    stages{
        stage('terraform init'){
            steps{
                sh ''' 
                    terraform init'''
            }
        }
        stage('terraform plan'){
            steps{
                sh '''
                terraform plan'''
            }
        }
        stage('pemission neede'){
            steps{
                input "do you want to proceed"
            }
        }



    }
}