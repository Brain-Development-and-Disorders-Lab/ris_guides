# RStudio

> Guidance on how to use RStudio on the RIS.

## Starting RStudio via OOD

> [!IMPORTANT]
> You will need to have access to RIS Compute to use the Open OnDemand (OOD) platform.

1. Log into Open OnDemand: [Open OnDemand](https://ood.ris.wustl.edu/pun/sys/dashboard/)
2. Click on the "Interactive Apps" menu item, and click on the "RStudio" tile.
3. Under "Mounts", include a mount for the following directories (this will allow you to interact with RIS Storage inside the RStudio instance):
    * `/storage1/fs1/linda.richards.projects/Active:/storage1/fs1/linda.richards.projects/Active`
4. Increase memory to at least 24 GB, preferably 32 GB. Set "Number of processors" to at least 4, ideally 8. All other options can be left as-is.
5. Click "Launch".
6. Once the job is ready, click "Connect to RStudio Server" to launch the RStudio instance in a separate browser tab.

## Accessing RIS Storage inside RStudio

> The RIS Storage is not initially directly accessible from the file browser panel in the lower-right corner of the RStudio interface.

1. Click the "..." button in the top-right corner of the file browser panel. A panel with title "Go To Folder" will appear.
2. Enter the path to the mounted directory from Step 3 above, e.g. `/storage1/fs1/linda.richards.projects/Active`.
3. Click "OK", and the RIS Storage directory will be opened in the file browser.
4. Once you have navigated to the directory you want to work from, click the "More" button at the top of the file browser panel, and click "Set As Working Directory".
