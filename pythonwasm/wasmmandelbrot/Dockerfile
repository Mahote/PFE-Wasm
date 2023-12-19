FROM ghcr.io/vmware-labs/python-wasm:3.11.1-wasmedge


COPY mandelbrot.py .


ENTRYPOINT [ "python.wasm", "mandelbrot.py" ]
