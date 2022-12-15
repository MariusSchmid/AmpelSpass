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
                sh  ''' 
                        python -m pip install pycodestyle
                        pycodestyle --max-line-length=200 ./ > pep8.report || true
                        python -m pip install pylint
                        pylint --recursive=y --output-format=parseable  --rcfile=./devops/pylintrc ./ > pylint.report || true
                    '''
            }
            post {
                always{
                    recordIssues enabledForFailure: true, tools: [pep8(pattern: "pep8.report")], qualityGates: [[threshold: 1, type: 'TOTAL', unstable: true]]
                    recordIssues enabledForFailure: true, tools: [pyLint(pattern: "pylint.report")], qualityGates: [[threshold: 1, type: 'TOTAL', unstable: true]]
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