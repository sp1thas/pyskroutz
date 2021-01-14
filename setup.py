from distutils.core import setup
import json

with open('Pipfile.lock') as f:
    all_dependencies = json.load(f)


def get_dependencies(section):
    """Look through the 'Pipfile.lock' to fetch requirements by section."""
    return [package + detail.get('version', "")
            for package, detail in all_dependencies.get(section, {}).items()]


setup(
    name="pyskroutz",
    packages=["src/pyskroutz"],
    version="0.0.1.4",
    description=(
        "Unofficial Python SDK for Skroutz.gr API. This client library is designed to support the Skroutz API. "
        "You can read more about the Skroutz API by accessing its official documentation."
    ),
    author="Panagiotis Simakis",
    license="GPLv3",
    author_email="sp1thas@autistici.org",
    url="https://github.com/sp1thas/pyskroutz",
    keywords=["skroutz", "api"],
    classifiers=[],
    install_requires=get_dependencies('default'),
    extras_require={
        'dev': get_dependencies('develop')
    }
)
