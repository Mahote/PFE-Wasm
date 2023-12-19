FROM ubuntu

COPY . .

RUN apt-get update && apt-get install -y && apt-get install -y gcc build-essential \
&& g++ -c -pipe -O3 -fomit-frame-pointer -march=ivybridge   binarytrees.c++ -o binarytrees.c++.o && g++ binarytrees.c++.o -o binarytrees.gpp_run

ENTRYPOINT ["./binarytrees.gpp_run"]