# Archiving IBM BPMS
# Description
The version 8.5.5 of the IBM BPMS provides an API Rest that returns Business Objects (BO) and your values of Process Applications.
In our case we needed extract BO values and record this datas in another databank for futures reports and actions of analytics.

We has many versions of the Process Applications and BO, for mapping individually. We choose using a NoSQL database because high difficult to mapping all versions and BO along time.

The NoSQL choosen is ElasticSearch (https://github.com/elastic/elasticsearch) in your version 5.2.2, because, your stack ELK, more specifically, because of Kibana (https://github.com/elastic/kibana) an tool for generate rich reports and dashboards easily.

Builded an application in Python 2.7 for extract BO of BPMS Process Server and persist ElasticSearch (bpms_parser.py) all hosted in CentOS7 distro.

# Architecture
+----------+               +------------+
| IBM BPMS |---REST API ---| Python APP |  <- Extracting and parsing informations
+----------+               +------------+
                                  |
                                JSON
                                  |
                           +---------------+     +--------+
          Persistence ->   | elasticsearch | ----| kibana |  <- Analytics
                           +---------------+     +--------+
# Usage
1. Set in bpms_parser.conf you sets authenication roles.
2. Set Protocol and URL for uses REST API of the IBM BPMS.
3. Change range of instances for need persists in the elasticsearch.

Don't change other parameters without absolutely certain!

# About me
[Vimerson Pereira da Silva](https://www.linkedin.com/in/vimerson-silva-2b2bb338/?locale=en_US)

# License
This project is licensed under a LGPLv3 license; read [LICENSE](https://github.com/viperblack/Archiving_IBM_BPMS/blob/master/LICENSE) file for more information.
