#!/user/bin/sh

python3 setup.py sdist
pip install ./dist/my_minipack-1.0.0.tar.gz
