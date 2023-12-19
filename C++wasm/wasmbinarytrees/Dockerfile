FROM emscripten/emsdk AS builder

COPY . .


RUN apt-get update && apt-get install -y \
	&& emcc binarytrees.c++ -o binarytrees.wasm 
	
FROM scratch
COPY --from=builder /src/binarytrees.wasm /binarytrees.wasm
ENTRYPOINT ["./binarytrees.wasm"]