# Setup logging
import logging
logger = logging.getLogger("caiman")
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
log_format = logging.Formatter("%(relativeCreated)12d [%(filename)s:%(funcName)10s():%(lineno)s] [%(process)d] %(message)s")
handler.setFormatter(log_format)
logger.addHandler(handler)


logger.info("Importing CaImAn...")
import caiman as cm
from caiman.motion_correction import MotionCorrect
from caiman.source_extraction.cnmf import cnmf, params
from caiman.utils.utils import download_demo
from caiman.utils.visualization import plot_contours, nb_view_patches, nb_plot_contour
from caiman.utils.visualization import nb_view_quilt


logger.info("Importing other dependencies...")
import cv2
from IPython import get_ipython
import numpy as np
import os


# The following lines are only required for the notebook
# import bokeh.plotting as bpl
# bpl.output_notebook()
# import holoviews as hv
# hv.notebook_extension("bokeh")


logger.info("Configuring OpenCV...")
try:
  cv2.setNumThreads(0)
except Exception as exception:
  logger.error("Could not set the number of threads: {}".format(exception))
  pass


logger.info("Checking IPython...")
try:
  if __IPYTHON__:
    get_ipython().run_line_magic("load_ext", "autoreload")
    get_ipython().run_line_magic("autoreload", "2")
except Exception as exception:
  logger.error("Error when interacting with \'__IPYTHON__\' variable: {}".format(exception))
  pass


# Specify the base directory, containing all `FTD-...` folders
# BASE_DIRECTORY = "/Volumes/linda.richards.projects/Active/Dunnarts/CA/Z/A/"
BASE_DIRECTORY = "/storage1/fs1/linda.richards.projects/Active/Dunnarts/CA/Z/A/"


# File extensions
COMBINED_EXTENSION = "_comb.tif"
DATA_EXTENSION = ".hdf5"


def start():
  logger.info("Using base directory: {}".format(BASE_DIRECTORY))
  for folder in os.listdir(BASE_DIRECTORY):
    folder_path = os.path.join(BASE_DIRECTORY, folder)
    if os.path.isdir(folder_path):
      logger.info("Found directory: {}".format(folder))

      # Flags for folder contents
      includes_combined = False
      includes_data = False

      # Filename for analysis input
      file_name = ""

      # Iterate over files in the directory
      for file in os.listdir(folder_path):
        full_filename = os.fsdecode(file)
        if full_filename.endswith(COMBINED_EXTENSION):
          includes_combined = True
          file_name = full_filename
          logger.info("File name: {}".format(file_name))
        elif full_filename.endswith(DATA_EXTENSION):
          includes_data = True

      # Respond accordingly
      if includes_combined == False:
        logger.warning("Folder does not contain combined .tif file")
      elif includes_combined == True and includes_data == True:
        logger.info("Folder contains analysis output, skipped")
      elif includes_combined == True and includes_data == False:
        logger.info("Folder does not contain analysis output, running analysis")
        run_pipeline(folder_path, file_name)


def run_pipeline(file_path, file_name):
  movie_path = os.path.join(file_path, file_name)
  logger.info("Combined file: {}".format(movie_path))

  save_file_name = str.join("", str(file_name).split(".")[:-1]) + "_output.hdf5"
  save_file = os.path.join(file_path, save_file_name)
  logger.info("Save file: {}".format(save_file))

  # Test file access
  with open(movie_path) as file:
      logger.info("Source movie file: %s", file.name)

  # general dataset-dependent parameters
  fr = 15                     # imaging rate in frames per second
  decay_time = 3            # length of a typical transient in seconds
  dxy = (2., 2.)              # spatial resolution in x and y in (um per pixel)

  # motion correction parameters
  max_shifts = (16,16)          # maximum allowed rigid shifts (in pixels)
  max_deviation_rigid = 3     # maximum shifts deviation allowed for patch with respect to rigid shifts
  pw_rigid = False             # flag for performing non-rigid motion correction

  # CNMF parameters for source extraction and deconvolution
  p = 2                       # order of the autoregressive system (set p=2 if there is visible rise time in data)
  gnb = 1                     # number of global background components (set to 1 or 2)
  bas_nonneg = True           # enforce nonnegativity constraint on calcium traces (technically on baseline)
  K = 500                     # number of components to be extracted

  # Enable the following lines if use patch-based CNMF
  # rf = 15                     # half-size of the patches in pixels (patch width is rf*2 + 1)
  # merge_thr = 0.85            # merging threshold, max correlation allowed
  # stride_cnmf = 10             # amount of overlap between the patches in pixels (overlap is stride_cnmf+1)
  # K = 4                       # number of components per patch

  gSig = np.array([2, 2])     # expected half-width of neurons in pixels (Gaussian kernel standard deviation)
  gSiz = 2*gSig + 1           # Gaussian kernel width and hight
  method_init = "greedy_roi"  # initialization method (if analyzing dendritic data see demo_dendritic.ipynb)
  ssub = 1                    # spatial subsampling during initialization
  tsub = 4                    # temporal subsampling during intialization

  # parameters for component evaluation
  min_SNR = 1.5               # signal to noise ratio for accepting a component
  rval_thr = 0.85             # space correlation threshold for accepting a component

  parameter_dict = {"fnames": movie_path,
                    "fr": fr,
                    "dxy": dxy,
                    "decay_time": decay_time,
                    "max_shifts": max_shifts,
                    "max_deviation_rigid": max_deviation_rigid,
                    "pw_rigid": pw_rigid,
                    "p": p,
                    "nb": gnb,
                    "K": K,
                    "gSig": gSig,
                    "gSiz": gSiz,
                    "method_init": method_init,
                    "rolling_sum": True,
                    "only_init": True,
                    "ssub": ssub,
                    "tsub": tsub,
                    "bas_nonneg": bas_nonneg,
                    "min_SNR": min_SNR,
                    "rval_thr": rval_thr,
                    "use_cnn": False}

  parameters = params.CNMFParams(params_dict=parameter_dict) # CNMFParams is the parameters class

  if "cluster" in locals():  # "locals" contains list of current local variables
      cm.stop_server(dview=cluster)
  _, cluster, n_processes = cm.cluster.setup_cluster(backend="multiprocessing", n_processes=4, ignore_preexisting=False)

  # Create model
  cnmf_model = cnmf.CNMF(n_processes, params=parameters, dview=cluster)

  # Motion correction & segmentation
  cnmf_model = cnmf_model.fit_file(motion_correct=True,include_eval=True)

  # Motion correction & segmentation
  cnmf_model.estimates.detrend_df_f(quantileMin=8, frames_window=1500, flag_auto=False)

  # Save the output file
  cnmf_model.save(save_file)
  cm.stop_server(dview=cluster)


if __name__ == "__main__":
    start()
