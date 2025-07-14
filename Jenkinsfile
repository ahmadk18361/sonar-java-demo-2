pipeline {
    agent any

    tools {
        maven 'Maven'
        jdk 'jdk-17'
    }

    environment {
        SONARQUBE_SERVER = 'Sonar-cve's' // Must match Jenkins config name exactly
    }

    stage('Checkout') {
          steps {
            checkout([$class: 'GitSCM',
              branches: [[name: '*/main']],
              userRemoteConfigs: [[url: 'https://github.com/ahmadk18361/sonar-java-demo-2.git']],
              extensions: [[$class: 'CloneOption', noTags: false, shallow: false, depth: 0]]
            ])
          }
        }

        
        stage('Remediate Vulnerabilities') {
            steps {
                bat 'remediation_cve_2019_0232.py src/main/java/com/example/TomcatCVE2019_0232Example.java'
                bat 'remediation_cve_2019_0232.py src/main/java/com/example/CmdInjectionBufferedReader.java'
                bat 'remediation_cve_2019_0232.py src/main/java/com/example/CmdInjectionArgsExample.java'                
            }
        }

        stage ('Debug Sonar Token') {
            steps {
                withCredentials([string(credentialsId: '2ndsonar', variable: 'SONAR_TOKEN')]) {
                    bat 'echo Debug: token is %SONAR_TOKEN%'
                }
            }
        }
        
        stage('SonarQube Scan') {
            steps {
                withSonarQubeEnv("${Sonar-cve-s}") {
                    withCredentials([string(credentialsId: '2ndsonar', variable: 'SONAR_TOKEN')]) {
                        bat 'mvn sonar:sonar -Dsonar.token=$SONAR_TOKEN'
                         bat 'echo Sonar token: %SONAR_TOKEN'
                       bat """
                       mvn clean verify sonar:sonar \
                          -Dsonar.projectKey=Sonar-cve-s \
                          -Dsonar.projectName='Sonar-cve's' \
                          -Dsonar.host.url=http://localhost:9000 \
                          sonar.sources=src/main/java/com/example
                          -Dsonar.token=sqp_b08b8163f360aa6cb24534b5c579de0a58f6211f

                            """
                    }
                }
            }
        }
    }
}
