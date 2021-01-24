from setuptools import setup
import json

with open("Pipfile.lock") as f:
    all_dependencies = json.load(f)


def get_dependencies(section):
    """Look through the 'Pipfile.lock' to fetch requirements by section."""
    return [
        package + detail.get("version", "")
        for package, detail in all_dependencies.get(section, {}).items()
    ]


setup(
    install_requires=get_dependencies("default"),
    extras_require={"dev": get_dependencies("develop")},
)
