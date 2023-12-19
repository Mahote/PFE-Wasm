FROM emscripten/emsdk AS builder

COPY . .

RUN apt-get update && apt-get install -y \
	&& emcc mandelbrot.c++ -o mandelbrot.wasm
FROM scratch
COPY --from=builder /src/mandelbrot.wasm /mandelbrot.wasm
ENTRYPOINT ["./mandelbrot.wasm"]