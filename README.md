[TOC]

四步思考法：

1. 放大影响面，如何快速响应修复（横向放大，广度）
2. 影响深入了，如何处理（纵向深入，深入）
3. 如何防止再次发生（本质思考）
4. 是否能形成产品或者防御链（输出）

举个例子：

1. 假定某个漏洞的影响面很广，有100万台内外网服务器受影响，无法及时迭代，如何防护？
2. 某些服务器已被入侵，如何在数万台服务器中快速区分出沦陷的服务器？
3. 如何防止再次发生同样的事情？
4. 能否输出点产品或者思考？

### Security

#### CVE Collections

- Type
- Usage
- Exp or Poc
- Analysis

#### Defense

- WAF

- IDS

- IPS

- Obfuscated code

- Information Leak Monitor
- Code Auidt (Dangerout API, demo, Exploit)
  - PHP
  - Java
  - Python
  - Go

#### Vulnerabilities(God's View)

- Web 
  - Xss
  - SqlInject
  - SSRF
  - CSRF
  - Unauthorized access
  - CMD inject
  - information leak
  - File upload
  - Bypass OAuth or OTP 
  - Presudo random generators
  - Graph QL
- Mobile 
  - Android
  - IOS
- Privilege Escalation
  - Windows
  - Linux
- New Attack Technique
  - To do

#### Tools

- Shell Managers
- Web Shell
  - PHP
  - Java(JSP)
  - Python
  - Asp
- Malware-Analysis
  - IDA Pro
- Information Gather

  - Brute Force Path
  - Domain Scanner
  - Domain certificate
  - Dictonary
    - username
    - password
    - webpath
    - middle software info
    - common ports
- Port Forward
  - Lcx
  - nc
  - ncat
- Port Scan
  - nmap
  - masscan
  - zmap
- Proxy Tools
  - BurpSuite

  - Fiddler

  - MITM Proxy

  - Wireshark

  - Tcpdump & ssldump
- Scanner
  - AWVS
  - APPScan
  - Nessus
- Post Exploit
  - [Metasploit](https://www.metasploit.com/)
  - [CobaltStrike](https://www.cobaltstrike.com/)
  - [Empire](http://www.powershellempire.com/)
  - [mimikatz](https://github.com/gentilkiwi/mimikatz)

#### Certificates

- CEH
- CISP
- CISSP
- OSCP
- OSCE
- OSEE
- Security +
- ISO 27001

#### Lab Environment

- [Hack the box](https://www.hackthebox.eu/)
- [Pentester Academy](https://www.pentesteracademy.com/)
- [Vulnhub](https://www.vulnhub.com/)

#### Bug Bounty Platform

- [Hackerone](http://hackerone.com/)
- [Bugcrowd](https://www.bugcrowd.com/)