FROM ghcr.io/vmware-labs/python-wasm:3.11.1-wasmedge


COPY pidigits.py .


ENTRYPOINT [ "python.wasm", "pidigits.py" ]
