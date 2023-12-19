FROM ghcr.io/vmware-labs/python-wasm:3.11.1-wasmedge


COPY fasta.py .


ENTRYPOINT [ "python.wasm", "fasta.py" ]
