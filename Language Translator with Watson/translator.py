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
    frenchtranslation = language_translator.translate(text=text1, model_id='en-fr').get_result()

    return frenchtranslation.get("translations")[0].get("translation")
def french_to_english(text1):
    """
        This function translate english to french
        """
    englishtranslation = language_translator.translate(text=text1, model_id='fr-en').get_result()

    return englishtranslation.get("translations")[0].get("translation")

# English to urdu
def english_to_urdu(text1):
    """
    This function will translate from english to urdu
    """
    urdutranslation = language_translator.translate(text=text1, model_id='en-ur').get_result()
    return urdutranslation.get("translations")[0].get("translation")

# French to English
print(french_to_english('Je veux te dire quelque chose'))

while True:
    print("For English to Urdu: Press 1\n")
    print("For English to French: Press 2\n")
    print("For Exit: Press 3")
    choice = int(input("Make your choice: "))

    if(choice ==  1):
        texts = input("Enter sentence in English: ")
        print(english_to_urdu(texts))
    elif(choice == 2):
        texts = input("Enter sentence in English: ")
        print(english_to_french(texts))
    elif(choice == 3):
        print("Thanks for Using our language Translator")
        break
    else:
        print("You have entered a wrong choice: Try Again")





