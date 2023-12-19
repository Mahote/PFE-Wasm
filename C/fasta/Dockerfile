FROM ubuntu 
COPY . .

RUN apt-get update && apt-get install -y && apt-get install -y gcc build-essential \
&& gcc -pipe -Wall -O3 -fomit-frame-pointer -march=ivybridge  fasta.c -o fasta.gcc_run
ENTRYPOINT ["./fasta.gcc_run"]