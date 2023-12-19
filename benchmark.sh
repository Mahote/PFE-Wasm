#!/bin/bash

echo "Which pair do you want to process?"
echo "1: C and Cwasm"
echo "2: C++ and C++wasm"
echo "3: Python and Pythonwasm"

read choice
ITER=10
binarytrees_params=(1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18)
pidigits_params=(100 250 500 1000 2500 5000 7500)
nbody_params=(25000 50000 100000 250000 500000 1000000)
fannkuch_params=(3 4 5 6 7 8 9 10 11 12)
fasta_params=(1000 10000 100000 1000000 5000000)
spectralnorm_params=(50 100 500 1000 2500 5000)
mandelbrot_params=(500 1000 1500 2000 2500)
binarytrees_paramswasm=(1 2 3 4 5 6 7 8 9 10 11 12)
pidigits_paramswasm=(100 250 500 1000 2500)
nbody_paramswasm=(2500 5000 7500 10000)
fannkuch_paramswasm=(3 4 5 6 7 8 9 10)
fasta_paramswasm=(10 100 1000 2500 3750 5000 10000)
spectralnorm_paramswasm=(25 50 75 100 125 150 200)
mandelbrot_paramswasm=(50 100 125 150 200)



case $choice in
  1)
    base_dirs=("C" "Cwasm")
    language="c"
    ;;
  2)
    base_dirs=("C++" "C++wasm")
    language="cpp"
    
    ;;
  3)
    base_dirs=("pythonwasm")
    language="python"
    ;;
  *)
    echo "Invalid choice"
    exit 1
    ;;
esac
echo ${binarytrees_params[@]}
function launch_docker() {
  iter=$1
  use_wasm=$2
  language=$3
  program=$4
  params = ${program}_params[@]
  if [ "$use_wasm" = true ]; then
    ext="-wasm${program}"
    params=${program}_paramswasm[@]
    params_values=${!params}
    docker_cmd="docker run -p 8080:8080 --runtime=io.containerd.wasmedge.v1 --platform=wasi/wasm32 ${language}wasm${program}docker"
  else
    params=${program}_params[@]
    params_values=${!params}
    ext="-${program}"
    docker_cmd="docker run -p 8080:8080 ${language}${program}docker"
  fi
  
  for i in $(seq 0 $iter); do
    for j in $params_values; do
      echo $docker_cmd $j
      start=$(date +%s%N)
      eval "$docker_cmd $j"
      end=$(date +%s%N)
      runtime=$(($(($end - $start))/1000000))
      echo $j $runtime >> ../../data/${program}/${language}${j}${ext}.txt;
    done
  done
}

# Loop through the base directories and execute the script
for base_dir in "${base_dirs[@]}"; do
    cd "$base_dir"
    echo "Processing base directory: $base_dir"
    # Find all subdirectories
    sub_dirs=`ls -d */`
    # Loop through the subdirectories and execute the script
    for dir in $sub_dirs; do
        dirname="${dir%/}"
        dockername="${dirname,,}"
        program=${dockername/wasm/}
        use_wasm=false 
        cd "$dirname"
        echo "Building Docker image for ${language}${dockername}docker"
        if [[ $dirname == *"wasm"* ]]; then
            docker build -t ${language}${dockername}docker . --platform=wasi/wasm32 --no-cache
            use_wasm=true
        else
            docker build -t ${language}${dockername}docker . --no-cache
        fi
        # Run the container using the launch_docker function
        case $program in
            "binarytrees")
                launch_docker $ITER  $use_wasm $language "binarytrees"
                ;;
            "pidigits")
                launch_docker $ITER $use_wasm $language "pidigits"
                ;;
            "nbody")
                launch_docker $ITER $use_wasm $language "nbody"
                ;;
            "fannkuch")
                launch_docker $ITER $use_wasm $language "fannkuch"
                ;;
            "fasta")
                launch_docker $ITER $use_wasm $language "fasta"
                ;;
            "spectralnorm")
                launch_docker $ITER $use_wasm $language "spectralnorm"
                ;;
            "mandelbrot")
                launch_docker $ITER $use_wasm $language "mandelbrot"
                ;;
            *)
                echo "Invalid directory name: $program"
                ;;
        esac
        cd ..
    done
    cd ..
done