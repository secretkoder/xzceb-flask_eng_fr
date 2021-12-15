"""A simple module to translate between english and french"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(englishText):
    """A simple English to French Translator method"""
    if (englishText in ["", None]):
        return englishText
    translation = language_translator.translate(
        text=englishText,
        model_id='en-fr').get_result()
    return translation["translations"][0]['translation']


def frenchToEnglish(frenchText):
    """A simple French to English Translator method"""
    if (frenchText in ["", None]):
        return frenchText
    translation = language_translator.translate(
        text=frenchText,
        model_id='fr-en').get_result()
    return translation["translations"][0]['translation']
