FROM ubuntu

COPY . .

RUN apt-get update && apt-get install -y && apt-get install -y gcc build-essential \
&& gcc -pipe -Wall -O3 -fomit-frame-pointer -march=ivybridge -fopenmp spectral-norm.c -o spectralnorm.gcc_run -lm
ENTRYPOINT ["./spectralnorm.gcc_run"]