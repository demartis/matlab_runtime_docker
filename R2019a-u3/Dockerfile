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
# @author Riccardo De Martis 
# @creation 2019-Nov-06
#

FROM debian:stretch-slim
MAINTAINER Riccardo De Martis <riccardo@demartis.it>
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -q update && \
    apt-get install -q -y --no-install-recommends \
      xorg \
      unzip \
      wget \
      curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Download the MCR from MathWorks site an install with -mode silent
RUN mkdir /mcr-install && \
    mkdir /opt/mcr && \
    cd /mcr-install && \
    wget --no-check-certificate -q https://ssd.mathworks.com/supportfiles/downloads/R2019a/Release/3/deployment_files/installer/complete/glnxa64/MATLAB_Runtime_R2019a_Update_3_glnxa64.zip && \
    unzip -q MATLAB_Runtime_R2019a_Update_3_glnxa64.zip && \
    rm -f MATLAB_Runtime_R2019a_Update_3_glnxa64.zip && \
    ./install -destinationFolder /opt/mcr -agreeToLicense yes -mode silent && \
    cd / && \
    rm -rf mcr-install

# Configure environment variables for MCR
ENV LD_LIBRARY_PATH /opt/mcr/v96/runtime/glnxa64:/opt/mcr/v96/bin/glnxa64:/opt/mcr/v96/sys/os/glnxa64:/opt/mcr/v96/extern/bin/glnxa64

ENV XAPPLRESDIR /etc/X11/app-defaults