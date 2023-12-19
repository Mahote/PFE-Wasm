FROM ubuntu

COPY . .

RUN apt-get update && apt-get install -y && apt-get install -y gcc wget build-essential \

&& g++ -c -pipe -O3 -fomit-frame-pointer -march=ivybridge   spectralnorm.c++ -o spectralnorm.c++.o && g++ spectralnorm.c++.o -o spectralnorm.gpp_run 

ENTRYPOINT ["./spectralnorm.gpp_run"]