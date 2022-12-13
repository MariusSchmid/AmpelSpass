pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Check Code Style') {
            agent {
                docker {
                    image "python:3.7"
                    args '--user 0:0 -v ${PWD}:/mydata -w /mydata'
                }
            }
            steps {
                echo "Pep8 style check"
                sh 'ls'
                sh  ''' 
                        python -m pip install pycodestyle
                        pycodestyle examples > pep8.report
                    '''
            }
            post {
                always{
                    recordIssues enabledForFailure: true, tools: [pep8()]
                }

            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}