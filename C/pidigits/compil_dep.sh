#!/bin/bash
apt-get install -y lzip
wget https://gmplib.org/download/gmp/gmp-6.2.1.tar.lz
tar xf gmp-6.2.1.tar.lz
cd gmp-6.2.1
./configure
make
make install
cd ..
rm gmp-6.2.1.tar.lz

wget https://www.mpfr.org/mpfr-current/mpfr-4.2.0.tar.xz
tar xf mpfr-4.0.2.tar.xz
cd mpfr-4.2.0
./configure
make
make install
cd ..
rm mpfr-4.2.0.tar.xz

wget https://ftp.gnu.org/gnu/mpc/mpc-1.3.1.tar.gz
tar xf mpc-1.3.1.tar.gz
cd mpc-1.3.1
./configure
make
make install
cd ..
rm mpc-1.3.1.tar.gz

