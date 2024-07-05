#!/bin/bash
export TRAINER_TELEMETRY=0
export LD_LIBRARY_PATH=/home/mark/voice/ai-voice-cloning/venv/lib/python3.10/site-packages/nvidia/cublas/lib:/home/mark/voice/ai-voice-cloning/venv/lib/python3.10/site-packages/nvidia/cudnn/lib
source "/home/mark/voice/alltalk_tts/alltalk_environment/conda/etc/profile.d/conda.sh"
conda activate "/home/mark/voice/alltalk_tts/alltalk_environment/env"
python finetune.py
