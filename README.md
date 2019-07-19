MATLAB Compiler Runtime (MCR) for linux
=============================


This Dockerfile will configure an environment into which the MATLAB Compiler Runtime will be installed and in which 
stand-alone MATLAB compiled applications can be executed (such as those created with deploytool or mcc).

See [MathWorks website](https://www.mathworks.com/products/compiler/matlab-runtime.html) for more info.

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