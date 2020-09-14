
# Created on 20 Oct 2016

# @author: ...

from environmentProperties.localhost.inventory import servers 
from environmentProperties.localhost.properties import dictionary
from library.auditing.auditServersBase import auditServersBase
from library.auditing.auditingLibrary import auditInitAudit

bApplyRequiredChanges = 1
auditInitAudit("localhost", "GlassFishGeneral")
auditServersBase("local servers", servers, dictionary, bApplyRequiredChanges)

