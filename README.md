# RIS Guides

A collection of Dockerfiles, documentation, and other scripts used on the WashU RIS Compute platform.

## Dockerfiles

* `CaImAn`: Docker image and scripts for using the [CaImAn](https://github.com/flatironinstitute/CaImAn) tool on RIS.

* `cisTarget`: Docker image and scripts for using the [create_cisTarget_databases](https://github.com/aertslab/create_cisTarget_databases) tool on RIS.

* `DeepLabCut`: Docker image and scripts for using DeepLabCut on RIS, making use of GPUs. Updated from [rob-the-bot/washu_hpc](https://github.com/rob-the-bot/washu_hpc/blob/main/ubuntu_gpu_docker/Dockerfile). Includes: updated `DEEPLABCUT.yaml` conda environment that works alongside the Docker image; `job_deeplabcut.sh` script to execute from $HOME directory; and `train.py` for long jobs submitted outside the `general-interactive` job queue.

* `RStudio`: Docker image and scripts for using the [RStudio](https://posit.co/download/rstudio-desktop/) application on RIS.

* `SCENIC+`: Docker image and scripts for using the [SCENIC+](https://github.com/aertslab/scenicplus) Python library with Jupyter Notebook on RIS, making use of GPUs.

## Documentation

* Transferring Data: Guidance on how to use the `rclone` tool to transfer large files and folders between RIS and Box.

## License

<!-- CC BY-NC-SA 4.0 License -->
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">
  <img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" />
</a>
<br />
This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

## Issues and Feedback

Please contact **Henry Burgess** <[henry.burgess@wustl.edu](mailto:henry.burgess@wustl.edu)> for all code-related issues and feedback.
