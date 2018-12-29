'''
@author: ...
'''
from environmentProperties.allEnvs import propertiesExtended as globalProperties
from library.auditing.auditServerBase import auditServerExtended
from library.auditing.auditingLibrary import auditReport
from library.util import gatherThreads, scatterThread


def auditServers(environment, servers, propertiesDict, bApplyRequiredChanges) :
    # merge global propertiesDict into dict - deliberately overwriting local with global dict all values
    runtimeProperties = dict()
    runtimeProperties.update(globalProperties.dictionary)
    runtimeProperties.update(propertiesDict)
          
    for servername in servers:
        ##############################################################
        # Base server audit...
        ##############################################################
        scatterThread("auditServerExtended", auditServerExtended, args=(environment, servername, propertiesDict, bApplyRequiredChanges))
        ##############################################################
        # Base server audit...
        ##############################################################
        # auditServersBaseAudit(environment, servers, propertiesDict, bApplyRequiredChanges)
    
    gatherThreads("auditServerExtended")
    for servername in servers:    
        auditReport(environment, servername)
