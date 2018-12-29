
# Created on 20 Oct 2016

# @author: ...

from environmentProperties.allEnvs.propertiesExtended import dictionary as globalDictionary
from library.auditing.auditServerExtened import auditServerExtended
from library.auditing.auditingLibrary import auditObjectAtom, auditReport, auditObjectAtoms
from library.util import scatterThread, gatherThreads


def auditServersBaseThread(environment, servername, propertiesDictionary, bApplyRequiredChanges): 
    runtimeProperties = dict()
    runtimeProperties.update(globalDictionary)
    runtimeProperties.update(propertiesDictionary)

#     if connectSilent(servername, runtimeProperties["username"], runtimeProperties["password"]) == None:
#         return
    auditServerExtended(environment, servername, runtimeProperties, bApplyRequiredChanges)
        
def auditServersBase(environment, servers, propertiesDictionary, bApplyRequiredChanges) :
    # merge global properties into dict - deliberately overwriting local with global dict all values

    strThreadPoolId = "auditServersBase"
    for servername in servers:
        # Create new threads
        scatterThread(strThreadPoolId, auditServersBaseThread, args=(environment, servername, propertiesDictionary, bApplyRequiredChanges))

    gatherThreads(strThreadPoolId)

    for servername in servers:
        auditReport(environment, servername)
