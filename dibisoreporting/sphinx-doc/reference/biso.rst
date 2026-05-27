Biso
====

Class to generate a BISO report.

By default the report contains the following visualizations:

* AnrProjects
* Chapters
* CollaborationMap: name = "world", countries_to_ignore = ["France"]
* CollaborationMap: name = "europe", resolution = 50, map_zoom = True
* CollaborationNames
* Conferences
* EuropeanProjects
* Journals
* OpenAccessWorks
* WorksType


This comes from the default value of ``default_visualizations`` :

.. code-block:: python

    default_visualizations =  {
        "AnrProjects": [
            {
                "max_plotted_entities": 20
            }
        ],
        "Chapters": [{}],
        "CollaborationMap": [
            {
                "name": "world",
                "countries_to_ignore": ["France"],
                "stats_to_save": {
                    "collaborations_nb": "collaborationsnb",
                    "institutions_nb": "institutionsnb",
                    "countries_nb": "countriesnb"
                },
            },
            {
                "name": "europe",
                "resolution": 50,
                "map_zoom": True,
            }
        ],
        "CollaborationNames": [
            {
                "countries_to_exclude": ["fr"],
                "max_plotted_entities": 40
            }
        ],
        "Conferences": [
            {
                "max_plotted_entities": 40
            }
        ],
        "EuropeanProjects": [
            {
                "max_plotted_entities": 20
            }
        ],
        "Journals": [
            {
                "stats_to_save": {
                    "nb_works": "bsojournalsnbworks",
                    "nb_works_found_in_bso": "bsojournalsnbworksfoundinbso",
                    "nb_journals": "bsojournalsnbjournals",
                    "bso_version": "bsojournalsbsoversion"
                },
            }
        ],
        "JournalsHal": [
            {
                "max_plotted_entities": 40
            }
        ],
        "OpenAccessWorks": [
            {
                "stats_to_save": {
                    "oa_works_period": "oaworksperiod"
                }
            }
        ],
        "PrivateSectorCollaborations": [
            {
                "max_plotted_entities": 35
            }
        ],
        "WorksBibtex": [
            {
                "max_plotted_entities": 1000
            }
        ],
        "WorksType": [{}],
    }


When needing statistics values to be printed in the report, you can export variables with the argument
``stats_to_save``.
You need to provide a dictionary with the keys being the name of the variables returned by the plotting library and the
values being the name of the variable in the report (aka the name of the macro in the LaTeX report).
In the above example, ``collaborations_nb`` is the key of the variable in the dictionary returned by the plotting
library and and ``collaborationsnb`` is the name of the LaTeX macro containing the value of the variable for the report,
callable with ``\collaborationsnb``.
The plotting library needs to return those variables in a dictionary returned by the method ``fetch_data()``.

The Biso Class
--------------

.. autoclass:: dibisoreporting.biso.Biso
   :members:
   :show-inheritance:
   :inherited-members:
   :undoc-members:
