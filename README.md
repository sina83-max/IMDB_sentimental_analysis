## Setting Up Kaggle API Credentials

In order to download the dataset using the Kaggle API, you'll need to set up your own Kaggle credentials.

### Option 1: Using the `kaggle.json` file

1. Go to your [Kaggle account](https://www.kaggle.com/account).
2. Scroll down to the **API** section and click **Create New API Token**. This will download a `kaggle.json` file containing your API credentials.
3. Place the `kaggle.json` file in the following location:
   - **Linux/macOS**: `~/.kaggle/kaggle.json`
   - **Windows**: `C:\Users\<Your-Username>\.kaggle\kaggle.json`

### Option 2: Using Environment Variables

Alternatively, you can set your credentials using environment variables:

1. Open a terminal and set the following environment variables (replace `<YOUR_USERNAME>` and `<YOUR_KEY>` with your own credentials):
   ```bash
   export KAGGLE_USERNAME=<YOUR_USERNAME>
   export KAGGLE_KEY=<YOUR_KEY>
   ```
