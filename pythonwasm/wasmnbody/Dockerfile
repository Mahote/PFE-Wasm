FROM ghcr.io/vmware-labs/python-wasm:3.11.1-wasmedge


COPY nbody.py .


ENTRYPOINT [ "python.wasm", "nbody.py" ]
