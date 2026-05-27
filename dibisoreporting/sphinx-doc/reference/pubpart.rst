PubPart
=======
Class to generate the PubPart report.

By default the report contains the following visualizations:
* InstitutionsLineageCollaborations
* TopicsCollaborations
* TopicsPotentialCollaborations
* WorksCollaborations: name = "citationsnormalized", metric = "citationsnormalized"
* WorksCollaborations: name = "citationscount", metric = "cited_by_count"

This comes from the default value of ``default_visualizations`` :

.. code-block:: python

    default_visualizations = {
        "InstitutionsLineageCollaborations": [{}],
        "TopicsCollaborations": [{}],
        "TopicsPotentialCollaborations": [{}],
        "WorksCollaborations": [
            {
                "name": "citationsnormalized",
                "metric": "citation_normalized_percentile"
            },
            {
                "name": "citationscount",
                "metric": "cited_by_count"
            },
        ],
    }

The PubPart Class
-----------------
.. autoclass:: dibisoreporting.pubpart.PubPart
   :members:
   :show-inheritance:
   :inherited-members:
   :undoc-members:
