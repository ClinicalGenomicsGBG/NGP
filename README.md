# NGP
National Genomic Platform

## &#x1F534; Disclaimer &#x1F534;  
> 121219  

**This is under development, some things might work, some might not.**
___  
  
# Usage  
The main script [NGP](https://github.com/ClinicalGenomicsGBG/NGP/blob/master/NGP) is a script containing several parts for compression, upload, download, delete and communication with the index. For detailed information go to the [Manual](https://github.com/ClinicalGenomicsGBG/NGP/wiki/NGP-Manual).

### Basic usage
**Using the uploader:**  
`./NGP upload --bucket [BUCKETNAME] --run [RUNID] --sample [SAMPLEID] --path [/path/to/directory] --compression [/path/to/copmressionscript] --jsonpath [/path/to/directory]`  

**Using the downloader:**  
`./NGP download --bucket [BUCKETNAME] --key [path/to/file] --output [OUTPUTNAME]`  

**Delete a file:**   
`./NGP delete --bucket [BUCKETNAME] --key [path/to/file]`
