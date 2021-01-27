<?php
/*
 * Dockerfile generator.
 *
 * MIT License. Copyright (c) 2021. Riccardo De Martis
 * All Trademarks referred to are the property of their respective owners.
 */

const R_2019_A = 'R2019a';
const R_2019_B = 'R2019b';
const R_2020_A = 'R2020a';

const FILE_LATEST = 'latest';
const FILE_LATEST_M = 'latest-meshlab';

$versions = [
    R_2019_A => ['v9.6'],
    R_2019_B => ['v9.7'],
    R_2020_A => ['v9.8'],
];

$builds = [
    R_2019_A => [
        [3,'2019-Nov-06'],
        [4,'2019-Jul-18'],
        5,
        6,
        [7,'2020-Feb-21'],
        [8,'2020-Apr-04'],
        [9,'2021-Jan-27'],
    ],
    R_2019_B => [
        [1,'2020-Feb-20'],
        [2,'2020-Jan-14'],
        [3,'2020-Feb-05'],
        [4,'2020-Feb-20'],
        [5,'2020-Mar-16'],
        [6,'2020-Nov-16'],
        [7,'2021-Jan-05'],
    ],
    R_2020_A => [
        [0,'2020-Mar-24'],
        [2,'2020-Jun-06'],
        [3,'2020-Jun-29'],
        [4,'2020-Jul-22'],
        [5,'2020-Nov-22'],
        [6,'2021-Jan-27'],
    ],
];


/**
 * @param string $vers        // v9.7
 * @param string $named_vers  // R2019b
 * @param string $date        // creation date: ex: 2020-Nov-16
 * @param int    $update_vers // 6
 * @param string $ld_lib_ver  // v97
 * @return string
 */
function gen_dockerfile($vers, $named_vers, $date, $update_vers, $ld_lib_ver)
{
    $dockerfile = <<<EOF
# MATLAB Compiler Runtime (MCR) $vers ($named_vers)
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
# @author Riccardo De Martis$date
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
    wget --no-check-certificate -q https://ssd.mathworks.com/supportfiles/downloads/$named_vers/Release/$update_vers/deployment_files/installer/complete/glnxa64/MATLAB_Runtime_${named_vers}_Update_${update_vers}_glnxa64.zip && \
    unzip -q MATLAB_Runtime_${named_vers}_Update_${update_vers}_glnxa64.zip && \
    rm -f MATLAB_Runtime_${named_vers}_Update_${update_vers}_glnxa64.zip && \
    ./install -destinationFolder /opt/mcr -agreeToLicense yes -mode silent && \
    cd / && \
    rm -rf mcr-install

# Configure environment variables for MCR
ENV LD_LIBRARY_PATH /opt/mcr/$ld_lib_ver/runtime/glnxa64:/opt/mcr/$ld_lib_ver/bin/glnxa64:/opt/mcr/$ld_lib_ver/sys/os/glnxa64:/opt/mcr/$ld_lib_ver/extern/bin/glnxa64

ENV XAPPLRESDIR /etc/X11/app-defaults
EOF;

    return $dockerfile;
}

function gen_dockerfile_meshlab($vers, $named_vers, $date, $tag_name){

$dockerfile = <<<EOF
# MATLAB Compiler Runtime (MCR) $vers ($named_vers)
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
# @author Riccardo De Martis$date
#

FROM demartis/matlab-runtime:$tag_name
MAINTAINER Riccardo De Martis <riccardo@demartis.it>

RUN apt-get -q update && \
    apt-get install -q -y --no-install-recommends \
      meshlab && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

EOF;

    return $dockerfile;
}

function folder_name($d_name, $d_updv){
   return $d_name.'-u'.$d_updv;
}

function safe_link($target, $link){
    unlink($link);
    return symlink($target, $link);
}

// Generate Dockerfiles
foreach($builds as $version=>$build){

    $d_vers = $versions[$version][0];
    $d_name = $version;
    $d_libv = str_replace('.', '', $d_vers);

    foreach($build as $update) {

        if(is_array($update)){
            $d_updv = $update[0];
            $d_date = "\n# @creation $update[1]";
        }else{
            $d_updv = $update;
            $d_date = '';
        }

        // create dockerfile
        $dockerfile = gen_dockerfile($d_vers, $d_name, $d_date, $d_updv, $d_libv);

        $folder_name = folder_name($d_name, $d_updv);
        if (!file_exists($folder_name)) {
            mkdir($folder_name, 0775, true);
        }
        file_put_contents($folder_name.DIRECTORY_SEPARATOR.'Dockerfile', $dockerfile);

        // create dockerfile with Meshlab
        $dockerfile = gen_dockerfile_meshlab($d_vers, $d_name, $d_date, $folder_name);
        $folder_name .= '-meshlab';
        if (!file_exists($folder_name)) {
            mkdir($folder_name, 0775, true);
        }
        file_put_contents($folder_name.DIRECTORY_SEPARATOR.'Dockerfile', $dockerfile);
    }
}

// Link latest versions
foreach($builds as $version=>$build){

    $update = end($build);
    $d_updv = is_array($update) ? $update[0] : $update;

    $folder_name = folder_name($d_name, $d_updv);

    // link main versions
    safe_link($folder_name, $version);
    safe_link($folder_name.'-meshlab', $version.'-meshlab');
}

// link latest latest-meshlab
$last_version = end(array_keys($versions));
safe_link($last_version, FILE_LATEST);
safe_link($last_version.'-meshlab', FILE_LATEST_M);