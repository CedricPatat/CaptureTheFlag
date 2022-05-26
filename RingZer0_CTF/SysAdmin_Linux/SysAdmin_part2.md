<h1 align="center"> SysAdmin Part 2 </h1>

The objective of this challenge is to obtain architect's password.

---
The command to connect is : 
`$ ssh -l morpheus -p 10148 challenges.ringzer0team.com`. The password is : `VNZDDLq2x9qXCzVdABbR1HOtz`.

We search the system for all the elements relating to Trinity with the command:
`$ grep "architect" -R /etc 2>/dev/null`.


The password is base64 encoded. The command to decrypt and display the password is: `echo -n '<password>' | base64 --decode`.

The answer is displayed in the results.
