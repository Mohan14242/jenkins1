pipeline{
    agent any 
    environment{
        USER='mohan'
    }
   
    triggers{
        cron('* * * * *')
    }
    parameters{
        string(name:'person',defaultValue:'mohan',description:'please enter your name')
        choice(name:"environment",choices:["dev","test","prod"],description:'please select your environemnt')
    }
    stages{
        stage('terraform init'){
            steps{
                echo "$USER is best one and the person who is executed id $params.person"
                
            }
        }
        stage('prod'){
            when{
                branch "master"
            }
            steps{
                echo "deploying the productions"
            }
        }

      
   

    }
}