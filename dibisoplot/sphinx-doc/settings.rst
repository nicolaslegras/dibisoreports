Settings
========

To generate plots, provide a HAL collection identifier for the BiSO or an OpenAlex ID for the PubPart.
If the ``year`` is not specified, the current year is used.

BiSO example
------------

To plot the top conferences attended by Université Paris-Saclay researchers:

.. code-block:: python

    from dibisoplot.biso import Conferences

    conf = Conferences(
        entity_id = "UNIV-PARIS-SACLAY"
    )

    conf_fig = conf.get_figure()

    conf_fig.show()



BiSO plots with scanR
---------------------

For some plots, you will need to provide API credentials to access to the scanR API :

.. code-block:: python

    from dibisoplot.biso import PrivateSectorCollaborations

    private_collabs = PrivateSectorCollaborations(
        entity_id = "LGI",
        year = 2023,
        scanr_api_password = "",
        scanr_api_url = "",
        scanr_api_username = "",
        scanr_publications_index = "",
    )

    private_collabs_fig = private_collabs.get_figure()

    private_collabs_fig.show()

Customize the layout
--------------------

You can customize the plot's layout by using arguments available in the class or by directly applying layout to the
plotly figure:

.. code-block:: python

    from dibisoplot.biso import Conferences

    conf = Conferences(
        entity_id = "UNIV-PARIS-SACLAY",
        max_plotted_entities = 10,
        title = "Top conferences",
        main_color = "green"
    )

    conf_fig = conf.get_figure()

    # Update the plotly figure layout
    conf_fig.update_layout(
        margin = dict(l=50, r=50, b=100, t=100, pad=4),
        height = 400
    )

    conf_fig.show()


For a full list of available arguments, refer to the class reference and __init__ arguments.
