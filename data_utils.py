import torch

class Dataset(torch.utils.data.Dataset):
    def __init__(self, image_folder_path, desired_image_size):
        # initialize the data from the path
        pass

    def __getitem__(self, i):
        # return the ith image as a tensor
        pass

    def __len__(self):
        # return the length of the dataset
        pass