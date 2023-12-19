FROM ubuntu

COPY . .

RUN apt-get update && apt-get install -y && apt-get install -y gcc build-essential \
&& g++ -c -pipe -O3 -fomit-frame-pointer -march=ivybridge   fasta.c++ -o fasta.c++.o && g++ fasta.c++.o -o fasta.gpp_run

ENTRYPOINT ["./fasta.gpp_run"]