# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    setup.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vafleith <vafleith@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/03/15 00:49:02 by vafleith          #+#    #+#              #
#    Updated: 2024/03/15 01:02:59 by vafleith         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from setuptools import setup, find_packages

setup(
    name="my_minipack",
    version="1.0.0",
    description="Howto create a package in python.",
    url="None",
    author="vafleith",
    author_email="vafleith@student.42.fr",
    license="GPLv3",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Students",
        "Topic :: Education",
        "Topic :: HowTo",
        "Topic :: Package",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
    ],
    packages=find_packages()
)
