FROM adoptopenjdk/openjdk8

RUN apt update && apt install -y maven

COPY ./java-hiverunner /hiverunner/

RUN cd /hiverunner && mvn install

CMD java -classpath /hiverunner/target/hiverunner-1.0-SNAPSHOT.jar HiveRunnerEntryPoint
