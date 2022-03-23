#!/usr/bin/env bash

PYPI_ZIP=$(find dist/*.whl | sort -r | head -1)

if [ -z "${PYPI_ZIP}" ]; then
  echo "You must package the library. Use the script 'setup.sh'"

elif ! pip freeze | grep -q twine; then
  echo "You must install the twine library. Use the 'install_req.sh' script"

else

  echo -n "Do you want to upload the '${PYPI_ZIP}' file to Nexus (y/n)? "
  read answer

  if [ "$answer" != "${answer#[Yy]}" ] ;then
    echo "Uploading ..."
    twine upload -r pypi "${PYPI_ZIP}"
    echo "Done!"
  else
    echo "Nothing to do..."
  fi

fi

exit 0
