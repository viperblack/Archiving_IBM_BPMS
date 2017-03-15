# Archiving IBM BPMS (v8.5.5)
The version 8.5.5 of the IBM BPMS 8.5.5 provides an API HTTP that returns Business Objects (BO) and your values of Process Applications.
In our case we needed extract BO values and record this datas in another databank.
We has many versions of the Process Applications and BO for mapping. We choose using a NoSQL database because high difficult to mapping all versions and BO along time.

The NoSQL choosen is ElasticSearch, because, your stack ELK, more specifically, using Kibana for generate reports and dashboards easily.

Builded an application in Python 2.7 for extract BO of BPMS Process Server and persist in ElasticSearch (bpms_parser.py).
