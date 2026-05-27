BiSO
====

| Romain THOMAS 2025
| DiBISO - Université Paris-Saclay

Load environment variables
--------------------------

Load the environment variables from the ``.env`` file.

Then, load the API keys and index names, and store them in a dictionary
for further use.

.. code:: ipython3

    import os
    from dotenv import load_dotenv
    
    load_dotenv()
    
    scanr_config = {
        'scanr_api_password' : os.getenv("SCANR_API_PASSWORD"),
        'scanr_api_url' : os.getenv("SCANR_API_URL"),
        'scanr_api_username' : os.getenv("SCANR_API_USERNAME"),
        'scanr_bso_index' : os.getenv("SCANR_BSO_INDEX"),
        'scanr_publications_index' : os.getenv("SCANR_PUBLICATIONS_INDEX")
    }

.. code:: ipython3

    # This cell has the metadata: "nbsphinx": "hidden" to be hidden in the sphinx documentation
    
    # Create figure directory
    
    import os
    
    os.makedirs("figures/biso", exist_ok=True)

ANR Projects
------------

.. code:: ipython3

    from dibisoplot.biso import AnrProjects
    
    anr_projects = AnrProjects(
        entity_id="SUP_SONDRA",
        year = 2023,
    )
    
    anr_fig = anr_projects.get_figure()
    
    # anr_fig.show()

.. code:: ipython3

    # This cell has the metadata: "nbsphinx": "hidden" to be hidden in the sphinx documentation
    
    anr_fig.update_layout(
        autosize=True,
        margin=dict(l=20, r=20, t=20, b=20),  # Reduce margins
        width=None,  # Let the iframe control width
        height=None, # Let the iframe control height
    )
    anr_fig.write_html(
        "figures/biso/anr_projects.html",
        include_plotlyjs="cdn",
        full_html=False,
        config={"responsive": True}
    )

.. container::

Chapters
--------

.. code:: ipython3

    from dibisoplot.biso import Chapters
    
    chapters = Chapters(
        entity_id="IEDP",
        year = "2023",
    )
    
    chapters_latex = chapters.get_figure()
    
    print(chapters_latex)

Collaboration Map
-----------------

.. code:: ipython3

    from dibisoplot.biso import CollaborationMap
    
    collab_map = CollaborationMap(
        entity_id="LISN",
        year = 2023,
        countries_to_ignore = ["France"],
    )
    
    collab_map_fig = collab_map.get_figure()
    
    # collab_map_fig.show()

.. code:: ipython3

    # This cell has the metadata: "nbsphinx": "hidden" to be hidden in the sphinx documentation
    
    collab_map_fig.update_layout(
        autosize=True,
        margin=dict(l=20, r=20, t=20, b=20),  # Reduce margins
        width=None,  # Let the iframe control width
        height=None, # Let the iframe control height
    )
    collab_map_fig.write_html(
        "figures/biso/collaboration_map.html",
        include_plotlyjs="cdn",
        full_html=False,
        config={"responsive": True}
    )

.. container::

Collaboration Names
-------------------

.. code:: ipython3

    from dibisoplot.biso import CollaborationNames
    
    collabs = CollaborationNames(
        entity_id="LISN",
        year = 2023,
        countries_to_exclude = ['fr'],
    )
    
    collabs_fig = collabs.get_figure()
    
    # collabs_fig.show()

.. code:: ipython3

    # This cell has the metadata: "nbsphinx": "hidden" to be hidden in the sphinx documentation
    
    collabs_fig.update_layout(
        autosize=True,
        margin=dict(l=20, r=20, t=20, b=20),  # Reduce margins
        width=None,  # Let the iframe control width
        height=None, # Let the iframe control height
    )
    collabs_fig.write_html(
        "figures/biso/collaboration_names.html",
        include_plotlyjs="cdn",
        full_html=False,
        config={"responsive": True}
    )

.. container::

Conferences
-----------

.. code:: ipython3

    from dibisoplot.biso import Conferences
    
    conf = Conferences(
        entity_id="LGI",
        year = 2023,
    )
    
    conf_fig = conf.get_figure()
    
    # conf_fig.show()

.. code:: ipython3

    # This cell has the metadata: "nbsphinx": "hidden" to be hidden in the sphinx documentation
    
    conf_fig.update_layout(
        autosize=True,
        margin=dict(l=20, r=20, t=20, b=20),  # Reduce margins
        width=None,  # Let the iframe control width
        height=None, # Let the iframe control height
    )
    conf_fig.write_html(
        "figures/biso/conferences.html",
        include_plotlyjs="cdn",
        full_html=False,
        config={"responsive": True}
    )

.. container::

European Projects
-----------------

.. code:: ipython3

    from dibisoplot.biso import EuropeanProjects
    
    eu_projects = EuropeanProjects(
        entity_id="UMPHY",
        year = 2023,
    )
    
    eu_projects_fig = eu_projects.get_figure()
    
    # eu_projects_fig.show()

.. code:: ipython3

    # This cell has the metadata: "nbsphinx": "hidden" to be hidden in the sphinx documentation
    
    eu_projects_fig.update_layout(
        autosize=True,
        margin=dict(l=20, r=20, t=20, b=20),  # Reduce margins
        width=None,  # Let the iframe control width
        height=None, # Let the iframe control height
    )
    eu_projects_fig.write_html(
        "figures/biso/european_projects.html",
        include_plotlyjs="cdn",
        full_html=False,
        config={"responsive": True}
    )

.. container::

Journals
--------

.. code:: ipython3

    from dibisoplot.biso import Journals
    
    journals = Journals(
        entity_id="EM2C",
        year = 2023,
        **scanr_config,
    )
    
    journals_latex = journals.get_figure()
    
    print(journals_latex)

Journals in HAL
---------------

.. code:: ipython3

    from dibisoplot.biso import JournalsHal
    
    journals_hal = JournalsHal(
        entity_id="EM2C",
        year = 2023,
    )
    
    journals_hal_fig = journals_hal.get_figure()
    
    # journals_hal_fig.show()

.. code:: ipython3

    # This cell has the metadata: "nbsphinx": "hidden" to be hidden in the sphinx documentation
    
    journals_hal_fig.update_layout(
        autosize=True,
        margin=dict(l=20, r=20, t=20, b=20),  # Reduce margins
        width=None,  # Let the iframe control width
        height=None, # Let the iframe control height
    )
    journals_hal_fig.write_html(
        "figures/biso/journals_hal.html",
        include_plotlyjs="cdn",
        full_html=False,
        config={"responsive": True}
    )

.. container::

Open Access Works
-----------------

.. code:: ipython3

    from dibisoplot.biso import OpenAccessWorks
    
    oa_works = OpenAccessWorks(
        entity_id="EM2C",
        year = 2023,
    )
    
    oa_works_fig = oa_works.get_figure()
    
    # oa_works_fig.show()

.. code:: ipython3

    # This cell has the metadata: "nbsphinx": "hidden" to be hidden in the sphinx documentation
    
    oa_works_fig.update_layout(
        autosize=True,
        margin=dict(l=20, r=20, t=20, b=20),  # Reduce margins
        width=None,  # Let the iframe control width
        height=None, # Let the iframe control height
    )
    oa_works_fig.write_html(
        "figures/biso/open_access_works.html",
        include_plotlyjs="cdn",
        full_html=False,
        config={"responsive": True}
    )

.. container::

Private Sector Collaborations
-----------------------------

.. code:: ipython3

    from dibisoplot.biso import PrivateSectorCollaborations
    
    private_collabs = PrivateSectorCollaborations(
        entity_id="LGI",
        year = 2023,
        **scanr_config,
    )
    
    private_collabs_fig = private_collabs.get_figure()
    
    # private_collabs_fig.show()

.. code:: ipython3

    # This cell has the metadata: "nbsphinx": "hidden" to be hidden in the sphinx documentation
    
    private_collabs_fig.update_layout(
        autosize=True,
        margin=dict(l=20, r=20, t=20, b=20),  # Reduce margins
        width=None,  # Let the iframe control width
        height=None, # Let the iframe control height
    )
    private_collabs_fig.write_html(
        "figures/biso/private_collabs.html",
        include_plotlyjs="cdn",
        full_html=False,
        config={"responsive": True}
    )

.. container::

Works in BibTeX format
----------------------

.. code:: ipython3

    from dibisoplot.biso import WorksBibtex
    
    works = WorksBibtex(
        entity_id="EM2C",
        year = 2023,
    )
    
    works_latex = works.get_figure()
    
    # print the first lines of the bibtex string
    print(works_latex[:2000] + "...")

Works Type
----------

.. code:: ipython3

    from dibisoplot.biso import WorksType
    
    works_type = WorksType(
        entity_id="LGI",
        year = 2023,
    )
    
    works_type_fig = works_type.get_figure()
    
    # works_type_fig.show()

.. code:: ipython3

    # This cell has the metadata: "nbsphinx": "hidden" to be hidden in the sphinx documentation
    
    works_type_fig.update_layout(
        autosize=True,
        margin=dict(l=20, r=20, t=20, b=20),  # Reduce margins
        width=None,  # Let the iframe control width
        height=None, # Let the iframe control height
    )
    works_type_fig.write_html(
        "figures/biso/works_type.html",
        include_plotlyjs="cdn",
        full_html=False,
        config={"responsive": True}
    )

.. container::
