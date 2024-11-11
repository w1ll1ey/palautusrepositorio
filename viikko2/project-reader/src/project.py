class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_items(self, items):
        return "\n- ".join(items) if len(items) > 0 else "-"


    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license}\n"
            f"\nAuthors: \n- {self._stringify_items(self.authors)}"
            f"\n\nDependencies: \n- {self._stringify_items(self.dependencies)}"
            f"\n\nDevelopment dependencies: \n- {self._stringify_items(self.dev_dependencies)}"
        )
