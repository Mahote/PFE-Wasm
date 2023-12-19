FROM emscripten/emsdk AS builder

COPY . .

RUN apt-get update && apt-get install -y \
    && emcc fannkuch-redux.c -o fannkuchredux.wasm

FROM scratch
COPY --from=builder /src/fannkuchredux.wasm /fannkuchredux.wasm
ENTRYPOINT ["./fannkuchredux.wasm"]