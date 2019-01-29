node("nvidia_server"){
    checkout scm

    stage("Build"){
        sh 'docker build -t grimsleepless/monitoring_client-test -f Dockerfile.test . --pull'
    }

    stage("Test"){
        sh 'docker run --runtime=nvidia -v /etc/os-release:/etc/os-release grimsleepless/monitoring_client-test'
    }
}
