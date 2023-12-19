FROM ubuntu

COPY . .

RUN apt-get update && apt-get install -y && apt-get install -y gcc build-essential \

&& g++ -c -pipe -O3 -fomit-frame-pointer -march=ivybridge   nbody.c++ -o nbody.c++.o && g++ nbody.c++.o -o nbody.gpp_run 
ENTRYPOINT ["./nbody.gpp_run"]