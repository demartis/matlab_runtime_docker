MATLAB Compiler Runtime (MCR) for linux
=======================================

![Docker Automated build](https://img.shields.io/docker/cloud/automated/demartis/matlab-runtime)
![GitHub last commit](https://img.shields.io/github/last-commit/demartis/matlab_runtime_docker.svg)
![GitHub repo size in bytes](https://img.shields.io/github/repo-size/demartis/matlab_runtime_docker.svg)
![GitHub language count](https://img.shields.io/github/languages/count/demartis/matlab_runtime_docker.svg)
![GitHub](https://img.shields.io/github/license/demartis/matlab_runtime_docker)
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fdemartis%2Fmatlab_runtime_docker.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2Fdemartis%2Fmatlab_runtime_docker?ref=badge_shield)

## About 
Docker image to run compiled MATLAB applications or components **without installing MATLAB**.

**No additional MathWorks licenses** are required. You can scale up your computational power easily and you can save large amount of money since MATLAB Compiler Runtime (MCR) doesn't require any license to run pre-compiled stand-alone routines.      



```
Changelog
v1.1
- new python script generator
- support until current R2023a
- each release supported to latest update only (e.g. R2020a supported to latest update 8)
- images upgraded from Debian Stretch to Buster
- switch from Docker Hub Automated Builds to GitHub Actions
- automated push to Docker Hub -> https://hub.docker.com/r/demartis/matlab-runtime

v1.0
- 2020a Updated to release 6 (MathWorks update 27nd January 2020)
- 2020a Updated to release 5 (MathWorks update 22nd November 2020)
- 2019b Updated to releases 6+7
- 2019a Updated to releases 8+9
- 2020a Updated to release 4 (MathWorks update 22nd July 2020)
- 2020a Updated to release 3 (MathWorks update 28th June 2020)
- 2020a Updated to release 2 (MathWorks update 01st June 2020)
- 2019a Updated to release 8 (MathWorks update 04th April 2020)
- 2020a Created fist release (MathWorks update 23rd March 2020)
- 2019b Updated to release 5 (MathWorks update 16th March 2020)
- 2019a Updated to release 7 (MathWorks update 21st February 2020)
- 2019b Updated to release 4 (MathWorks update 20th February 2020)
- 2019b Updated to release 3 (MathWorks update 06th January 2020)
- 2019b Updated to release 2 (MathWorks update 13th November 2019)
- 2019b Created fist release (MathWorks update 01st November 2019)
- 2019a Updated to release 6 (MathWorks update 06th November 2019)
- 2019a Updated to release 5 (MathWorks update 05th October 2019)

```
___

This Dockerfile will configure an environment into which the MATLAB Compiler Runtime will be installed and in which 
stand-alone MATLAB compiled applications can be executed (such as those created with deploytool or mcc).

Respective builds including MeshLab tool are also available.

## TL;DR: 
1. Compile your MCR MATLAB Standalone Application executable ("*your_exe*") ([MATLAB](https://www.mathworks.com/products/matlab.html) + [MATLAB Compiler](https://www.mathworks.com/products/compiler.html) required)
2. Run *your_exe* with:
```bash
docker run --rm -ti \
   -v /your_project/for_redistribution_files_only:/mcr/exe/ \
   demartis/matlab-runtime:latest \
   /mcr/exe/your_exe [<params>]
```


## Suggested tags 

Each tag points to respective latest release

#### Standard
 

|   tag    |   tag    |   tag    |   tag    |   tag    |   tag    |   tag    |   tag    |    tag    |
|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|:---------:|
| `latest` |          |          |          |          |          |          |          |           |
| `R2023a` | `R2022b` | `R2022a` | `R2021b` | `R2021a` | `R2020b` | `R2020a` | `R2019b` | `R2019a`  | 

#### With MeshLab



|        tag       |       tag        |        tag       |       tag        |        tag       |        tag       |        tag       |         tag      |        tag       |
|:----------------:|:----------------:|:----------------:|:----------------:|:----------------:|:----------------:|:----------------:|:----------------:|:----------------:|
| `latest-meshlab` |                  |                  |                  |                  |                  |                  |                  |                  |
| `R2023a-meshlab` | `R2022b-meshlab` | `R2022a-meshlab` | `R2021b-meshlab` | `R2021a-meshlab` | `R2020b-meshlab` | `R2020a-meshlab` | `R2019b-meshlab` | `R2019a-meshlab` | 


## Links
[GitHub](https://github.com/demartis/matlab_runtime_docker), 
[Docker Hub](https://hub.docker.com/r/demartis/matlab-runtime), 
[Fossa](https://app.fossa.com/projects/git%2Bgithub.com%2Fdemartis%2Fmatlab_runtime_docker)


## Usage

1. Set up your environment 

    1. Pull (suggested method)

        ```bash
        docker pull demartis/matlab-runtime:latest
        ```

    2. Build (not suggested method)
    
        To build by your own the latest tag you can *git clone* this repo, then execute build.sh or run:
        ```bash
        docker build --no-cache --tag demartis/matlab-runtime `pwd`/latest
        ```

2. Compile your MCR executable as Standalone Application (MATLAB Application Compiler). Follow the [MathWorks' compiler official reference](https://www.mathworks.com/products/compiler.html)

3. Run your MCR executable in docker

To run a Matlab Stand-Alone executable (MSAE) you can do the following:
```bash
docker run --rm -ti \
   -v /your_project/for_redistribution_files_only:/mcr/exe \
   demartis/matlab-runtime:latest \
   /mcr/exe/your_exe [<params>]
```
in a single line:
```bash
docker run --rm -ti -v /your_project/for_redistribution_files_only:/mcr/exe demartis/matlab-runtime:latest /mcr/exe/your_exe [<params>] 
```
"your_exe" is your MATLAB linux compiled (MSAE) Matlab Stand-Alone executable.

*Remember* that if your application needs files or other resources as input or generate some output, those resources must also be mounted in the container 
and the full path to them (in the container) must be provided.  
e.g.:
```bash
docker run --rm -ti \
  -v /your_project/for_redistribution_files_only:/mcr/exe \
  ...
  -v /your_data/data_input:/mcr/input/ \
  -v /your_data/data_output:/mcr/output/ \
  ...	
  demartis/matlab-runtime:latest \
  /mcr/exe/your_exe [<params>]
```

You can also send ENV params to your exe
```bash
docker run --rm -ti \
  -v /your_project/for_redistribution_files_only:/mcr/exe \
  ...
  --env CUSTOM_VAR1="lorem ipsum 1" \
  --env CUSTOM_VAR2="lorem ipsum 2" \
  ...	
  demartis/matlab-runtime:latest \
  /mcr/exe/your_exe [<params>]
```
and get them with [getenv function](https://www.mathworks.com/help/matlab/ref/getenv.html):
```Matlab
% MATLAB code
var1=getenv('CUSTOM_VAR1')
var2=getenv('CUSTOM_VAR2')
```

Please [contact me](mailto:riccardodemartis@hotmail.com) if you encounter any issue

## Supported tags and respective Dockerfile links

- [latest](https://github.com/demartis/matlab_runtime_docker/blob/master/latest/Dockerfile)
- [R2023a](https://github.com/demartis/matlab_runtime_docker/blob/master/R2023a/Dockerfile)
- [R2022b](https://github.com/demartis/matlab_runtime_docker/blob/master/R2022b/Dockerfile)
- [R2022a](https://github.com/demartis/matlab_runtime_docker/blob/master/R2022a/Dockerfile)
- [R2021a](https://github.com/demartis/matlab_runtime_docker/blob/master/R2021a/Dockerfile)
- [R2021b](https://github.com/demartis/matlab_runtime_docker/blob/master/R2021b/Dockerfile)
- [R2020b](https://github.com/demartis/matlab_runtime_docker/blob/master/R2020b/Dockerfile)
- [R2020a](https://github.com/demartis/matlab_runtime_docker/blob/master/R2020a/Dockerfile)
- [R2019b](https://github.com/demartis/matlab_runtime_docker/blob/master/R2019b/Dockerfile)
- [R2019a](https://github.com/demartis/matlab_runtime_docker/blob/master/R2019a/Dockerfile)

-------------------------------------

- [latest-meshlab](https://github.com/demartis/matlab_runtime_docker/blob/master/latest-meshlab/Dockerfile)
- [R2023a-meshlab](https://github.com/demartis/matlab_runtime_docker/blob/master/R2023a-meshlab/Dockerfile)
- [R2022b-meshlab](https://github.com/demartis/matlab_runtime_docker/blob/master/R2022b-meshlab/Dockerfile)
- [R2022a-meshlab](https://github.com/demartis/matlab_runtime_docker/blob/master/R2022a-meshlab/Dockerfile)
- [R2021a-meshlab](https://github.com/demartis/matlab_runtime_docker/blob/master/R2021a-meshlab/Dockerfile)
- [R2021b-meshlab](https://github.com/demartis/matlab_runtime_docker/blob/master/R2021b-meshlab/Dockerfile)
- [R2020b-meshlab](https://github.com/demartis/matlab_runtime_docker/blob/master/R2020b-meshlab/Dockerfile)
- [R2020a-meshlab](https://github.com/demartis/matlab_runtime_docker/blob/master/R2020a-meshlab/Dockerfile)
- [R2019b-meshlab](https://github.com/demartis/matlab_runtime_docker/blob/master/R2019b-meshlab/Dockerfile)
- [R2019a-meshlab](https://github.com/demartis/matlab_runtime_docker/blob/master/R2019a-meshlab/Dockerfile)


## Included MATLAB Runtime boxes
```
- 5G Toolbox Addin
- Aerospace Toolbox Addin
- Audio Toolbox Addin
- Automated Driving Toolbox Addin
- Bioinformatics Toolbox Addin
- Communications Toolbox Addin
- Computer Vision Toolbox Addin
- Control System Toolbox Addin
- Core
- Curve Fitting Toolbox Addin
- Database Toolbox Addin
- Datafeed Toolbox Addin
- Deep Learning Toolbox Addin
- DSP System Toolbox Addin
- Econometrics Toolbox Addin
- Financial Instruments Toolbox Addin
- Financial Toolbox Addin
- Fixed-Point Designer Addin
- Fuzzy Logic Toolbox Addin
- Global Optimization Toolbox Addin
- Hadoop And Spark Addin
- Image Acquisition Toolbox Addin
- Image Processing Toolbox Addin
- Instrument Control Toolbox Addin
- Java Addin
- LTE Toolbox Addin
- Mapping Toolbox Addin
- MATLAB Report Generator Addin
- Model Predictive Control Toolbox Addin
- Navigation Toolbox Addin
- NET And Excel Addin
- Numerics
- Optimization Toolbox Addin
- Parallel Computing Toolbox Addin
- Partial Differential Equation Toolbox Addin
- Phased Array System Toolbox Addin
- Predictive Maintenance Toolbox Addin
- Production Server Addin
- Python
- Rapid Accelerator
- RF Toolbox Addin
- Risk Management Toolbox Addin
- Robotics System Toolbox Addin
- ROS Toolbox Addin
- Sensor Fusion and Tracking Toolbox Addin
- Signal Processing Toolbox Addin
- SimBiology Addin
- Simulink 3D Animation Addin
- Simulink Design Optimization Addin
- Statistics and Machine Learning Toolbox Addin
- System Identification Toolbox Addin
- Text Analytics Toolbox Addin
- Trading Toolbox Addin
- Vehicle Network Toolbox Addin
- Wavelet Toolbox Addin
- Web Apps Addin
- WLAN Toolbox Addin
```


--------------------------------------
## Support

This project is released as is, use it at you own risk. Ensure your project be compatible with the MIT License and Third Party licenses.

Please use [GitHub Issues](https://github.com/demartis/matlab_runtime_docker/issues) or [contact me](mailto:riccardodemartis@hotmail.com) for any question or collaboration.


--------------------------------------

## Disclaimer
```
Disclaimer:
The code included in this project will not decompile, modify, reverse engineer, or create derivative works.
MATLAB, MeshLab and their respective Company names are protected by Copyright Law. 
You acknowledge that you’re using copyrighted material.
```
See [MathWorks](https://www.mathworks.com/products/compiler/matlab-runtime.html) and [Meshlab](http://www.meshlab.net/) websites for more info. 



### Licenses


```
MATLAB Compiler Runtime (MCR)
MATLAB Runtime is a collection of shared libraries and code that enables the execution of 
compiled and packaged MATLAB applications on systems without an installed version of MATLAB.
See MathWorks website: https://www.mathworks.com/products/compiler/matlab-runtime.html for more info.

MeshLab
MeshLab sources are distributed under the GPL 3.0 Licensing Scheme.
The 'MeshLab' name is a EUIPO trademark owned by CNR.
MeshLab Logos are distributed under Creative Commons License
Creative Commons Attribution-Sharealike 4.0 International License and they can be freely used inside any wikimedia project.

```
   
