#!/bin/bash
export TRAINER_TELEMETRY=0
export LD_LIBRARY_PATH=/home/mark/voice/alltalk_tts/alltalk_environment/env/lib/python3.11/site-packages/nvidia/cublas/lib:/home/mark/voice/alltalk_tts/alltalk_environment/env/lib/python3.11/site-packages/nvidia/cudnn/lib
source "/home/mark/voice/alltalk_tts/alltalk_environment/conda/etc/profile.d/conda.sh"
conda activate "/home/mark/voice/alltalk_tts/alltalk_environment/env"
python train_finetune.py
