# Corona Detection from Ct-Scan Images

## Installation of Streamlit

```bash
pip install streamlit
streamlit hello
```
## Installation of Project

```bash
git clone https://github.com/Dream4Theater/corona-detect-v1-streamlit-app
streamlit run app.py
```
That way u can easily get source code and run application on your local host.

## Installation of GCP

U should first create a project from GCP.
![Uploading image.png…]()

Then create a bucket for your project for adding model.

For adding model , i am using colab, u can add your trained model to bucket running this code.

```bash
from tensorflow import keras

model = keras.models.load_model(<your_model_path>)
model.save(<your_model_name>)

## Uploading a model to Google Storage from within Colab ##

# Authorize Colab and initalize gcloud (enter the appropriate inputs when asked)
from google.colab import auth
auth.authenticate_user()
!curl https://sdk.cloud.google.com | bash
!gcloud init

# Upload SavedModel to Google Storage Bucket
!gsutil cp -r <your_saved_model_path> gs://<your_bucket_name>
```

## Project site

U can also check how is project is looking by clicking [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dream4theater/corona-detect-v1-streamlit-app/app.py/) here.

## License

Streamlit is completely free and open-source and licensed under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license.


