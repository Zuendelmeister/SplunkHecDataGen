REM for url: https://127.0.0.1:8088/services/collector
REM for token: 9f830b6f-94cd-4b5a-8d60-d69c9f953605

docker stop splunk-hec-datagen
docker rm splunk-hec-datagen
docker rmi splunk-hec-datagen
docker build -t "splunk-hec-datagen:latest" .
docker run --name splunk-hec-datagen --network host -e URL=<url> -e TOKEN=<token> splunk-hec-datagen
docker logs -f splunk-hec-datagen
