#!/bin/bash
# This is a script which uses rtq2txt which downloads all tickets into *.txt files and then runs
# sa-learn --spam --no-sync, sa-learn --sync
# example:
# ./rt_qmark_spam.sh same values as you use

RTQ2TXT=$(which do_rtq2txt.py 2>/dev/null||echo "/usr/bin/python ./rtq2txt.py")
SA_LEARN=$(which sa-learn 2>/dev/null||echo "NOT_INSTALLED")
FIND=$(which find)

# Check if RTQ2TXT is installed
[ "$RTQ2TXT" = "NOT_INSTALLED" ] && (echo "rtq2txt.py is not installed"; exit 1)
[ "$SA_LEARN" = "NOT_INSTALLED" ] && (echo "sa-learn is not installed"; exit 1)

# Should return OUTPUT_DIR=
export $(${RTQ2TXT} "$@"|grep OUTPUTDIR)

# Make sure OUTPUTDIR is set. If it's not then we have a bigger problem.
[ -z ${OUTPUTDIR+x} ] && (echo "OUTPUTDIR is unset."; exit 1)

${FIND} ${OUTPUTDIR} -name "*.txt" -exec ${SA_LEARN} --spam --no-sync '{}' \;

${SA_LEARN} --sync

rm -rf ${OUTPUTDIR}
