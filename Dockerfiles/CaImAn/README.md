# CaImAn

> ℹ️ Docker image for the [CaImAn](https://github.com/flatironinstitute/CaImAn) repository.

## Usage - Interactive

1. Export a port prior to running the job: `export LSF_DOCKER_PORTS='8888:8888'`

2. Export any storage required for accessing data during the job (Note: This example makes the `HOME`, `STORAGE1`, and `CAIMAN_DATA` paths available during the job): `export STORAGE1=/storage1/fs1/<RIS directory>`, `export CAIMAN_DATA=/storage1/fs1/<Temporary file directory>`, `export LSF_DOCKER_VOLUMES="$HOME:$HOME $STORAGE1:$STORAGE1 $CAIMAN_DATA:$CAIMAN_DATA"`

3. Start the job (Note: This configuration uses 64GB of RAM, and 16 vCPUs by default): `bsub -R "rusage[mem=64GB]" -R "select[port8888=1]" -n 16 -Is -q general-interactive -a 'docker(henryburgess/caiman:latest)' /bin/bash`

4. Activate the Anaconda environment: `conda activate caiman`

5. Change into the `STORAGE1` directory `cd $STORAGE1` (optional), and start a Jupyter Notebook instance: `jupyter notebook --ip=0.0.0.0 --NotebookApp.allow_origin=* --port=8888`

6. Access the Jupyter Notebook instance via a web browser at the following URL: `http://compute1-exec-nn.ris.wustl.edu:8888/?token=<48-character token>`. The actual token is contained in the output from step 5.

## Usage - General

1. Export any storage required for accessing data during the job (Note: This example makes the `HOME`, `STORAGE1`, and `CAIMAN_DATA` paths available during the job): `export STORAGE1=/storage1/fs1/<RIS directory>`, `export CAIMAN_DATA=/storage1/fs1/<temporary file directory>`, `export LSF_DOCKER_VOLUMES="$HOME:$HOME $STORAGE1:$STORAGE1 $CAIMAN_DATA:$CAIMAN_DATA"`

2. Set execution permissions on the shell script: `chmod +x <path to shell script>`.

3. Start the job (Note: This configuration uses 64GB of RAM, and 16 vCPUs by default): `bsub -R "rusage[mem=64GB]" -n 16 -q general -a 'docker(henryburgess/caiman:latest)' <path to shell script>`

## Notes

* When running in `general`, make sure the `start_pipeline.sh` script has executable permissions (`chmod +x <path to shell script>`).
* For larger files (> 5GB), notebook usage is patchy and may crash. Ensure there is sufficient memory for the kernel, but if all else fails, create a Python script with the workbook contents instead.
