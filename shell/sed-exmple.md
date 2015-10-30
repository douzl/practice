```
zdou@zdou-django:~/work/shell$ cat db.txt
'dsn'=>'mysql:host=localhost;dbname=mydb;'
'dsn'=>'mysql:host=localhost1;dbname=mydb1;'
'dsn'=>'mysql:host=localhost2;dbname=mydb2;'
zdou@zdou-django:~/work/shell$
zdou@zdou-django:~/work/shell$
zdou@zdou-django:~/work/shell$ sed -i -e 's/\(mysql:host=\).*\(;dbname=.*\)/\1dbhostreplaced\2/g' -e 's/\(dbname=\).*\(;.*\)/\1dbnamereplaced\2/g' db.txt
zdou@zdou-django:~/work/shell$
zdou@zdou-django:~/work/shell$
zdou@zdou-django:~/work/shell$ cat db.txt
'dsn'=>'mysql:host=dbhostreplaced;dbname=dbnamereplaced;'
'dsn'=>'mysql:host=dbhostreplaced;dbname=dbnamereplaced;'
'dsn'=>'mysql:host=dbhostreplaced;dbname=dbnamereplaced;'
```
