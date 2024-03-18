# SCENIC+ and Jupyter Notebook

> This Docker container allows you to use SCENIC+ with a Jupyter Notebook.

## Usage

1. Export a port prior to running the job: `export LSF_DOCKER_PORTS='8888:8888'`

2. Start the job: `bsub -R 'gpuhost' -R "rusage[mem=32GB]" -gpu "num=1:gmodel=TeslaV100_SXM2_32GB" -Is -q general-interactive -R 'select[port8888=1]' -a 'docker(henryburgess/scenic-notebook)' /bin/bash`

3. Run any setup prior to starting the Jupyter Notebook instance.

4. Start a Jupyter Notebook instance: `jupyter notebook --ip=0.0.0.0 --NotebookApp.allow_origin=*`

5. Access the Jupyter Notebook instance via a web browser at the following URL: `http://compute1-exec-nn.ris.wustl.edu:8888/?token=<48-character token>`. The actual token is contained in the output from step 4.
