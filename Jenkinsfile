pipeline {
	agent any
	triggers {
        pollSCM('* * * * *') //runs this pipeline on every commit
        cron('30 23 * * *') //run at 23:30:00 
    }
	stages {
		stage("Compile") {
			steps {
				//pip install requirements.txt
				echo "Python compile done"
			}
		}
		stage("Unit test") {
			steps {
				sh "python myapptest.py"
			}
		}
	}
}
