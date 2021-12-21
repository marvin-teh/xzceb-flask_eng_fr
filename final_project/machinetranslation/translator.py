import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('VzRHo7uOXU3_316kH5NY0eRJFQ15RnRDsZL3cI49EmSw')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(
    'https://api.us-south.language-translator.watson.cloud.ibm.com/instances/d0ab8a65-878c-454f-86e2-56ff238a5627')

def english_to_french(english_text):
    if(english_text=='' or english_text is None):
        return 'Please enter an English text'

    e2f = language_translator.translate(text=english_text, model_id='en-fr').get_result()
    french_text = e2f['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    if(french_text=='' or french_text is None):
        return 'Please enter a French text'

    f2e = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    english_text = f2e['translations'][0]['translation']
    return english_text