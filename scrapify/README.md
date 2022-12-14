```
docker build --no-cache --target local --build-arg ENV=local -t scrapify .
docker run --rm -it --name scrapify -p 80:80 scrapify
```