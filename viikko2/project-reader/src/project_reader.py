from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url
 
    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        parsed_content = toml.loads(content)

        name = parsed_content["tool"]["poetry"]["name"]
        description = parsed_content["tool"]["poetry"].get("description", "")
        license = parsed_content["tool"]["poetry"].get("license")

        authors = parsed_content["tool"]["poetry"]["authors"]

        dependecies = list(parsed_content["tool"]["poetry"]["dependencies"].keys())
        dev_dependencies = list(parsed_content["tool"]["poetry"]["group"]["dev"]["dependencies"].keys())

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, license, authors, dependecies, dev_dependencies)