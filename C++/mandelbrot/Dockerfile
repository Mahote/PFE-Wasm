FROM ubuntu

COPY . .

RUN apt-get update && apt-get install -y && apt-get install -y gcc build-essential \
&& g++ -c -pipe -O3 -fomit-frame-pointer -march=ivybridge   mandelbrot.c++ -o mandelbrot.c++.o && g++ mandelbrot.c++.o -o mandelbrot.gpp_run

ENTRYPOINT ["./mandelbrot.gpp_run"]