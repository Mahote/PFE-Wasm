FROM ubuntu

COPY . .

RUN apt-get update && apt-get install -y && apt-get install -y gcc build-essential \
&& gcc -pipe -Wall -O3 -fomit-frame-pointer -march=ivybridge  fannkuch-redux.c -o fannkuchredux.gcc_run
ENTRYPOINT ["./fannkuchredux.gcc_run"]