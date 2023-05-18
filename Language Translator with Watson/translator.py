from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('6I2OmJKLCxjwmAK-UWQwKplgiO-acMQaaPGpMmW39y0M')
language_translator = LanguageTranslatorV3(
    version='2023-05-18',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/c94faa41-b3dd-4e82-a719-7eb15d1ef39c')

def english_to_french(text1):
    """
    This function translate english to french
    """
    frenchtranslation = language_translator.translate(text=text1, model_id='en-ur').get_result()

    return frenchtranslation.get("translations")[0].get("translation")
def french_to_english(text1):
    """
        This function translate english to french
        """
    englishtranslation = language_translator.translate(text=text1, model_id='fr-en').get_result()

    return englishtranslation.get("translations")[0].get("translation")

print(english_to_french('I want to tell you something but I can not'))