#!/usr/bin/env python 
# -*- coding: utf-8 -*-

##########################################################################################
#  -- PortalSearch --  extract relevant 'Queries' from QP logs file                      #
##########################################################################################
# Owner: gautier.franchini@data-essential.com                                            #
# Version: 1.0                                                                           #
# creation: 09/12/2016                                                                   #
# update:  [date] [who] [what]                                                           #
#       12/12/2016: GF -- Add Regular Expression to the script.  (re.compile("xxxx"))    #
#                                                                                        #
##########################################################################################

#############################
#         FUNCTIONS         #
#############################

def extract_query_qp(logfile):
    import re
    # re.search() - to see if a str maches a regex (similar to find())
    # re.findall() - to extract portions of a strings that match you regex (similar to a combiantion of find() and slicing: var[5:10]
    # if re.match(r'^hello', somestring):
        # do stuff

    #rf = open("api_query.2016-12-04.log")
    rf = open(logfile)

    querylist = []
    line2print=''
    # get rid of multiline and spaces
    for line in rf:
        datepattern = re.compile("^[0-9]{2}\/")
        if datepattern.match(line) :
        #if line.startswith( '04/12/2016' ) == True :
            querylist.append("".join(line2print.split()))
            line2print = line.rstrip('\r\n')
        else:
            line2print += line.rstrip('\r\n')

    # store only line with query
    for element in querylist:
        # if match regex, do:
        regexpattern = re.compile(".*-ES\([0-9]+\)\={.*")
        if regexpattern.match(element) :
            # get rid of begining of line: 
                # 04/12/2016-09:31:13.787[taskExecutor-2]c9b35753-d651-462e-8b88-96a24ea661e7INFOe.e.e.p.s.q.e.ElasticsearchExecutor-ES(3)=
            element2write = element.split('=')
            wf.write(str(element2write[1]))
            wf.write('\n')  # remove to leave out line breaks
        # if not match remove from list
        else:
            querylist.pop(querylist.index(element))
    # close "logfile"
    rf.close()


def main():
    import glob, os
    # open logs file and passe them to extract query function

    os.chdir("/Users/gfranchini/Bitbucket/PyDevOps/logs")
    for file in glob.glob("*.log"):
        print(file)
        extract_query_qp(file)
        


#############################
#           main            #
#############################
wf = open("es-qp.json","w")

main()

wf.close()
