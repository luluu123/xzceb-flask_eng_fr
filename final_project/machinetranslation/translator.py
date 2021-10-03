import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

# Created tranalator instance
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version = '2018-05-01',
    authenticator = authenticator
)
language_translator.set_service_url(url)

# English to French Translation
def english_to_french(english_text):
    '''This function translates text from English to French'''
    translation = language_translator.translate(
                  text = english_text,
                  model_id ='en-fr').get_result()

    # Extract actual tranalated text
    french_text = translation.get('translations')[0].get('translation')
    return french_text

# French to English Translation
def french_to_english(french_text):
    '''French to English'''
    translation = language_translator.translate(
                  text = french_text,
                  model_id ='fr-en').get_result()

    # Extract actual tranalated text
    english_text = translation.get('translations')[0].get('translation')
    return english_text