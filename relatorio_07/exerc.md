# Agregações

~~~SQL
MATCH (n:DeliveryAddress) RETURN COUNT(n.state CONTAINS 'Vermont');
MATCH (n:BankAccount) RETURN AVG(n.balance);
MATCH (n:BankAccount) RETURN MIN(n.balance);
MATCH (n:BankAccount) RETURN MAX(n.balance);
MATCH (n:CreditCard) RETURN COLLECT(n.limit) LIMIT 25;
~~~

# Funções Matemáticas

~~~SQL
MATCH (n:BankAccount) RETURN ROUND(AVG(n.balance),2);
~~~

# Funções com String

~~~SQL
MATCH (n:AccountHolder) RETURN TOUPPER(n.firstName) as Name, REPLACE(TOSTRING(n.birthDate), "-","/") as Niver LIMIT 25;
~~~
