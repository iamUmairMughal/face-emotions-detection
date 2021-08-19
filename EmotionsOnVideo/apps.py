from django.apps import AppConfig
import tensorflow

keras_file = "model/self_trained/model_weights.h5"
model = tensorflow.keras.models.load_model(keras_file)

class EmotionsonvideoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'EmotionsOnVideo'
