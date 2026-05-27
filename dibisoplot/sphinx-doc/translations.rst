Translations
************

.. _translations:

Installation
============

Do generate the ``mo`` files, you need to install the ``gettext`` utilities.
On Ubuntu or Debian systems, this can be done using the following command:

.. code-block:: bash

    sudo apt install gettext

Generate translations
=====================

Go to the ``dibisoplot`` directory before running the following command.

Step 1: Extract Translatable Strings
------------------------------------

Use the ``xgettext`` utility to extract strings from your Python script and generate a ``.pot`` (Portable Object Template) file.

To generate the ``.pot`` file from the ``Biso`` class, run:

.. code-block:: bash

    xgettext --output=locales/dibisoplot.pot --language=Python --keyword=_ --from-code=UTF-8 biso/biso.py

This command will create a ``.pot`` file in the locales directory with all the strings that need translation.

Step 2: Create and Edit Translation Files
-----------------------------------------

For each language you want to support, you'll create a ``.po`` file from the ``.pot`` template.
For example, to add French translations:

.. code-block:: bash

    mkdir -p locales/fr/LC_MESSAGES
    cp locales/dibisoplot.pot locales/fr/LC_MESSAGES/dibisoplot.po

Now, open ``locales/fr/LC_MESSAGES/dibisoplot.po`` in a text editor and add the translations.
Here is an example of what the content might look like after translation:

.. code-block:: none

    msgid "Hello!"
    msgstr "Bonjour!"

    msgid "This is a translatable string."
    msgstr "Ce message est une chaîne traduisible."

Step 3: Compile the Translation Files
-------------------------------------

Once the translations are added to the .po file, compile it into a .mo file (Machine Object file) using msgfmt:

.. code-block:: bash

    msgfmt locales/fr/LC_MESSAGES/dibisoplot.po -o locales/fr/LC_MESSAGES/dibisoplot.mo

The ``.mo`` file is what ``gettext`` will use at runtime to perform the translations.


Update translations
===================

To update the translations, you can use the ``msgmerge`` command to merge the latest changes from the ``.pot`` file into the ``.po`` file.
First, follow the step 1 to recreate the ``.pot`` file.
Then, run the following command to update the ``.po`` file:

.. code-block:: bash

    msgmerge --update locales/fr/LC_MESSAGES/dibisoplot.po locales/dibisoplot.pot

Then follow the step 3 to compile the ``.po`` file into a ``.mo`` file.

