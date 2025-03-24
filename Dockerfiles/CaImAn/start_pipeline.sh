#!/bin/bash

conda init
source ~/.bashrc
export CAIMAN_DATA="/storage1/fs1/linda.richards.projects/Active/Dunnarts/CA/Z/temp"
conda activate caiman
python /storage1/fs1/linda.richards.projects/Active/Dunnarts/CA/Z/FTD_Ca_WorkingNotebooks/caiman_pipeline_iterative.py
