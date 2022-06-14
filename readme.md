# Docker/k8s learning project
## Mini web applications that display a picture of a cat

###Docker commands:
1. docker build -t seidovsi/web:1.0.0 -t seidovsi/web:latest .  -- сборка docker image
2. docker run -ti --rm -p 8000:8000 --name web seidovsi/web:1.0.0  -- запуск контейнера из созданного image, то есть запуск web-приложения
3. docker push seidovsi/web:1.0.0 -- выгрузка image в Docker Hub
4. docker pull seidovsi/web:1.0.0 -- загрузка созданного image из Docker Hub

####Пример работы web-приложения 
![](C:\Users\Said\Desktop\1.png)

####Пример работы команды $ docker images
![](C:\Users\Said\Desktop\2.png)

#### Пример работы команды $ docker pull seidovsi/web:1.0.0
![](C:\Users\Said\Desktop\3.png)

#### Ссылка на docker Hub: https://hub.docker.com/u/seidovsi

###k8s commands:
1. minikube start --embed-certs  - Запуск кластера 
2. Создание Pod manifest - pod.yaml
3. $ kubectl apply -f pod.yaml -n default - Применение manifest
4. $ kubectl get pod web -n default --watch -проверка его установки

![](C:\Users\Said\Desktop\4.png)
6. $ kubectl port-forward pods/web 8000:8000  - выброс наружу web-приложения
7. curl http://127.0.0.1:8000/ -проверка web-приложения

![](C:\Users\Said\Desktop\5.png)
9. $ kubectl logs web -n default -  логи внутри docker container Pod

![](C:\Users\Said\Desktop\6.png)

#### Перейдем на http://127.0.0.1:8000/

![](C:\Users\Said\Desktop\7.png)