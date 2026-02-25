```shell
Get-Content media_file.txt | ForEach-Object { ni $_ -Force }
```
