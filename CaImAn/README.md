# CaImAn

> ℹ️ Docker image for the [CaImAn](https://github.com/flatironinstitute/CaImAn) repository.

## Usage

1. Export a port prior to running the job: `export LSF_DOCKER_PORTS='8888:8888'`

2. Export any storage required for accessing data during the job (Note: This example makes the `$HOME` and `$STORAGE1` paths available during the job): `export STORAGE1=/storage1/fs1/<RIS directory>`, `export LSF_DOCKER_VOLUMES="$HOME:$HOME $STORAGE1:$STORAGE1"`

3. Export the CaImAn `caiman_data` directory (Note: Required since CaImAn generates large ): `export CAIMAN_DATA=<Temporary file directory>`

4. Start the job (Note: This configuration uses 64GB of RAM, and 16 vCPUs by default): `bsub -R "rusage[mem=64GB]" -R "select[port8888=1]" -n 16 -Is -q general-interactive -a 'docker(henryburgess/caiman:1.0)' /bin/bash`

5. Activate the Anaconda environment: `conda activate caiman`

6. Start a Jupyter Notebook instance: `jupyter notebook --ip=0.0.0.0 --NotebookApp.allow_origin=* --port=8888`

7. Access the Jupyter Notebook instance via a web browser at the following URL: `http://compute1-exec-nn.ris.wustl.edu:8888/?token=<48-character token>`. The actual token is contained in the output from step 5.
