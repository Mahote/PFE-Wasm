FROM ubuntu

COPY . .

RUN apt-get update && apt-get install -y && apt-get install -y gcc build-essential \
&& g++ -c -pipe -O3 -fomit-frame-pointer -march=ivybridge  -std=c++11 -pthread fannkuch-redux.c++ -o fannkuchredux.c++.o && g++ fannkuchredux.c++.o -o fannkuch.gpp_run -lpthread 
ENTRYPOINT ["./fannkuch.gpp_run"]