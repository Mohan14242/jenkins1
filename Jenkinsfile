pipeline{
    agent any 
    environment{
        USER='mohan'
    }
    options {
        timeout(time:1 ,unit:'MINUTES')
    }
    stages{
        stage('terraform init'){
            steps{
                echo "$USER is best one"
                
            }
        }
   

    }
}