FROM ubuntu 
COPY . .

RUN apt-get update && apt-get install -y && apt-get install -y gcc build-essential \
&& gcc -pipe -Wall -O3 -fomit-frame-pointer -march=ivybridge  binarytrees.c -o binarytrees.gcc_run -lm
ENTRYPOINT ["./binarytrees.gcc_run"]