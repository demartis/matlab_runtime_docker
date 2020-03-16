MATLAB Compiler Runtime (MCR) for linux
=======================================

Logs: 

```
- 2019b Updated to release 5 (MathWorks update 16th March 2020)
- 2019a Updated to release 7 (MathWorks update 21st February 2020)
- 2019b Updated to release 4 (MathWorks update 20th February 2020)
- 2019b Updated to release 3 (MathWorks update 06th January 2020)
- 2019b Updated to release 2 (MathWorks update 13th November 2019)
- 2019b Created fist release (MathWorks update 01st November 2019)
- 2019a Updated to release 6 (MathWorks update 06th November 2019)
- 2019a Updated to release 5 (MathWorks update 05th October 2019)

```

This Dockerfile will configure an environment into which the MATLAB Compiler Runtime will be installed and in which 
stand-alone MATLAB compiled applications can be executed (such as those created with deploytool or mcc).

Respective builds including MeshLab tool are also available.

```
Disclaimer:
The code included in this project will not decompile, modify, reverse engineer, or create derivative works.
MATLAB, MeshLab and their respective Company names are protected by Copyright Law. 
You acknowledge that you’re using copyrighted material.
```
See [MathWorks](https://www.mathworks.com/products/compiler/matlab-runtime.html) and [Meshlab](http://www.meshlab.net/) websites for more info. 



## Supported tags and respective Dockerfile links

#### R2019b:
- [R2019b-u5, R2019b, latest](https://github.com/demartis/matlab_runtime_docker/blob/master/R2019b-u5/Dockerfile)
- [R2019b-u4](https://github.com/demartis/matlab_runtime_docker/blob/master/R2019b-u4/Dockerfile)
- [R2019b-u3](https://github.com/demartis/matlab_runtime_docker/blob/master/R2019b-u3/Dockerfile)
- [R2019b-u2](https://github.com/demartis/matlab_runtime_docker/blob/master/R2019b-u2/Dockerfile)
- [R2019b-u1](https://github.com/demartis/matlab_runtime_docker/blob/master/R2019b-u1/Dockerfile)

#### R2019b + Meshlab:
- [R2019b-u4-meshlab, R2019b-meshlab](https://github.com/demartis/matlab_runtime_docker/blob/master/R2019b-u4-meshlab/Dockerfile)
- [R2019b-u3-meshlab](https://github.com/demartis/matlab_runtime_docker/blob/master/R2019b-u3-meshlab/Dockerfile)
- [R2019b-u2-meshlab](https://github.com/demartis/matlab_runtime_docker/blob/master/R2019b-u2-meshlab/Dockerfile)
- [R2019b-u1-meshlab](https://github.com/demartis/matlab_runtime_docker/blob/master/R2019b-u1-meshlab/Dockerfile)

#### R2019a:
- [R2019a-u7, R2019a](https://github.com/demartis/matlab_runtime_docker/blob/master/R2019a-u7/Dockerfile)
- [R2019a-u6](https://github.com/demartis/matlab_runtime_docker/blob/master/R2019a-u6/Dockerfile)
- [R2019a-u5](https://github.com/demartis/matlab_runtime_docker/blob/master/R2019a-u5/Dockerfile)
- [R2019a-u4](https://github.com/demartis/matlab_runtime_docker/blob/master/R2019a-u4/Dockerfile)
- [R2019a-u3](https://github.com/demartis/matlab_runtime_docker/blob/master/R2019a-u3/Dockerfile)

#### R2019a + Meshlab:
- [R2019a-u7-meshlab, R2019a-meshlab](https://github.com/demartis/matlab_runtime_docker/blob/master/R2019a-u7-meshlab/Dockerfile)
- [R2019a-u6-meshlab](https://github.com/demartis/matlab_runtime_docker/blob/master/R2019a-u6-meshlab/Dockerfile)
- [R2019a-u5-meshlab](https://github.com/demartis/matlab_runtime_docker/blob/master/R2019a-u5-meshlab/Dockerfile)
- [R2019a-u4-meshlab](https://github.com/demartis/matlab_runtime_docker/blob/master/R2019a-u4-meshlab/Dockerfile)
- [R2019a-u3-meshlab](https://github.com/demartis/matlab_runtime_docker/blob/master/R2019a-u3-meshlab/Dockerfile)




## Usage

1.
    1. Pull (suggested method)

        ```bash
        docker pull demartis/matlab-runtime:latest
        
        ```

    2. Build (not suggested method)
    
        To build by your own the latest tag you can git clone this repo and run build.sh or run:
        ```bash
        docker build --no-cache --tag demartis/matlab-runtime `pwd`/latest
        ```

2. Compile your MCR executable

3. Run your MCR executable in docker

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
   
