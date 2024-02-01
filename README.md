# ris_docker

A collection of Dockerfiles used on the WashU RIS Compute platform.

## Dockerfiles

* `DeepLabCut`: Image for using DeepLabCut on RIS, making use of GPUs. Updated from [rob-the-bot/washu_hpc](https://github.com/rob-the-bot/washu_hpc/blob/main/ubuntu_gpu_docker/Dockerfile). Includes: updated `DEEPLABCUT.yaml` conda environment that works alongside the Docker image; `job_deeplabcut.sh` script to execute from $HOME directory; and `train.py` for long jobs submitted outside the `general-interactive` job queue.
