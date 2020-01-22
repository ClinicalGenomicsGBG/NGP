# NGP
National Genomic Platform

### &#x1F534; Disclaimer &#x1F534;  
> 121219  

**This is under development, some things might work, some might not.**
___  
  
# Usage  
The main script [NGP](https://github.com/ClinicalGenomicsGBG/NGP/blob/master/NGP) is a script containing several parts for compression, upload, download, delete and communication with the index. For detailed information go to the [Manual](https://github.com/ClinicalGenomicsGBG/NGP/wiki/NGP-Manual).

### Basic usage

**Using the uploader creating json files using `--template`:**  
`./uploader.py --run [RUNID] --sample [SAMPLEID] --jsonpath [/path/to/directory] --template`  

**Using the uploader:**  
`./NGP upload --bucket [BUCKETNAME] --run [RUNID] --sample [SAMPLEID] --path [/path/to/directory] --compression [/path/to/copmressionscript] --jsonpath [/path/to/directory]`  

**Using the downloader:**  
`./NGP download --bucket [BUCKETNAME] --key [path/to/file] --output [OUTPUTNAME]`  

**Delete a file:**   
`./NGP delete --bucket [BUCKETNAME] --key [path/to/file]`


### Singularity   
The Singularityfile is used to build a singularity image.   

`singularity build ngp.img Singularityfile`  

Or you can get the Singularity image by using the command:
`singularity pull --arch amd64 library://vilmacanfjorden/default/ngpr:latest`   

Use it by starting a shell and mount a directory with your input files, in this case the files are put in the directory /scratch:
`singularity shell -B /path/to/inputfiles/:/scratch ngp.img`  
    

# **More information**  
[Wiki](https://github.com/ClinicalGenomicsGBG/NGP/wiki)
