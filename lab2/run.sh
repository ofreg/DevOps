

docker build -t news-site:single -f Dockerfile .
docker run -d -p 8000:8000 --name news-single news-site:single


docker build -t news-site:multi -f Dockerfile.multistage .
docker run -d -p 8001:8000 --name news-multi news-site:multi


docker images | grep news-site
