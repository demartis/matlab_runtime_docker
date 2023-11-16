#  Copyright (c) 2020-2023 Riccardo De Martis
#  MIT License
#  All Trademarks referred to are the property of their respective owners.

import os

FILE_LATEST = 'latest'
FILE_LATEST_M = 'latest-meshlab'

builds = [
    ['R2019a', 'v9.6',  9, '2023-May-11'],
    ['R2019b', 'v9.7',  9, '2023-May-11'],
    ['R2020a', 'v9.8',  8, '2023-May-11'],
    ['R2020b', 'v9.9',  8, '2023-May-11'],
    ['R2021a', 'v9.10', 8, '2023-May-11'],
    ['R2021b', 'v9.11', 7, '2023-Nov-14'],
    ['R2022a', 'v9.12', 7, '2023-Nov-14'],
    ['R2022b', 'v9.13', 7, '2023-Nov-14'],
    ['R2023a', 'v9.14', 5, '2023-Nov-14'],
    ['R2023b', 'v23.2', 3, '2023-Nov-14'],
]


def gen_dockerfile(vers, named_vers, date, update_vers, ld_lib_ver):
    dockerfile = f"""
# MATLAB Compiler Runtime (MCR) {vers} ({named_vers})  
#  
# This docker file will configure an environment into which the Matlab compiler
# runtime will be installed and in which stand-alone matlab routines (such as
# those created with MATLAB's deploytool) can be executed.  

# MATLAB Runtime  
# Run compiled MATLAB applications or components without installing MATLAB  
# The MATLAB Runtime is a standalone set of shared libraries that enables the  
# execution of compiled MATLAB applications or components. When used together,  
# MATLAB, MATLAB Compiler, and the MATLAB Runtime enable you to create and distribute  
# numerical applications or software components quickly and securely.  
#  
# See https://www.mathworks.com/products/compiler/matlab-runtime.html for more info.  
#  
# @author Riccardo De Martis{date}  
# @link https://github.com/demartis/matlab_runtime_docker  
#  

FROM debian:buster-slim  
MAINTAINER Riccardo De Martis <riccardo@demartis.it>  
ENV DEBIAN_FRONTEND noninteractive  

RUN apt-get -q update && \\
    apt-get install -q -y --no-install-recommends \\
      xorg \\
      unzip \\
      wget \\
      curl && \\
    apt-get clean && \\
    rm -rf /var/lib/apt/lists/*  

# Download the MCR from MathWorks site an install with -mode silent  
RUN mkdir /mcr-install && \\
    mkdir /opt/mcr && \\
    cd /mcr-install && \\
    wget --no-check-certificate -q https://ssd.mathworks.com/supportfiles/downloads/{named_vers}/Release/{update_vers}/deployment_files/installer/complete/glnxa64/MATLAB_Runtime_{named_vers}_Update_{update_vers}_glnxa64.zip && \\
    unzip -q MATLAB_Runtime_{named_vers}_Update_{update_vers}_glnxa64.zip && \\
    rm -f MATLAB_Runtime_{named_vers}_Update_{update_vers}_glnxa64.zip && \\
    ./install -destinationFolder /opt/mcr -agreeToLicense yes -mode silent && \\
    cd / && \\
    rm -rf mcr-install  

# Configure environment variables for MCR  
ENV LD_LIBRARY_PATH /opt/mcr/{ld_lib_ver}/runtime/glnxa64:/opt/mcr/{ld_lib_ver}/bin/glnxa64:/opt/mcr/{ld_lib_ver}/sys/os/glnxa64:/opt/mcr/{ld_lib_ver}/extern/bin/glnxa64  

ENV XAPPLRESDIR /etc/X11/app-defaults  

# Configure a variable to dump VersionInfo.xml and test the correct installation through GitHub Actions
ENV MCR_MASTER_PATH /opt/mcr/{ld_lib_ver}
"""
    return dockerfile


def gen_dockerfile_meshlab(vers, named_vers, date, tag_name):
    dockerfile = f"""
# MATLAB Compiler Runtime (MCR) {vers} ({named_vers})   
#   
# This docker file will configure an environment into which the Matlab compiler
# runtime will be installed and in which stand-alone matlab routines (such as
# those created with MATLAB's deploytool) can be executed.   

# MATLAB Runtime   
# Run compiled MATLAB applications or components without installing MATLAB   
# The MATLAB Runtime is a standalone set of shared libraries that enables the   
# execution of compiled MATLAB applications or components. When used together,
# MATLAB, MATLAB Compiler, and the MATLAB Runtime enable you to create and distribute  
# numerical applications or software components quickly and securely.   
#
# See https://www.mathworks.com/products/compiler/matlab-runtime.html for more info. 
#
# MeshLab  
# the open source system for processing and editing 3D triangular meshes. 
# It provides a set of tools for editing, cleaning, healing, inspecting, rendering,   
# texturing and converting meshes.  It offers features for processing raw data produced by   
# 3D digitization tools/devices and for preparing models for 3D printing.
#
# @author Riccardo De Martis {date}
# @link https://github.com/demartis/matlab_runtime_docker  
#

FROM demartis/matlab-runtime:{tag_name}  
MAINTAINER Riccardo De Martis <riccardo@demartis.it>  

RUN apt-get -q update && \\
    apt-get install -q -y --no-install-recommends \\
      meshlab && \\
    apt-get clean && \\
    rm -rf /var/lib/apt/lists/*

"""
    return dockerfile


def safe_link(target, link):
    if os.path.islink(link):
        os.unlink(link)
    os.symlink(target, link)


def create_folder(folder_name):
    if os.path.islink(folder_name):
        os.unlink(folder_name)

    if not os.path.exists(folder_name):
        os.mkdir(folder_name)


######################
# Generate Dockerfiles
######################
for build in builds:
    d_name = build[0]
    d_vers = build[1]

    # Starting from R2022b:
    # MATLAB® Runtime now installs to a folder whose name uses the corresponding MATLAB release name.
    # Previously, the default path to an installation of MATLAB Runtime included the MATLAB Runtime version,
    # such as v912 in R2022a. The new installer uses the MATLAB release name in the installation path,
    # for example, C:\Program Files\MATLAB\MATLAB Runtime\R2022b.
    if d_name >= "R2022b":
        d_libv = d_name
    else:
        d_libv = d_vers.replace('.', '')

    d_updv = build[2]
    d_date = f"\n# @creation {build[3]}"

    print('generating {} \t{} \tupdate {}'.format(d_name, d_vers, d_updv))

    # create dockerfile
    dockerfile = gen_dockerfile(d_vers, d_name, d_date, d_updv, d_libv)
    folder_name = d_name
    create_folder(folder_name)
    with open(os.path.join(folder_name, 'Dockerfile'), 'w') as f:
        f.write(dockerfile)

    # create dockerfile with Meshlab
    dockerfile = gen_dockerfile_meshlab(d_vers, d_name, d_date, folder_name)
    folder_name += '-meshlab'
    create_folder(folder_name)
    with open(os.path.join(folder_name, 'Dockerfile'), 'w') as f:
        f.write(dockerfile)


# link latest latest-meshlab
latest_name = builds[-1][0]
safe_link(latest_name, FILE_LATEST)
safe_link(f"{latest_name}-meshlab", FILE_LATEST_M)

############################
# Generate GitHub CI Actions
############################
# master
############################
cb1 = '{{'
cb2 = '}}'
ci_action = f"""
# ------------------------------------------------------------------------
# Copyright (c) 2020-2023 Riccardo De Martis. MIT License.
# All Trademarks referred to are the property of their respective owners.
# ------------------------------------------------------------------------

# This is the master workflow, taken by CI of GitHub.
# It (only) aims at properly organizing the sub-workflows.

name: CI

on:
  push:
    branches:
      - "master"

concurrency:
  group: CI-${cb1} github.head_ref || github.run_id {cb2}
  cancel-in-progress: true

jobs:
  Description:
    uses: ./.github/workflows/sub_description.yaml
    with:
      DOCKERHUB_REPO: demartis/matlab-runtime
    secrets: inherit
"""
cr = '\n'
latest_name = builds[-1][0]
for build in builds:
    d_name = build[0]

    ci_action += f"""
  {d_name}:
    uses: ./.github/workflows/sub_release.yaml
    secrets: inherit
    with:
      DOCKERHUB_REPO: demartis/matlab-runtime
      DOCKERHUB_TAG: {d_name}
      DOCKER_CONTEXT: {d_name}{str.format('{0}      is_latest: true{0}', cr) if latest_name == d_name else cr}
      MATLAB_NAME: {d_name}
  {d_name}-meshlab:
    needs: [ {d_name} ]
    uses: ./.github/workflows/sub_release.yaml
    secrets: inherit
    with:
      DOCKERHUB_REPO: demartis/matlab-runtime
      DOCKERHUB_TAG: {d_name}-meshlab
      DOCKER_CONTEXT: {d_name}-meshlab{str.format('{0}      is_latest_meshlab: true{0}', cr) if latest_name == d_name else cr}
      MATLAB_NAME: {d_name}"""

with open(os.path.join('.github', 'workflows', 'ci.yaml'), 'w') as f:
    f.write(ci_action)


