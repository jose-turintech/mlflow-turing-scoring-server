#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ────────────────────────────────────────── imports ────────────────────────────────────────── #
import os
import sys

from pkg_resources import parse_requirements
from setuptools import find_packages, setup

from src import __about__

# ───────────────────────────────────────────────────────────────────────────────────────────── #
# ─── Utils
# ───────────────────────────────────────────────────────────────────────────────────────────── #

here = os.path.abspath(os.path.dirname(__file__))


def read_about():
    _about = {}
    with open(__about__.__file__) as fp:
        exec(fp.read(), _about)
    return _about


def read(rel_path):
    """ Read the indicated file with relative path """
    with open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()


def get_requirements(file: str):
    """
    Reads package dependencies and returns a list of requirement. e.g. ['django==1.5.1', 'mezzanine==1.4.6']
    """
    file_path = os.path.join(here, file)
    with open(str(file_path)) as fp:
        return [str(r) for r in parse_requirements(fp)]


def get_python_requires():
    python_requires = "3.8"
    try:
        float(python_requires)
    except ValueError:
        return python_requires
    return f">={python_requires}"


# ───────────────────────────────────────────────────────────────────────────────────────────── #
# ─── Definitions
# ───────────────────────────────────────────────────────────────────────────────────────────── #

about = read_about()

setup_description_file = 'README.md'

setup_package_dir = 'src'

requirements = get_requirements(file='setup/requirements.txt')
tests_requirements = get_requirements(file='setup/requirements_develop.txt')

readme = read(rel_path='README.md')
history = read(rel_path='CHANGES').replace('.. :changelog:', '')

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

if sys.argv[-1] == 'info':
    for k, v in about.items():
        print('%s: %s' % (k, v))
    sys.exit()

# ───────────────────────────────────────────────────────────────────────────────────────────── #
# ─── Setup
# ───────────────────────────────────────────────────────────────────────────────────────────── #
setup(
    name=about['__project_name__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=f"{readme}\n\n{history}",
    long_description_content_type="text/markdown",
    author=about['__author__'],
    author_email=about['__email__'],
    url="https://github.com/turintech/mlflow-turing-scoring-server",

    license=about['__license__'],

    # Distribute the code as python binary libraries (pyd)
    build_with_nuitka=False,

    # Classifiers help users find your project by categorizing it.
    #
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 0.0.0 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        # 'Topic :: Topic 1 :: Topic2',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate you support Python 3. These classifiers are *not*
        # checked by 'pip install'. See instead 'python_requires' below.
        'Programming Language :: Python :: 3.8',
    ],

    # This field adds keywords for your project which will appear on the
    # project page. What does your project relate to?
    #
    # Note that this is a list of additional keywords, separated
    # by commas, to be used to assist searching for the distribution in a
    # larger catalog.
    keywords=about['__title__'],  # Optional

    # When your source code is in a subdirectory under the project root, e.g.
    # `src/`, it is necessary to specify the `package_dir` argument.
    # package_dir={'': 'metaml'},  # Optional

    # You can just specify package directories manually here if your project is
    # simple. Or you can use find_packages().
    #
    # Alternatively, if you just want to distribute a single Python file, use
    # the `py_modules` argument instead as follows, which will expect a file
    # called `my_module.py` to exist:
    #
    #   py_modules=["my_module"],
    #
    # packages=find_packages(where='metaml.*'),  # Required
    packages=find_packages(
        where=setup_package_dir
    ),
    package_dir={
        '': setup_package_dir
    },

    # Add the data files included in the "/src" packages
    package_data={
        # "/src/*"
        "mlflow_turing_scoring_server": ["scoring_server/nginx.conf"]
    },

    scripts=[
    ],

    # Specify which Python versions you support. In contrast to the
    # 'Programming Language' classifiers above, 'pip install' will check this
    # and refuse to install the project if the version does not match. See
    # https://packaging.python.org/guides/distributing-packages-using-setuptools/#python-requires
    python_requires=get_python_requires(),

    # This field lists other packages that your project depends on to run.
    # Any package you put here will be installed by pip when your project is
    # installed, so they must be valid existing projects.
    #
    # For an analysis of "install_requires" vs pip's requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=requirements,  # Optional

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # `pip` to create the appropriate form of executable for the target
    # platform.
    #
    # For example, the following would provide a command called `sample` which
    # executes the function `main` from this package when invoked:
    # entry_points={  # Optional
    #     'console_scripts': [
    #         'main=main:main',
    #     ],
    # },
)
