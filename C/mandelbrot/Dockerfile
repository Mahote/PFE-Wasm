FROM ubuntu

COPY . .

RUN apt-get update && apt-get install -y && apt-get install -y gcc build-essential \
&& gcc -pipe -Wall -O3 -fomit-frame-pointer -march=ivybridge  mandelbrot.c -o mandelbrot.gcc_run
ENTRYPOINT ["./mandelbrot.gcc_run"]