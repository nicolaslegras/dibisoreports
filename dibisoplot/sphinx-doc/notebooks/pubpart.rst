PubPart
=======

Collaborations between Université Paris-Salcay and Stockholms Universitet
-------------------------------------------------------------------------

Those plots present collaborations between the Université Paris-Saclay
and Stockholms Universitet from 2020 to 2025 using data from OpenAlex.

For the Université Paris-Salcay, we use the OpenAlex Institution ID
I277688954 with its full ROR lineage (all the university’s child
structures).

For Stockholms Universitet, we use the OpenAlex Institution ID
I161593684 with its full ROR lineage (all the institution’s child
structures), the OpenAlex Publisher ID P4310320318 full lineage and the
OpenAlex Funder ID F4320325669. This means that works which are either
from author(s) from Stockholms Universitet, published by Stockholms
Universitet or funded by Stockholms Universitet will be included in the
analysis below.

To run this notebook, you need at least 10 GB of RAM. You can reduce the
year time frame for each plot if you want to reduce the memory
requirements.

| Romain THOMAS 2025
| DiBISO - Université Paris-Salcay

.. code:: ipython3

    # This cell has the metadata: "nbsphinx": "hidden" to be hidden in the sphinx documentation
    
    # Create figure directory
    
    import os
    
    os.makedirs("figures/pubpart", exist_ok=True)

OpenAlex Topics in works in collaboration
-----------------------------------------

.. code:: ipython3

    from dibisoplot.pubpart import TopicsCollaborations
    
    tc = TopicsCollaborations(
        "I277688954",
        year="2020-2025",
        language="en",
        entity_openalex_filter_field = "authorships.institutions.lineage",
        secondary_entity_id = ["I161593684", "P4310320318", "F4320325669"],
        secondary_entity_filter_field = [
            "authorships.institutions.lineage",
            "locations.source.publisher_lineage",
            "grants.funder"
        ]
    )
    
    tc_fig = tc.get_figure()

.. code:: ipython3

    # This cell has the metadata: "nbsphinx": "hidden" to be hidden in the sphinx documentation
    
    tc_fig.update_layout(
        autosize=True,
        width=None,  # Let the iframe control width
        height=None, # Let the iframe control height
    )
    tc_fig.write_html(
        "figures/pubpart/tc_fig.html",
        include_plotlyjs="cdn",
        full_html=False,
        config={"responsive": True}
    )

.. container::

OpenAlex topics identified as potential collaboration areas
-----------------------------------------------------------

.. code:: ipython3

    from dibisoplot.pubpart import TopicsPotentialCollaborations
    
    tpc = TopicsPotentialCollaborations(
        "I277688954",
        language="en",
        year="2020-2025",
        entity_openalex_filter_field = "authorships.institutions.lineage",
        secondary_entity_id = ["I161593684", "P4310320318", "F4320325669"],
        secondary_entity_filter_field = [
            "authorships.institutions.lineage",
            "locations.source.publisher_lineage",
            "grants.funder"
        ]
    )
    
    tpc_fig = tpc.get_figure()

.. code:: ipython3

    # This cell has the metadata: "nbsphinx": "hidden" to be hidden in the sphinx documentation
    
    tpc_fig.update_layout(
        autosize=True,
        width=None,  # Let the iframe control width
        height=None, # Let the iframe control height
    )
    tpc_fig.write_html(
        "figures/pubpart/tpc_fig.html",
        include_plotlyjs="cdn",
        full_html=False,
        config={"responsive": True}
    )

.. container::

Structures with the most collaborations in co-publications
----------------------------------------------------------

.. code:: ipython3

    from dibisoplot.pubpart import InstitutionsLineageCollaborations
    
    ilc = InstitutionsLineageCollaborations(
        "I277688954",
        year="2020-2025",
        language="en",
        entity_openalex_filter_field = "authorships.institutions.lineage",
        secondary_entity_id = ["I161593684", "P4310320318", "F4320325669"],
        secondary_entity_filter_field = [
            "authorships.institutions.lineage",
            "locations.source.publisher_lineage",
            "grants.funder"
        ]
    )
    
    ilc_fig = ilc.get_figure()

.. code:: ipython3

    # This cell has the metadata: "nbsphinx": "hidden" to be hidden in the sphinx documentation
    
    ilc_fig.update_layout(
        autosize=True,
        width=None,  # Let the iframe control width
        height=None, # Let the iframe control height
    )
    ilc_fig.write_html(
        "figures/pubpart/ilc_fig.html",
        include_plotlyjs="cdn",
        full_html=False,
        config={"responsive": True}
    )

.. container::

Works in collaboration
----------------------

Sorted by citation_normalized_percentile

.. code:: ipython3

    from dibisoplot.pubpart import WorksCollaborations
    
    wcn = WorksCollaborations(
        "I277688954",
        language="en",
        year="2020-2025",
        entity_openalex_filter_field = "authorships.institutions.lineage",
        secondary_entity_id = ["I161593684", "P4310320318", "F4320325669"],
        secondary_entity_filter_field = [
            "authorships.institutions.lineage",
            "locations.source.publisher_lineage",
            "grants.funder"
        ],
        metric="citation_normalized_percentile",
    )
    
    wnc_fig = wcn.get_figure()

.. code:: ipython3

    # This cell has the metadata: "nbsphinx": "hidden" to be hidden in the sphinx documentation
    
    wnc_fig.update_layout(
        autosize=True,
        width=None,  # Let the iframe control width
        height=None, # Let the iframe control height
    )
    wnc_fig.write_html(
        "figures/pubpart/wnc_fig.html",
        include_plotlyjs="cdn",
        full_html=False,
        config={"responsive": True}
    )

.. container::

Works in collaboration
----------------------

Sorted by cited_by_count

.. code:: ipython3

    from dibisoplot.pubpart import WorksCollaborations
    
    wcc = WorksCollaborations(
        "I277688954",
        language="en",
        year="2020-2025",
        entity_openalex_filter_field = "authorships.institutions.lineage",
        secondary_entity_id = ["I161593684", "P4310320318", "F4320325669"],
        secondary_entity_filter_field = [
            "authorships.institutions.lineage",
            "locations.source.publisher_lineage",
            "grants.funder"
        ],
        metric="cited_by_count",
        max_plotted_entities=50,
    )
    
    wcc_fig = wcc.get_figure()

.. code:: ipython3

    # This cell has the metadata: "nbsphinx": "hidden" to be hidden in the sphinx documentation
    
    wcc_fig.update_layout(
        autosize=True,
        width=None,  # Let the iframe control width
        height=None, # Let the iframe control height
    )
    wcc_fig.write_html(
        "figures/pubpart/wcc_fig.html",
        include_plotlyjs="cdn",
        full_html=False,
        config={"responsive": True}
    )

.. container::
