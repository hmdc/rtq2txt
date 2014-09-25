rtq2txt
=======

Reads tickets from an Request Tracker (RT) queue and outputs them in .txt

Requirements
------------
* python >= 2.6
* RT (python-rt)

Installation
------------
python setup.py install

Usage
-----
* The following example writes all tickets and writes their data to /tmp/output in the format of ticket#.txt and subsequently deletes the ticket.

```shell
python rtq2txt.py -l https://my.rt.server -u USER -p PASS -q A_RT_QUEUE -o /tmp/output -s deleted
```

* @ Harvard-MIT Data Center, we use this application to read all tickets from the SPAM queue and pipe it to sa-learn spam. If you want to do this, use the included script:
```shell
rtq_mark_spam.sh -l https://my.rt.server -u USER -p PASS -q A_RT_QUEUE -o /tmp/output -s deleted
```
