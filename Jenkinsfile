pipeline{
    agent any 
    environment{
        USER='mohan'
    }
    options {
        timeout(time:1 ,unit:'MINUTES')
    }
    parameters{
        string(name:'person',defaultValue:'mohan',description:'please enter your name')
    }
    stages{
        stage('terraform init'){
            steps{
                echo "$USER is best one and the person who is executed id $params.person"
                
            }
        }
      
   

    }
}