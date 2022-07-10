def translate_with_en_on_ru(translation):
    from translate import Translator
    translator= Translator(from_lang = 'en', to_lang = 'ru')
    translation = translator.translate(input())
    return translation

translation = 0
translation=translate_with_en_on_ru(translation)
print(translation)