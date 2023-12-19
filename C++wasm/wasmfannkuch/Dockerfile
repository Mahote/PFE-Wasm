FROM emscripten/emsdk AS builder

COPY . .

RUN apt-get update && apt-get install -y \
	&& emcc fannkuch-redux.c++ -o fannkuch.wasm 
	
FROM scratch
COPY --from=builder /src/fannkuch.wasm /fannkuch.wasm
ENTRYPOINT ["./fannkuch.wasm"]