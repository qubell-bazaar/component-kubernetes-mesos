Description
===========
Install and configure Kubernetes cluster with Mesos as  cloud provider

Version 1.0-43p
-------------

[![Install](https://raw.github.com/qubell-bazaar/component-skeleton/master/img/install.png)](https://express.qubell.com/applications/upload?metadataUrl=https://raw.github.com/qubell-bazaar/component-kubernetes-mesos/1.0-43p/meta.yml)

Attributes
----------

Configurations
--------------
 - Kubernetes 1.0 release
 - Mesos 0.22.0  
 - Ubuntu 14.04 (us-east-1/ami-d85e75b0), AWS EC2 m1.small, ubuntu

Pre-requisites
--------------
 - Configured Cloud Account a in chosen environment
 - Either installed Chef on target compute OR launch under root
 - Internet access from target compute:
  - S3 bucket with Chef recipes: ** (TBD)
  - If Chef is not installed: ** (TBD)

Implementation notes
--------------------
 - Installation is based on Chef recipes from ""

