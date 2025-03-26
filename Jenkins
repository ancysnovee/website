pipeline{
    agent any
    stages{
        stage("adding"){
            steps{
                url:"https://github.com/ancysnovee/website.git" , branch:main
            }
        }
        stage("dependency") {
            steps{
                bat '''
                    python -m venv venv
                    call venv\\Scripts\\activate
                    pip install --upgrade pip
                    pip install pytest
                '''
            }
        }
        stage ("testing){
            steps{
                bat '''
                    call venv\\Scripts\\activate
                    pytest test.py
                '''

            }
            
        }
        stage ("deploy"){
            steps{
                bat '''
                    call venv\\Scripts\\activate
                    python course.py
                '''
            }
        }

    }
}