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
That way u can easily get source code and run application on your local host. But it will give errors because u need GCP project for image prediction.

## Installation of GCP

1. U should first create a project from GCP.

2. Then create a bucket for your project for adding model.

![alt text](https://github.com/Dream4Theater/corona-detect-v1-streamlit-app/blob/master/images/image2.png?raw=true)

3. For adding model , i am using colab, u can add your trained model to bucket running this code.

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

Your model should appear on bucket now u upload your model to GCP.

![alt text](https://github.com/Dream4Theater/corona-detect-v1-streamlit-app/blob/master/images/image3.png?raw=true)

So with working your model u need version of it.

![alt text](https://github.com/Dream4Theater/corona-detect-v1-streamlit-app/blob/master/images/image4.png?raw=true)

And finally u should add API service to app work.

![alt text](https://github.com/Dream4Theater/corona-detect-v1-streamlit-app/blob/master/images/image5.png?raw=true)

And now u good to go if everything is okay ur project should be looking like this [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dream4theater/corona-detect-v1-streamlit-app/app.py/)

## License

Streamlit is completely free and open-source and licensed under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license.


