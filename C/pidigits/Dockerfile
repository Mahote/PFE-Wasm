FROM ubuntu

COPY . .

RUN apt-get update && apt-get install -y && apt-get install -y gcc wget build-essential && apt-get install -y libgmp3-dev \
&& gcc -pipe -Wall -O3 -fomit-frame-pointer -march=ivybridge pidigits.c -lgmp -o pidigits.gcc_run
ENTRYPOINT ["./pidigits.gcc_run"]