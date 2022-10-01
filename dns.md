---
title: DNS Records
description: DNS (Domain Name System) takes a human friendly domain names as input and translate that to an IP Address. There are various record types like A record, CNAME, MX, TXT, SRV, AAAA etc.,
created: 2019-06-25
updated: 2022-10-01
color: #60a3bc
---

DNS (Domain Name System) takes a human friendly domain names as input and translate that to an IP Address. There are various record types like A record, CNAME, MX, TXT, SRV, AAAA etc.,

## Major DNS record types
|Record Type|Description|
|---|---|
|A Record|Points to an IPv4 address|
|AAAA|Similar to `A` but this allows to point to an `IPv6 address`|
|CNAME (Canonical Name)| Points to another domain name|
|MX (Mail Exchanger)| Directs email to a mail server|
|TXT| Map domain to text, mostly for information. Often used for verification purpose|
|SRV|Points to a domain name using a specific destination port|

## Other DNS record types
|Record Type|Description|
|---|---|
|CAA|Provide additional confirmation for the Certification Authority when validating an SSL certificate|
|CERT|Provides a space in the DNS for certificates and related certificate revocation lists|
|DNSKEY|Contains a public signing key (usually for DNSSEC)|
|DS|Refers to a DNSKEY resource record by including a digest of that DNSKEY resource record|
|LOC|Expressing geographic location information for a domain name|
|NS|Contains the name of the authoritative name server within a domain or DNS zone|
|PTR|Verify that the sender matches the IP address it claims to be using|
|SPF|Lists all the servers authorized to send emails from a particular domain|
|SSHFP|Identifies SSH keys that are associated with a host name.|
|TLSA|Associate a TLS server certificate or public key with the domain name where the record is found|
|URI|Means for publishing mappings from hostnames to URIs|
