# Archiving IBM BPMS
# Description
The version 8.5.5 of the IBM BPMS provides an API Rest that returns Business Objects (BO) and your values of Process Applications.
In our case we needed extract BO values and record this datas in another databank for futures reports and actions of analytics.

We has many versions of the Process Applications and BO, for mapping individually. We choose using a NoSQL database because high difficult to mapping all versions and BO along time.

The NoSQL choosen is ElasticSearch (https://github.com/elastic/elasticsearch) in your version 5.2.2, because, your stack ELK, more specifically, because of Kibana (https://github.com/elastic/kibana) an tool for generate rich reports and dashboards easily.

Builded an application in Python 2.7 for extract BO of BPMS Process Server and persist ElasticSearch (bpms_parser.py) all hosted in CentOS7 distro.

Table of Contents: Optionally, include a table of contents in order to allow other people to quickly navigate especially long or detailed READMEs.

Installation: Installation is the next section in an effective README. Tell other users how to install your project locally. Optionally, include a gif to make the process even more clear for other people.

Usage: The next section is usage, in which you instruct other people on how to use your project after they’ve installed it. This would also be a good place to include screenshots of your project in action.

Contributing: Larger projects often have sections on contributing to their project, in which contribution instructions are outlined. Sometimes, this is a separate file. If you have specific contribution preferences, explain them so that other developers know how to best contribute to your work. To learn more about how to help others contribute, check out the guide for (setting guidelines for repository contributors)[https://help.github.com/articles/setting-guidelines-for-repository-contributors/].

Credits: Include a section for credits in order to highlight and link to the authors of your project.

# License
This project is licensed under a LGPLv3 license; read LICENSE file for more information.
