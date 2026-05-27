import copy
from datetime import datetime

from dibisoplot.pubpart import InstitutionsLineageCollaborations
from dibisoplot.pubpart import TopicsCollaborations
from dibisoplot.pubpart import TopicsPotentialCollaborations
from dibisoplot.pubpart import WorksCollaborations

from dibisoreporting import DibisoReporting

from dibisoreporting.utils import escape_for_latex

from dibisoplot._version import __version__ as dibisoplot_version
from dibisoreporting._version import __version__ as dibisoreporting_version


class PubPart(DibisoReporting):
    """
    Class to generate the PubPart report

    :cvar class_mapping: Dictionary that maps class names to actual classes
    :cvar default_plot_main_color: Default color for the main plot (#004e7d)
    :cvar default_visualizations: Dictionary contains each type of plot to include in the report with the parameters of
        each plot.
    """

    # Map class names to actual classes
    class_mapping = {
        "InstitutionsLineageCollaborations": InstitutionsLineageCollaborations,
        "TopicsCollaborations": TopicsCollaborations,
        "TopicsPotentialCollaborations": TopicsPotentialCollaborations,
        "WorksCollaborations": WorksCollaborations,
    }

    default_plot_main_color = "#004e7d"

    # an empty list means that the visualization won't be done, an empty dictionary in a list means that the
    # visualization will be done with the default values
    default_visualizations =  {
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


    def __init__(
            self,
            entity_id: str,
            year: int | str | None = None,
            entity_openalex_filter_field: str = "authorships.institutions.lineage",
            secondary_entity_id: str | list[str] | None = None,
            secondary_entity_filter_field: str | list[str] | None = "authorships.institutions.lineage",
            entities_acronym: str = "",
            entities_full_name: str = "",
            latex_main_file_path: str | None = None,
            latex_main_file_url: str | None = None,
            latex_biblio_file_path: str | None = None,
            latex_biblio_file_url: str | None = None,
            latex_template_path: str | None = None,
            latex_template_url: str | None = None,
            max_entities: int | None = 100000,
            max_plotted_entities: int = 25,
            plot_main_color: str | None = None,
            root_path: str | None = None,
            watermark_text: str = "",
            **kwargs
    ):
        """
        Initialize the PubPart class with the given parameters.

        :param entity_id: The HAL collection identifier. This usually refers to the entity acronym.
        :type entity_id: str
        :param year: The year for which to fetch data. If None, uses the current year.
        :type year: int | str | None, optional
        :param entity_openalex_filter_field: Field to filter on in the OpenAlex API.
            Default to 'authorships.institutions.lineage'.
            The list of possible values can be found in the OpenAlex documentation:
            https://docs.openalex.org/api-entities/works/filter-works
        :type entity_openalex_filter_field: str, optional
        :param secondary_entity_id: The OpenAlex ID for the secondary entity or entities to analyze the topics of
            collaborations. If a work is present in several entities, it is counted only once.
        :type secondary_entity_id: str | list[str] | None, optional
        :param secondary_entity_filter_field: The OpenAlex filter field for the secondary entity or entities. If None,
            use the same as for the main entity. If a single string is provided, it is used for all secondary entities.
        :type secondary_entity_filter_field: str | list[str] | None, optional
        :param entities_acronym: The acronym of the entities.
        :type entities_acronym: str
        :param entities_full_name: The full name of the entities.
        :type entities_full_name: str
        :param latex_main_file_path: Path to a single LaTeX main file. This file is the one to use to compile the
            report. It will copy the main file to root_path. Default to None. If None, doesn't try getting the main file
            from the path. If both latex_main_file_path and latex_main_file_url are not None, the library will first try
            to get the main file from the path.
        :type latex_main_file_path: str | None, optional
        :param latex_main_file_url: URL to download a single LaTeX main file. It will download the file directly
            to root_path. Default to None. If None, doesn't try getting the main file from the URL.
        :type latex_main_file_url: str | None, optional
        :param latex_biblio_file_path: Path to a single LaTeX biblio file. This file is the one to use to compile the
            bibliography. It will copy the biblio file to root_path. Default to None. If None, doesn't try getting the
            biblio file from the path. If both latex_biblio_file_path and latex_biblio_file_url are not None, the
            library will first try to get the biblio file from the path.
        :type latex_biblio_file_path: str | None, optional
        :param latex_biblio_file_url: URL to download a single LaTeX biblio file. It will download the file directly
            to root_path. Default to None. If None, doesn't try getting the biblio file from the URL.
        :type latex_biblio_file_url: str | None, optional
        :param latex_template_path: Path to the LaTeX template files. It will copy the templates files to root_path.
            Default to None. If None, doesn't try getting the template from the path. If both latex_template_path and
            latex_template_url are not None, the library will first try to get the template from the path.
        :type latex_template_path: str | None, optional
        :param latex_template_url: URL to a GitHub repository containing the template. It will get the latest repository
            release and extract it to get the template files. Default to None. If None, doesn't try getting the template
            from the URL.
        :type latex_template_url: str | None, optional
        :param max_entities: Default maximum number of entities used to create the plot. Default 1000.
            Set to None to disable the limit. This value limits the number of queried entities when doing analysis.
            For example, when creating the collaboration map, it limits the number of works to query from HAL to extract the
            collaborating institutions from.
        :type max_entities: int | None, optional
        :param max_plotted_entities: Maximum number of bars in the plot or rows in the table. Default to 25.
        :type max_plotted_entities: int, optional
        :param plot_main_color: Main color used in the plots. Default to "blue". Plotly color.
        :type plot_main_color: str, optional
        :param root_path: Path to the root directory where the report and figures will be generated.
        :type root_path: str
        :param watermark_text: The text to be used as a watermark in the report. Default to "" (no watermark).
        :type watermark_text: str
        """

        super().__init__(
            entity_id,
            year,
            latex_main_file_path=latex_main_file_path,
            latex_main_file_url=latex_main_file_url,
            latex_biblio_file_path=latex_biblio_file_path,
            latex_biblio_file_url=latex_biblio_file_url,
            latex_template_path=latex_template_path,
            latex_template_url=latex_template_url,
            max_entities=max_entities,
            max_plotted_entities=max_plotted_entities,
            plot_main_color=plot_main_color,
            root_path = root_path
        )

        self.entity_openalex_filter_field = entity_openalex_filter_field
        self.secondary_entity_id = secondary_entity_id
        self.secondary_entity_filter_field = secondary_entity_filter_field
        self.entities_acronym = entities_acronym
        self.entities_full_name = entities_full_name
        self.watermark_text = watermark_text

        self.data_fetch_date = datetime.now().strftime("%d/%m/%Y")

        self.kwargs = kwargs


    def generate_report(
            self,
            visualizations_to_make: dict[str, list[dict]] | None = None,
            import_default_visualizations = True
    ):
        """
        Generate the report by calling the specified functions with their parameters to create the desired
        visualizations. To select which visualization to make and configure them, you can use `visualizations_to_make`
        as follows:

        .. code-block:: python

            visualizations_to_make = {
                "PubInstitutions": [
                    { "name": "PubInstitutions1", "param1": "value1", "param2": "value2" },
                    { "name": "PubInstitutions2", "param1": "value3", "param2": "value4" }
                ],
                "InstitutionsLineageCollaborations": [
                    { "name": "ilc", "param1": "value1", "param2": "value2" }
                ],
                "TopicsCollaborations": [
                    {}
                ],
                "TopicsPotentialCollaborations": []
            }

        This example, will create:
          * 2 PubInstitutions visualizations (with the parameters defined in the dictionaries)
          * 1 InstitutionsLineageCollaborations visualization (with the parameters defined in the dictionary)
          * 1 TopicsCollaborations visualizations
          * 0 TopicsPotentialCollaborations visualizations (as the list is empty)

        :param visualizations_to_make: A dictionary specifying which visualizations to make and their parameters.
        :type visualizations_to_make: list[dict[str, Any]]
        :param import_default_visualizations: Whether to import default visualizations settings. Defaults to True.
            To not generate a plot, set its dictionary in import_default_visualizations to an empty list.
            Example: If you don't want to generate the Conferences visualization, you can set
            import_default_visualizations as follows: ``import_default_visualizations = {"Conferences": []}``.
        :type import_default_visualizations: bool
        """

        # TODO: check that the IDs exist

        # create a copy to modify the default visualizations to set entity_openalex_filter_field,
        # secondary_entity_id and secondary_entity_filter_field
        self.default_visualizations = copy.deepcopy(PubPart.default_visualizations)
        for viz_type_val in self.default_visualizations.values():
            for viz in viz_type_val:
                viz["entity_openalex_filter_field"] = self.entity_openalex_filter_field
                viz["secondary_entity_id"] = self.secondary_entity_id
                viz["secondary_entity_filter_field"] = self.secondary_entity_filter_field

        self.add_marco("reportyear", escape_for_latex(str(self.year)))
        self.add_marco("entitiesacronym", escape_for_latex(self.entities_acronym))
        self.add_marco("entitiesfullname", escape_for_latex(self.entities_full_name))
        self.add_marco("datafetchdate", escape_for_latex(self.data_fetch_date))
        self.add_marco("watermarktext", escape_for_latex(self.watermark_text))
        self.macros.append("")
        self.add_marco("dibisoplotversion", escape_for_latex(dibisoplot_version))
        self.add_marco("dibisoreportingversion", escape_for_latex(dibisoreporting_version))
        self.macros.append("")

        super().generate_report(visualizations_to_make, import_default_visualizations)


