# Docker/k8s learning project
## Mini web applications that display a picture of a cat

## Docker commands:
1. docker build -t seidovsi/web:1.0.0 -t seidovsi/web:latest .  -- сборка docker image
2. docker run -ti --rm -p 8000:8000 --name web seidovsi/web:1.0.0  -- запуск контейнера из созданного image, то есть запуск web-приложения
3. docker push seidovsi/web:1.0.0 -- выгрузка image в Docker Hub
4. docker pull seidovsi/web:1.0.0 -- загрузка созданного image из Docker Hub

## Пример работы web-приложения 
![1](https://user-images.githubusercontent.com/105795798/173576358-4938663e-4c8a-44a4-9d76-d527a3d867db.png)

## Пример работы команды $ docker images

![2](https://user-images.githubusercontent.com/105795798/173576443-91b4c4e7-9f7e-49b5-a067-870cb5cabaa2.png)


## Пример работы команды $ docker pull seidovsi/web:1.0.0
![3](https://user-images.githubusercontent.com/105795798/173576493-1a8cfc0b-38a7-4a01-ba80-04d7f8a3ea94.png)

## Ссылка на docker Hub: https://hub.docker.com/u/seidovsi

## k8s commands:
1. minikube start --embed-certs  - Запуск кластера 
2. Создание Pod manifest - pod.yaml
3. $ kubectl apply -f pod.yaml -n default - Применение manifest
4. $ kubectl get pod web -n default --watch -проверка его установки

![4](https://user-images.githubusercontent.com/105795798/173576559-2d6f471f-d38a-4492-9b4f-efb65993842c.png)

6. $ kubectl port-forward pods/web 8000:8000  - выброс наружу web-приложения
7. curl http://127.0.0.1:8000/ -проверка web-приложения

![5](https://user-images.githubusercontent.com/105795798/173576667-5040e7b0-d777-4592-a6b7-d716ac6a9fe8.png)

8. $ kubectl logs web -n default -  логи внутри docker container Pod

![6](https://user-images.githubusercontent.com/105795798/173576753-19524c74-a284-4dd6-ba0f-f63920161d73.png)

#### Перейдем на http://127.0.0.1:8000/

![7](https://user-images.githubusercontent.com/105795798/173576793-1195f849-efe0-4660-baa0-1556b38fb16f.png)


