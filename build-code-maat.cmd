https://github.com/adamtornhill/code-maat.git
docker build -t maat . 
docker create --name maat 
docker cp maat:/usr/src/code-maat/app-standalone.jar ./