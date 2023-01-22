#!/bin/bash


# Set flags
while getopts r: flag
do
    case "${flag}" in
        r) RELEASE_VERSION=${OPTARG};;
    esac
done


# Validate required arguments
REQUIRED_ENVS=("GH_TOKEN" "TEST_PYPI_USERNAME" "TEST_PYPI_PASSWORD" "PYPI_USERNAME" "PYPI_PASSWORD")
for env in "${REQUIRED_ENVS[@]}"; do
    echo "Checking $env"
    if [ -z "${!env}" ]; then
        echo "ERROR: $env is not set"
        exit 1;
    fi;
done


# Install requirements
pip install --upgrade -r requirements-release.txt


# Checkout master branch
git checkout master
git pull


# Set new version
VERSION_FILE_PATH='pytest_compare/__init__.py'
VERSION_REGEX='^(((__version__ = \")([[:digit:]]+.)*)([[:digit:]]+)((a|b|rc)[[:digit:]]*)?(.post[[:digit:]]+)?(.dev[[:digit:]]+)?(\"))$'
VERSION_TAG_REGEX='([[:digit:]]+.)*([[:digit:]]+)((a|b|rc)[[:digit:]]*)?(.post[[:digit:]]+)?(.dev[[:digit:]]+)?'

if [ -z "$RELEASE_VERSION" ];
then
  echo "No RELEASE_VERSION provided"
  NEW_MINOR=`sed -En "s/$VERSION_REGEX/\5/p" $VERSION_FILE_PATH | awk '{print $1 + 1}'`
  sed -Ei.bac "s/$VERSION_REGEX/\2$NEW_MINOR\"/" $VERSION_FILE_PATH
else
  echo "Found RELEASE_VERSION = $RELEASE_VERSION"
  if grep -Eo "$VERSION_REGEX" $VERSION_FILE_PATH
  then
    echo "Version is in a correct format"
    sed -Ei.bac "s/$VERSION_REGEX/\3$RELEASE_VERSION\"/" $VERSION_FILE_PATH
  else
    echo "No correct version found in $VERSION_FILE_PATH"
  exit 1
  fi
fi


# Print new version
export RELEASE_VERSION=`grep -Eio $VERSION_TAG_REGEX $VERSION_FILE_PATH`
echo "Created version: v$RELEASE_VERSION"


# Confirm release
while true; do
    read -p "Publish the package with the new version [y/n]? " yn
    case $yn in
        [Yy]* ) break;;
        [Nn]* ) exit;;
        * ) echo "Please answer 'y' or 'n'.";;
    esac
done


# Remove backup
rm $VERSION_FILE_PATH.bac


# Commit and push new version
git checkout -b "release-v$RELEASE_VERSION"
git commit -am $RELEASE_VERSION
git checkout master
git merge "release-v$RELEASE_VERSION"
git push https://$GH_TOKEN@github.com/IlyaMichlin/pytest-compare.git


# Build
python -m build


# Publish Test
twine upload dist/* --repository-url https://test.pypi.org/legacy/ --username $TEST_PYPI_USERNAME --password $TEST_PYPI_PASSWORDT


# Publish
twine upload dist/* --verbose --username $PYPI_USERNAME --password $PYPI_PASSWORDT


# Create Github Release
gh release create v$RELEASE_VERSION ./dist/* --title "v$RELEASE_VERSION" --notes "Release v$RELEASE_VERSION"
