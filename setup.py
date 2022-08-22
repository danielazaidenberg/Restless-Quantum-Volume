# This code is part of Qiskit.
#
# (C) Copyright IBM 2017.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"Qiskit experiment extension setup file."

import os
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    REQUIREMENTS = f.read().splitlines()


version_path = os.path.abspath(
        os.path.join(
            os.path.join(os.path.dirname(__file__), 'restless_quantum_volume'),
        'VERSION.txt'))
with open(version_path, 'r') as fd:
    version = fd.read().rstrip()

# Read long description from README.
README_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                           'README.md')
with open(README_PATH) as readme_file:
    README = readme_file.read()

setup(
    name="Restless Quantum Volume",
    version=version,
    description="A restless quantum volume experiment with restless analysisnd restless mixin for quantum volume",
    long_description=README,
    long_description_content_type='text/markdown',
    url="https://github.com/danielazaidenberg/Restless Quantum Volume",
    author="Daniela Zaidenberg and Will Shanks",
    author_email="Daniela.Zaidenberg@ibm.com and Will.Shanks@ibm.com",
    license="Apache 2.0",
    classifiers=[
        "Environment :: Console",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering",
    ],
    keywords="qiskit experiments",
    packages=find_packages(exclude=['test*']),
    install_requires=REQUIREMENTS,
    include_package_data=True,
    python_requires=">=3.7",
    zip_safe=False
)
