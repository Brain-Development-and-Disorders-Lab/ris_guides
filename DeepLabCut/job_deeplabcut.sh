#!/bin/bash
# Switch into the correct directory
cd $STORAGE1/Dunnarts/DeepLabCut_Projects/

# Install the conda environment
conda env create -f DEEPLABCUT.yaml

# Activate the conda environment
eval "$(conda shell.bash hook)" # https://stackoverflow.com/a/56155771
conda activate DEEPLABCUT

# Run the Python training script
python train.py
