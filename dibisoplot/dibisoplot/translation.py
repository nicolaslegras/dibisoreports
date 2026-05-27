import gettext
import logging
import warnings
import os
from typing import Callable

def get_translator(
        domain: str = 'dibisoplot',
        language: str = 'en',
        locale_dir: str | None = None
) -> Callable[[str], str]:
    """
    Initialize and return a gettext translation function for the specified domain and language.
    If the language is English or no translation files are found, it falls back to null translations, which are English
    strings.
    If the locale directory is not provided, it defaults to a 'locales' directory relative to this file.

    :param domain: The gettext domain to use for translations. Defaults to 'dibisoplot'.
    :type domain: str
    :param language: The language code for the desired translations (e.g., 'fr', 'en'). Defaults to 'en'.
    :type language: str
    :param locale_dir: Path to the directory containing translation files.
        If None, defaults to a 'locales' directory relative to this file.
    :type locale_dir: str | None
    :return: A translation function (gettext) that translates strings to the specified language.
        If translation files are missing or the language is English, returns a null translator.
    :rtype: Callable[[str], str]
    """
    # If locale_dir is not provided, use the default path relative to this file
    if locale_dir is None:
        # Get the directory where this translation.py file is located
        current_dir = os.path.dirname(os.path.abspath(__file__))
        locale_dir = os.path.join(current_dir, 'locales')
    
    # if English, using original strings
    if language == "en":
        translation = gettext.NullTranslations()
    else:
        try:
            translation = gettext.translation(domain, localedir=locale_dir, languages=[language])
        except FileNotFoundError as e:
            warnings.warn(
                f"No translation files found for {language} language. "
                "Using null translations (original English strings)."
            )
            logging.warning(e)
            translation = gettext.NullTranslations()
    return translation.gettext
