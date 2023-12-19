# Wasm Benchmark

This project is a university project, the main goal is to see the new technology of docker+wasm

## Getting started

First of  all you need to follow this [guide](https://docs.docker.com/desktop/wasm/) to active Docker+Wasm bêta, and of course have docker on your computer very important you need to start docker desktop before running the benchmark.
## run the benchmark
`./benchmark.sh`
To get the data to plot you need tu launch all the benchmark you have three choices :
- 1 : C and Cwasm 
- 2 : Cpp and Cppwasm
- 3 : python and pythonwasm

Important : you might need to remove the images and containers before launching each benchmark, it depends on the space you allow to docker desktop

Important : to plot all the data you need to launch all three benchmarks for `./plot.sh` to work correctly, if you dont do all the benchmark you will get errors.
Data is in the directory `data` each applications of the CLBG that could be computed to wasm has is subdirectory inside.
All of the plots are in te `res` directory with the same hierarchy as for `data`

## Difficulties encounter : 
- Lot of time wasted to compile bash in wasm which happens to be impossible as i know even when you succeed to compile with emcc and all the dependencies you cant launch the .wasm
- Emcc is a great tool but need to be more developped there is lots of library missing, for example i had to change `ulong` to `unsigned long` because emcc use a Clang compiler so it doesn't recognize it.
- Python is in alpha stage for wasm to work on it so its very very slow.

## Conclusion 
you can see all of my plots and data gathered in the `public` directory for each applications
To conclude wasm is a great technology to run complex operation in the browser in order to gain performance but as for wasm docker the technology is in early stage, if you want to build web application using low level language I recommend using `rust`.  
I think Docker+Wasm will be useful to run specific module inside a web application deployed on container but it needs to be improve.
Also in one of my plot the `allfastalog` Cwasm is below the curve of C but i checked the data and Cwasm curve should follow closelly Cppwasm curve 


