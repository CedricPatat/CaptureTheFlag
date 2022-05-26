<h1 align="center"> SysAdmin Part 1 </h1>

The objective of this challenge is to obtain Trinity's password.

---
The command to connect is : 
`$ ssh -l morpheus -p 10089 challenges.ringzer0team.com`.

We search the system for all the elements relating to Trinity with the command:
`$ grep "trinity" -R /etc`.

It is possible to not display errors with the command: `$ grep "trinity" -R /etc 2>/dev/null`.

The answer is displayed in the results.
