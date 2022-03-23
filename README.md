# mlflow_turin_scoring_server

Description of your python library project

## Description _[TODO]_

What your project can do specifically?

Provide context and add a link to any reference visitors might be unfamiliar with. A list of Features, or a Background
subsection can also be added here.

### Prerequisites

- python

## Useful scripts

- [Makefile](setup/Makefile): This file defines a set of tasks to be executed using the `make` utility.

    ```commandline
    (env-py38-mlflow-turing-scoring-server) user@pc:~/mlflow-turing-scoring-server$ make
     Usage: make <task>
       task options:
            help                           This help.
            clean-dist                     Remove 'dist' folder.
            clean-build                    Remove construction artifacts, except 'dist' folder.
            clean-pyc                      Remove Python file artifacts.
            req-install-dev                Install only development requirements in the activated local environment
            req-install                    Install the required libraries.
            req-remove                     Uninstall all the libraries installed in the Python environment.
            req-clean                      Remove all items from the pip cache.
            lint                           Check style with flake8 and pylint.
            test                           Run tests quickly with the default Python.
            sdist                          Package as .tar.gz.
            bdist                          Package as .whl (recommended).
    ```

- [**upload.sh**](upload.sh): Script to upload the packaging to the PyPI repository on the Nexus server.

    ```commandline
    (env-py38-mlflow-turing-scoring-server) user@pc:~/mlflow-turing-scoring-server$ ./upload.sh
    ```

  In order to upload, you must have previously configured your machine to be able to perform "Uploading PyPI Packages"
  (https://help.sonatype.com/repomanager3/formats/pypi-repositories).

  On the other hand, you must also have installed the requirements in the Python environment (`make req-install-dev`)
  and generated the packaging (`make bdist`).

## Usage _[TODO]_

## Configuration

The values indicated as an example in each of the variables is the value that will be taken by default if you do not
specify that variable in the file '.env'

#### Logging configuration

For more details, see [loguru](https://loguru.readthedocs.io/en/stable/api/logger.html)

| Variable              | Description                                                     | Default value             |
| --------------------- | --------------------------------------------------------------- | ------------------------- |
| LOGGER_ENABLE         | Flag that indicates whether the logging configuration should be initialized (true) or, if on the contrary, this configuration is already supposed to be initialized (false) | false |
| LOGGER_SINK           | Path to the log file                               | /tmp/mlflow-turing-scoring-server/logs/mlflow_turing_scoring_server.log |
| LOGGER_LEVEL          | The minimum severity level from which logged messages should be sent to the sink. <br> - Options: `critical, error, warning, success, info, debug, trace` | INFO |
| LOGGER_ROTATION       | A condition indicating whenever the current logged file should be closed and a new one started. | "12:00"  # New file is created each day at noon |
| LOGGER_RETENTION      | A directive filtering old files that should be removed during rotation or end of program. | "1 month" |

### Basic development steps

1) **Activate a Python virtual environment**: `conda activate env-py38`

    ```commandline
    user@pc:~/mlflow-turing-scoring-server$ conda activate env-py38
    (env-py38) user@pc:~/user/mlflow-turing-scoring-server$ 
    ```

2) **Install the project requirements**: `make req-install`

    ```commandline
    (env-py38) user@pc:~/user/mlflow-turing-scoring-server$ make req-install 
    make[1]: Entering directory '/home/user/mlflow-turing-scoring-server'
    ──────────────────────────────────────────────────────────────────────────────────────────────────────────
    ─── Install requirements: requirements.txt requirements_develop.txt 
    ──────────────────────────────────────────────────────────────────────────────────────────────────────────
   
    [...]
   
    pip freeze > /home/user/mlflow-turing-scoring-server/setup/requirements_freeze.txt
    make[1]: Leaving directory '/home/user/mlflow-turing-scoring-server'
    ```

3) **Check the quality of the code**: `make lint`

    ```commandline
    (env-py38) user@pc:~/user/mlflow-turing-scoring-server$ make lint
    
    ────────────────────────────────────────────────────────────────────────────────────────────────────────────
    ─── Checking the project code style [flake8]
    ────────────────────────────────────────────────────────────────────────────────────────────────────────────
    
    ────────────────────────────────────────────────────────────────────────────────────────────────────────────
    ─── Checking the project code style [pylint]
    ────────────────────────────────────────────────────────────────────────────────────────────────────────────
    
    --------------------------------------------------------------------
    Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
    ```

4) **Running the tests**: `make test`

    ```commandline
    (env-py38) user@pc:~/user/mlflow-turing-scoring-server$ make test
    =================================================================================== test session starts ===================================================================================
    platform linux -- Python 3.8.11, pytest-6.1.2, py-1.10.0, pluggy-0.13.1 -- /home/user/.conda/envs/env-py38/bin/python
    rootdir: /home/user/mlflow-turing-scoring-server/src/mlflow_turing_scoring_server/tests, configfile: pytest.ini
    plugins: cov-2.12.1
    collected 7 items                                                                                                                                                                                                                                               
    
    tests_library_template/tests_conf/test_conf_manager.py::TestConfManager::test_init PASSED                                                                        [ 14%]
    tests_library_template/tests_conf/test_conf_manager.py::TestConfManager::test_update_conf_mgr PASSED                                                             [ 28%]
    tests_library_template/tests_conf/test_conf_manager.py::TestConfManager::test_library_paths PASSED                                                               [ 42%]
    tests_library_template/tests_conf/test_conf_manager.py::TestConfManager::test_logging_conf PASSED                                                                [ 57%]
    tests_library_template/tests_conf/test_data_conf.py::TestDataConf::test_default_data_conf PASSED                                                                 [ 71%]
    tests_library_template/tests_conf/test_data_conf.py::TestDataConf::test_env_data_conf PASSED                                                                     [ 85%]
    tests_library_template/tests_conf/test_data_conf.py::TestDataConf::test_data_conf_factory PASSED                                                                 [100%]
    
    ---------- coverage: platform linux, python 3.8.11-final-0 -----------
    Name                                                                                                            Stmts   Miss Branch BrPart  Cover
    -------------------------------------------------------------------------------------------------------------------------------------------------
    /home/user/mlflow-turing-scoring-server/src/mlflow_turing_scoring_server/src/library_template/__init__.py                0      0      0      0   100%
    /home/user/mlflow-turing-scoring-server/src/mlflow_turing_scoring_server/src/library_template/conf/__init__.py           0      0      0      0   100%
    /home/user/mlflow-turing-scoring-server/src/mlflow_turing_scoring_server/src/library_template/conf/conf_manager.py      46      4      8      1    91%
    /home/user/mlflow-turing-scoring-server/src/mlflow_turing_scoring_server/src/library_template/conf/data_conf.py         13      0      2      0   100%
    /home/user/mlflow-turing-scoring-server/src/mlflow_turing_scoring_server/src/library_template/conf/logger_conf.py       28      1      0      0    96%
    /home/user/mlflow-turing-scoring-server/src/mlflow_turing_scoring_server/src/library_template/main.py                   18     18      2      0     0%
    -------------------------------------------------------------------------------------------------------------------------------------------------
    TOTAL                                                                                                             105     23     12      1    78%
    Coverage HTML written to dir ../docs/coverage
    
    
    =================================================================================== 7 passed in 0.21s ===================================================================================

    ```

   > **NOTE:**
   >
   > Note that if you want to run the tests in debug mode in pycharm, you should disable the coverage
   > in [pytest.ini](./tests/pytest.ini). Otherwise, the execution will not stop at the checkpoints.
   >
   > https://pytest-cov.readthedocs.io/en/latest/debuggers.html

5) **Verification that the log files are generated**: `ls /tmp/mlflow-turing-scoring-server/logs/`

    ```commandline
    (env-py38) user@pc:~/user/mlflow-turing-scoring-server$ ls /tmp/mlflow-turing-scoring-server/logs/
    mlflow_turing_scoring_server.log
    (env-py38) user@pc:~/user/mlflow-turing-scoring-server$
    ```

6) **Library packaging**: `make bdist`

    ```commandline
    (env-py38) user@pc:~/user/mlflow-turing-scoring-server$ make bdist
    
    ────────────────────────────────────────────────────────────────────────────────────────────────────────────
    ─── Setup bdist_wheel
    ────────────────────────────────────────────────────────────────────────────────────────────────────────────
    running clean
    'build/lib' does not exist -- can't clean it
    'build/bdist.linux-x86_64' does not exist -- can't clean it
    'build/scripts-3.8' does not exist -- can't clean it
    running bdist_wheel
    running build
    running build_py
    creating build
    creating build/lib
    creating build/lib/library_template
        [...]
    creating 'dist/mlflow_turing_scoring_server-0.0.0-py3-none-any.whl' and adding 'build/bdist.linux-x86_64/wheel' to it
        [...]
    make[1]: Entering directory '/home/user/mlflow-turing-scoring-server/src/mlflow_turing_scoring_server'
    make[1]: Leaving directory '/home/user/mlflow-turing-scoring-server/src/mlflow_turing_scoring_server'
    
    total 12
    -rw------- 1 user developers 12121 Aug  3 15:55 mlflow_turing_scoring_server-0.0.0-py3-none-any.whl
    ```

    ```commandline
    (env-py38) user@pc:~/user/mlflow-turing-scoring-server$ ls
    AUTHORS.md  CHANGES  dist  LICENSE  Makefile  MANIFEST.in  README.md  setup  setup.py  src  tests  upload.sh
    (env-py38) user@pc:~/user/mlflow-turing-scoring-server$ ls dist/
    mlflow_turing_scoring_server-0.0.0-py3-none-any.whl
    ```

    - **With Nuitka disabled**: The generated compress should have a structure like the following:

         ```commandline
         mlflow_turing_scoring_server-0.0.0-py3-none-any.whl
         ├── mlflow_turing_scoring_server
         │   ├── conf
         │   │   ├── base_default_conf.py
         │   │   ├── conf_manager.py
         │   │   ├── data_conf.py
         │   │   ├── __init__.py
         │   │   └── logger_conf.py
         │   ├── __init__.py
         │   └── main.py
         └── mlflow_turing_scoring_server-0.0.0.dist-info
             ├── AUTHORS.md
             ├── LICENSE
             ├── METADATA
             ├── RECORD
             ├── top_level.txt
             └── WHEEL
         ```

      **NOTE**: With this configuration, **all** the code is **accessible** once the library is installed.

    - **With Nuitka enabled**: The generated compress contains the python binary library, and it should have a structure
      like the following:

         ```commandline
         mlflow_turing_scoring_server-0.0.0-py3-none-any.whl
         ├── mlflow_turing_scoring_server-0.0.0.dist-info
         │   ├── AUTHORS.md
         │   ├── LICENSE
         │   ├── METADATA
         │   ├── RECORD
         │   ├── top_level.txt
         │   └── WHEEL
         ├── mlflow_turing_scoring_server.cpython-37m-x86_64-linux-gnu.so
         └── mlflow_turing_scoring_server.pyi
         ```

      **NOTE**: With this configuration, **only** the structures **specified** in the
      [mlflow_turing_scoring_server/\_\_init__.py](./src/mlflow_turing_scoring_server/__init__.py) file **can be
      accessed** after the library is installed

7) **Upload the packaging to the PyPI repository on the Nexus server**:

    - Give execution permission to the script:

        ```commandline
        (env-py38) user@pc:~/user/mlflow-turing-scoring-server$ chmod 777 upload.sh
        ```

    - These are the messages that you will see if you **accept** the upload:

        ```commandline 
        (env-py38) user@pc:~/user/mlflow-turing-scoring-server$ ./upload.sh 
        Do you want to upload the 'dist/mlflow_turing_scoring_server-0.0.0-py3-none-any.whl' file to Nexus (y/n)? y
        Uploading ...
        Done!
        ```

    - These are the messages that you will see if you **reject** the upload::

        ```commandline 
        (env-py38) user@pc:~/user/mlflow-turing-scoring-server$ ./upload.sh 
        Do you want to upload the 'dist/mlflow_turing_scoring_server-0.0.0-py3-none-any.whl' file to Nexus (y/n)? n
        Nothing to do...
        ```

8) **Installation of the new library**: To install the library you have 2 options:

    1) Install it directly using the packed file:

        ```commandline
        (new-environment) user@pc:~/user/mlflow-turing-scoring-server$ pip install ./dist/mlflow_turing_scoring_server-0.0.0-py3-none-any.whl
        ```

    1) Install it from the Python repository:

        ```commandline
        (new-environment) user@pc:~/user/mlflow-turing-scoring-server$ pip install mlflow-turing-scoring-server
        ```
