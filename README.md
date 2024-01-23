# GAN-skeleton-code 🫨

*New Emoji Generation using generative adversarial networks (GANs) - UCLA ACM AI, Projects, Fall '23*

## Training your model on Kaggle

We recommend using Kaggle for training, because it allows you to access GPU runtime for 12 hours. You can also try Google Colab; however Colab has a 90 min GPU usage limit before kicking you out.

1. Navigate to the [Full Emoji Image Kaggle Dataset](https://www.kaggle.com/datasets/subinium/emojiimage-dataset). Click on the "New Notebook" button to create a new notebook. The dataset should be automatically loaded in the `/kaggle/input` folder.

2. Import your Jupyter Notebook `main.ipynb` from your cloned GitHub repository using File > Import Notebook.
  
3. To use the GPU, click the three dots in the top-right corner and select Accelerator > GPU.

4. To access your code (in particular, the `data_utils.py` and `models.py` files), run the following command (replacing the URL):
   ```
   !git clone "https://github.com/latka-krystof/GAN-skeleton-code"
   ```
   This should clone this repository into the `/kaggle/working` folder.
   
6. Change directories into your repository by running the command:
   ```
   cd GAN-skeleton-code
   ```
5. You should now be able to import your code from these files normally.

6. If you want your code to run without keeping the tab open, you can click on "Save version" and commit your code. Make sure to save any outputs (e.g. log files) to the `/kaggle/output`, and you should be able to access them in the future.
