# Archiving IBM BPMS
The version 8.5.5 of the IBM BPMS provides an API Rest that returns Business Objects (BO) and your values of Process Applications.
In our case we needed extract BO values and record this datas in another databank for futures reports and actions of analytics.

We has many versions of the Process Applications and BO, for mapping individually. We choose using a NoSQL database because high difficult to mapping all versions and BO along time.

The NoSQL choosen is ElasticSearch (https://github.com/elastic/elasticsearch) in your version 5.2.2, because, your stack ELK, more specifically, because of Kibana (https://github.com/elastic/kibana) an tool for generate rich reports and dashboards easily.

Builded an application in Python 2.7 for extract BO of BPMS Process Server and persist ElasticSearch (bpms_parser.py) all hosted in CentOS7 distro.
