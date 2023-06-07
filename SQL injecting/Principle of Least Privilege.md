Principle of Least Privilege
Applications should ensure that each process or software component can access and affect only the resources it needs. Apply “levels of clearance” as appropriate, in the same way that only certain bank employees have access to the vault. Applying restricted privileges can help mitigate a lot of the risk around injection attacks.

It is rarely necessary for applications to change the structure of the database at run-time – typically tables are created, dropped, and modified during release windows, with temporarily elevated permissions. Therefore, it is good practice to reduce the permissions of the application at runtime, so it can at most edit data, but not change table structures. In a SQL database, this means making sure your production accounts can only execute DML statements, not DDL statements.

With complex database designs, it can be worth making these permissions even more fine-grained. Many processes can be permissioned to perform data edits only through stored procedures, or to execute with read-only permissions.

Sensibly designing access management in this way can provide a vital second line of defense. No matter how the attacker gets access to your system, it can mitigate the type of damage they can possibly do.