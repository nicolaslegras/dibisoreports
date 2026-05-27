BiSO
====

Example to generate a BiSO report (Bilan de la Science Ouverte:
Open-Science report).

This generates the report for the Université Paris-Salcay, year 2024,
and limits the number of works to the value set by ``max_entities``
(100) in the library ``dibisoplot``.

.. code:: ipython3

    from dibisoreporting import Biso
    
    import os
    from dotenv import load_dotenv
    
    load_dotenv()
    
    biso_reporting = Biso(
        "UNIV-PARIS-SACLAY",
        2024,
        entity_acronym = "UPSaclay",
        entity_full_name = "Université Paris-Saclay",
        latex_main_file_url = "https://raw.githubusercontent.com/dibiso-upsaclay/dibiso-latex-templates/refs/heads/main/examples/biso/biso-main.tex",
        latex_biblio_file_url = "https://raw.githubusercontent.com/dibiso-upsaclay/dibiso-latex-templates/refs/heads/main/examples/biso/biso-biblio.tex",
        latex_template_url = "https://github.com/dibiso-upsaclay/dibiso-latex-templates/releases/latest",
        max_entities = 1000,
        root_path = "test_report",
        watermark_text = "DUMMY DATA",
        scanr_api_password = os.getenv("SCANR_API_PASSWORD"),
        scanr_api_url = os.getenv("SCANR_API_URL"),
        scanr_api_username = os.getenv("SCANR_API_USERNAME"),
        scanr_bso_index = os.getenv("SCANR_BSO_INDEX"),
        scanr_publications_index = os.getenv("SCANR_PUBLICATIONS_INDEX"),
    )
    
    # Don't add more than 100 references to the bibtex references file:
    visualizations_to_make_custom_config = {
        "WorksBibtex": [
            {
                "max_plotted_entities": 100
            }
        ]
    }
    
    # generate the report with the custom config:
    biso_reporting.generate_report(
        visualizations_to_make = visualizations_to_make_custom_config
    )

| Romain THOMAS 2025
| DiBISO - Université Paris-Saclay
