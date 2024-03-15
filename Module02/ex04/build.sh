#!/bin/bash
#python3 -m venv temp_env && source temp_env/bin/activate
#./build.sh
#ls dist
#pip list
#pip show -v my_minipack
#deactivate
#rm -rf temp_env dist my_minipack.egg-info
python3 setup.py sdist
pip install ./dist/my_minipack-1.0.0.tar.gz
