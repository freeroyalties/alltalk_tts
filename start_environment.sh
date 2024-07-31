#!/bin/bash
cd "."
if [[ "/home/mark/voice/alltalk_tts" =~ " " ]]; then echo This script relies on Miniconda which can not be silently installed under a path with spaces. && exit; fi
# deactivate existing conda envs as needed to avoid conflicts
{ conda deactivate && conda deactivate && conda deactivate; } 2> /dev/null
# config
CONDA_ROOT_PREFIX="/home/mark/voice/alltalk_tts/alltalk_environment/conda"
INSTALL_ENV_DIR="/home/mark/voice/alltalk_tts/alltalk_environment/env"
# environment isolation
export PYTHONNOUSERSITE=1
unset PYTHONPATH
unset PYTHONHOME
export CUDA_PATH="/home/mark/voice/alltalk_tts/alltalk_environment/env"
export CUDA_HOME="/home/mark/voice/alltalk_tts/alltalk_environment/env"
export LD_LIBRARY_PATH=/home/mark/voice/alltalk_tts/alltalk_environment/env/lib/python3.11/site-packages/nvidia/cublas/lib:/home/mark/voice/alltalk_tts/alltalk_environment/env/lib/python3.11/site-packages/nvidia/cudnn/lib
# activate env
bash --init-file <(echo "source \"/home/mark/voice/alltalk_tts/alltalk_environment/conda/etc/profile.d/conda.sh\" && conda activate \"/home/mark/voice/alltalk_tts/alltalk_environment/env\"")
