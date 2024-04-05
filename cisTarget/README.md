# cisTarget

> ℹ️ Docker image for the [create_cisTarget_databases](https://github.com/aertslab/create_cisTarget_databases) repository.

## Usage

1. Start the job: `bsub -R "rusage[mem=32GB]" -Is -q general-interactive -a 'docker(henryburgess/cistarget)' /bin/bash`
2. Activate the conda environment: `conda activate create_cistarget_databases`

## Notes

* This container uses Miniconda3 with Python 3.10 and includes the `cbust`, `liftOver`, and `bigWigAverageOverBed` executables.
* The container will start with the `create_cistarget_databases` conda environment active.
* The create_cisTarget_databases repository can be found at `~/create_cisTarget_databases` once the container is running.
