# Web Stack Debugging
For this project, we were given a Docker image and the command to run it:
docker run -p 8080:80 -d -it holbertonschool/265-0
-p 8080:80 means whatever service running on my container on 80 will be available on my host on 8080.
At this point, when executing curl 0:8080 on the command line would return an error.
We were tasked with finding the command to run on the instance to fix that.
