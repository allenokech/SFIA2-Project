pipeline{
    agent any
    environment{
        DATABASE_URI = credentials("DATABASE_URI")
    }
        stage("Build and Push"){
            steps{
                // install docker and docker-compose
                // add jenkins to docker group
                // sudo su - jenkins, docker login
                // docker-compose build and push
                sh "docker rmi -f \$(docker images -qa) || true"
                sh "docker-compose build && docker-compose push"
            }
        }
    }