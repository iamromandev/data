```
docker build -t scrapify --target local --build-arg ENV=local --no-cache .
docker run --rm -it --name scrapify -p 80:80 scrapify

docker-compose -f docker-compose.yml build
docker-compose -f docker-compose.dev.yml build
```