FROM ubuntu

COPY . .

RUN apt-get update && apt-get install -y && apt-get install -y gcc build-essential \
&& gcc -pipe -Wall -O3 -fomit-frame-pointer -march=ivybridge  nbody.c -o nbody.gcc_run -lm
ENTRYPOINT ["./nbody.gcc_run"]