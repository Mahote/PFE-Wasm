FROM ghcr.io/vmware-labs/python-wasm:3.11.1-wasmedge


COPY fannkuch.py .


ENTRYPOINT [ "python.wasm", "fannkuch.py" ]
