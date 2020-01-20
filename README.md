MATLAB Compiler Runtime (MCR) for linux
=============================

- Updated to release 6 (MathWorks update 6, November 2019)
- ~~Updated to release 5 (MathWorks update 5, October 2015)~~

This Dockerfile will configure an environment into which the MATLAB Compiler Runtime will be installed and in which 
stand-alone MATLAB compiled applications can be executed (such as those created with deploytool or mcc).

See [MathWorks website](https://www.mathworks.com/products/compiler/matlab-runtime.html) for more info.

### Supported tags and respective Dockerfile links
- [latest, R2019a, R2019a-u6] (https://github.com/demartis/matlab_runtime_docker/blob/master/R2019a-u6/Dockerfile)
- R2019a-u5
- R2019a-u4
- R2019a-u3
- R2019a-u6-meshlab, 2019a-meshlab
- R2019a-u5-meshlab
- R2019a-u4-meshlab 
- R2019a-u3-meshlab 



### Build
To build you can download this repo and run build.sh or run:
```bash
docker build --no_cache -t demartis/matlab-runtime `pwd`
```

### Usage
To run a Matlab Stand-Alone executable (MSAE) you can do the following:
```bash
    docker run --rm -ti \
        -v /your/local/path/to/exe:/mcr/exe \
        demartis/matlab-runtime \
        /mcr/exe [<params>]
```
in a single line:
```bash
    docker run --rm -ti -v /your/local/path/to/exe:/mcr/exe demartis/matlab-runtime /mcr/exe [<params>] 
```
'exe' is your MATLAB linux compiled (MSAE) Matlab Stand-Alone executable

You can also mount the full path:
```bash
    docker run --rm -ti \
        -v /your/local/path:/mcr \
        demartis/matlab-runtime \
        /mcr/exe [<params>]
```
in a single line:
```bash
    docker run --rm -ti -v /your/local/path/:/mcr demartis/matlab-runtime /mcr/exe [<params>] 
``` 
- Remember that if those inputs are files or other resources, those resources must also be mounted in the container 
and the full path to them (in the container) must be provided.


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
   
