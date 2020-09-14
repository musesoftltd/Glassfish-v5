'''
Created on 4 Apr 2017

@author: x
'''


dictionary = {
    "port" : "8686",
    
    # properties auto-generated

    "amx:pp=/domain/configs/config[default-config]/network-config/protocols/protocol[http-listener-1],type=http. Scheme" : "None",
    "amx:pp=/domain/configs/config[default-config]/network-config/protocols/protocol[http-listener-1],type=http. Version" : "HTTP/1.1",
    "amx:pp=/domain/configs/config[default-config]/network-config/protocols/protocol[http-listener-1],type=http. Adapter" : "org.glassfish.grizzly.http.server.StaticHttpHandler",
    "amx:pp=/domain/configs/config[default-config]/network-config/protocols/protocol[http-listener-1],type=http. DnsLookupEnabled" : "false",
    "amx:pp=/domain/configs/config[default-config]/network-config/protocols/protocol[http-listener-1],type=http. JkConfigurationFile" : "${com.sun.aas.instanceRoot}/config/glassfish-jk.properties",
    "amx:pp=/domain/configs/config[default-config]/network-config/protocols/protocol[http-listener-1],type=http. CompressableMimeType" : "text/html,text/xml,text/plain",
    "amx:pp=/domain/configs/config[default-config]/network-config/protocols/protocol[http-listener-1],type=http. ForcedResponseType" : "None",
    "amx:pp=/domain/configs/config[default-config]/network-config/protocols/protocol[http-listener-1],type=http. DefaultResponseType" : "None",
    "amx:pp=/domain/configs/config[default-config]/network-config/protocols/protocol[http-listener-1],type=http. SendBufferSizeBytes" : "8192",
    "amx:pp=/domain/configs/config[default-config]/network-config/protocols/protocol[http-listener-1],type=http. MaxRequestParameters" : "10000",
    "amx:pp=/domain/configs/config[default-config]/network-config/protocols/protocol[http-listener-1],type=http. Http2MaxHeaderListSizeInBytes" : "4096",
    "amx:pp=/domain/configs/config[default-config]/network-config/protocols/protocol[http-listener-1],type=http. MaxSwallowingInputBytes" : "-1",
    "amx:pp=/domain/configs/config[default-config]/network-config/protocols/protocol[http-listener-1],type=http. Http2DisableCipherCheck" : "false",
    "amx:pp=/domain/configs/config[default-config]/network-config/protocols/protocol[http-listener-1],type=http. WebsocketsTimeoutSeconds" : "900",
    "amx:pp=/domain/configs/config[default-config]/network-config/protocols/protocol[http-listener-1],type=http. MaxFormPostSizeBytes" : "2097152",
    "amx:pp=/domain/configs/config[default-config]/network-config/protocols/protocol[http-listener-1],type=http. NoCompressionUserAgents" : "None",
    "amx:pp=/domain/configs/config[default-config]/network-config/protocols/protocol[http-listener-1],type=http. ConnectionUploadTimeoutMillis" : "300000",
    "amx:pp=/domain/configs/config[default-config]/network-config/protocols/protocol[http-listener-1],type=http. MaxPostSizeBytes" : "-1",
    "amx:pp=/domain/configs/config[default-config]/network-config/protocols/protocol[http-listener-1],type=http. RemoteUserMapping" : "None",
    "amx:pp=/domain/configs/config[default-config]/network-config/protocols/protocol[http-listener-1],type=http. UploadTimeoutEnabled" : "true",
    "amx:pp=/domain/configs/config[default-config]/network-config/protocols/protocol[http-listener-1],type=http. EncodedSlashEnabled" : "false",
    
        
    # security hardening
    "x-powered-by" : "false",
    "rewrite-pattern" : "^(PUT|HEAD|DELETE|TRACE|TRACK|OPTIONS)$",
    "rewrite-flags" : "NC",
    "Http11Protocol" : "NotAvailable",
    "URI_ENCODING" : "UTF-8",
    "USE_BODY_ENCODING_FOR_QUERY_STRING" : "true",
    "enable-welcome-root": "false",
    "sampleWebAlias": "[\"localhost\"]",
    "customServerHeader": "NotAvailable",
    
    # SSL Ciphers
    "sslProtocols" : "TLSv1,TLSv1.1,TLSv1.2",
    "cipherSuite" : "ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA256"

}
