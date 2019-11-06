# MATLAB Compiler Runtime (MCR) v9.6 (R2019a)
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
#
# MeshLab
# the open source system for processing and editing 3D triangular meshes.
# It provides a set of tools for editing, cleaning, healing, inspecting, rendering,
# texturing and converting meshes.  It offers features for processing raw data produced by
# 3D digitization tools/devices and for preparing models for 3D printing.
#
#
# @author Riccardo De Martis
# @creation 2019-nov-06
#

FROM demartis/matlab-runtime:R2019a-u6
MAINTAINER Riccardo De Martis <riccardo@demartis.it>

RUN apt-get -q update && \
    apt-get install -q -y --no-install-recommends \
      meshlab && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
