# Run the DeepLabCut training
import deeplabcut

# Note: Ensure configuration file has been updated for relocated project files
path_config_file = "/storage1/fs1/linda.richards.projects/Active/Dunnarts/DeepLabCut_Projects/dunnart_behaviour_test_project-Henry-2024-01-25/config.yaml" # Path to configuration file

# Create the training dataset
deeplabcut.create_training_dataset(path_config_file, net_type="efficientnet-b0")

# Train the network
deeplabcut.train_network(path_config_file)
