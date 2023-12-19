FROM emscripten/emsdk AS builder

COPY . .

RUN apt-get update && apt-get install -y \ 
	&& emcc spectralnorm.c++ -o spectralnorm.wasm

FROM scratch
COPY --from=builder /src/spectralnorm.wasm /spectralnorm.wasm
ENTRYPOINT ["./spectralnorm.wasm"]
