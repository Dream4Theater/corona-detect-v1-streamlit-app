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

4. Your model should appear on bucket now u upload your model to GCP.

![alt text](https://github.com/Dream4Theater/corona-detect-v1-streamlit-app/blob/master/images/image3.png?raw=true)

5. So with working your model u need version of it.

![alt text](https://github.com/Dream4Theater/corona-detect-v1-streamlit-app/blob/master/images/image4.png?raw=true)

6. And finally u should add API service to app work.

![alt text](https://github.com/Dream4Theater/corona-detect-v1-streamlit-app/blob/master/images/image5.png?raw=true)

## Deploying Streamlit

If u wanna know how to deploy a project on Streamlit share u should check out [here.](https://blog.streamlit.io/deploying-streamlit-apps-using-streamlit-sharing/)

## Conclusion

If u deploy your project to Streamlit, it should be looking like this [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dream4theater/corona-detect-v1-streamlit-app/app.py/) if code doesn't working that means i am out of free credits from GCP so u should be careful how u spend it.

This was my school project, for those of u did not understand how i managing things u should absolutely checkout Daniel Bourke's this [Github Project](https://github.com/mrdbourke/cs329s-ml-deployment-tutorial) github project how i learned things first place.
