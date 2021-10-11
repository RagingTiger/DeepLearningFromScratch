## TL;DR
`JupyterLab` notebook exploring the contents of
*Deep Learning from Scratch: Building with Python from First Principles* by
[Seth Weidman](https://github.com/SethHWeidman).

**Quickstart On Mac with Docker:**
```
# assumes your current working directory is DeepLearningFromScratch
docker run -d \
           --rm \
           --name jupyter-dlfs \
           -e JUPYTER_ENABLE_LAB=yes \
           -e TZ=America/New_York \
           -p 8888:8888 \
           -v $PWD:/home/jovyan/work \
           jupyter/scipy-notebook:lab-3.1.14 && \
sleep 5 && \
docker logs jupyter-dlfs 2>&1 | grep "http://127.0.0.1" | tail -n 1 | awk '{print $2}'
```

# Usage
Below we will discuss running the `JupyterLab` server.

## Docker
`Docker` will be the primary way discussed for running the `JupyterLab` server.
Please see the [Docker documentation](https://docs.docker.com/get-started/overview/)
for more info about `Docker`.

### Remove
To remove the server simply stop it
```
$ docker stop jupyter-dlfs
```

### :)
```
head -n 15 README.md
```

# References
+ [Code for DeepLearningFromScratch](https://github.com/SethHWeidman/DLFS_code)
