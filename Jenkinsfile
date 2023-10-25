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
        stage('parralel stage'){
            parrallel{
                stage('paralle1'){
                    steps{
                        echo "parallel 1"
                    }
                }
                stage('paralle2'){
                    steps{
                        echo "thiis parallel 2"
                    }
                }
                stage('2 more'){
                    stages{
                        stage('paralle3l'){
                            steps{
                                echo 'thhis is tehmohan'
                            }
                        }
                        stage('paralel4'){
                            steps{
                                echo 'this is the sus'
                            }
                        }
                    }
                }
            }
        }

      
   

    }
}