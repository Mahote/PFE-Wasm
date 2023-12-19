FROM ubuntu

COPY . .

RUN apt-get update && apt-get install -y && apt-get install -y gcc wget build-essential && apt-get install -y libgmp3-dev \ 

&& g++ -c -pipe -O3 -fomit-frame-pointer -march=ivybridge  -std=c++14 -g pidigits.c++ -lgmp -o pidigits.c++.o && g++ pidigits.c++.o -lgmp -o pidigits.gpp_run 

ENTRYPOINT ["./pidigits.gpp_run"]