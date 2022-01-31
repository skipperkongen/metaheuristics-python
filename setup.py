from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    LONG_DESCRITPION = fh.read()

with open('requirements.txt') as fi:
    REQUIRE = [
        line.strip() for line in fi.readlines()
        if not line.startswith('#')
    ]

with open('LICENSE') as fi:
    LICENSE = fi.read()

setup(
    name='metaheuristics',
    author="Pimin Konstantin Kefalouks",
    author_email='skipperkongen@gmail.com',
    url="https://github.com/skipperkongen/metaheuristics-python",
    version="0.0.1",
    description="A repo for practicing metaheuristics.",
    long_description=LONG_DESCRITPION,
    long_description_content_type="text/markdown",
    license=LICENSE,
    install_requires=REQUIRE,
    extras_require={'test': ['pytest']},
    packages=find_packages('src'),
    package_dir={'': 'src'}
)
