FROM emscripten/emsdk AS builder

COPY . .

RUN apt-get update && apt-get install -y && apt-get install -y gcc wget build-essential \
    && chmod 777 compil_dep.sh && ./compil_dep.sh \
	&& emcc pidigits.c ${HOME}/opt/lib/libgmp.a -I${HOME}/opt/include -o pidigits.wasm

FROM scratch
COPY --from=builder /src/pidigits.wasm /pidigits.wasm
ENTRYPOINT ["./pidigits.wasm"]