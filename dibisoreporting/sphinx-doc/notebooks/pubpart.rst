PubPart
=======

Example to generate a Publications & Partnerships report.

This generates the report for the collaborations between Université
Paris-Saclay and Stockholms Universitet, years 2024-2025.

.. code:: ipython3

    from dibisoreporting import PubPart
    
    biso_reporting = PubPart(
        "I277688954",
        "2024-2025",
        secondary_entity_id = "I265217849",
        entities_acronym = "UPSaclay et SU",
        entities_full_name = "Université Paris-Saclay et Stockholms Universitet",
        latex_main_file_url = "https://raw.githubusercontent.com/dibiso-upsaclay/dibiso-latex-templates/refs/heads/main/examples/biso/biso-main.tex",
        latex_biblio_file_url = "https://raw.githubusercontent.com/dibiso-upsaclay/dibiso-latex-templates/refs/heads/main/examples/biso/biso-biblio.tex",
        latex_template_url = "https://github.com/dibiso-upsaclay/dibiso-latex-templates/releases/latest",
        plot_main_color = "#63003C",
        root_path = "pubpart_report",
        watermark_text = "EXAMPLE",
    )
    
    
    biso_reporting.generate_report()

| Romain THOMAS 2025
| DiBISO - Université Paris-Saclay
