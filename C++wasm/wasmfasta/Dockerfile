FROM emscripten/emsdk AS builder

COPY . .

RUN apt-get update && apt-get install -y \
	&& emcc fasta.c++ -o fasta.wasm 
	
FROM scratch

COPY --from=builder /src/fasta.wasm /fasta.wasm
ENTRYPOINT ["./fasta.wasm"]