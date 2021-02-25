Para executar pe.py:

`$ python3 pe.py "<Caminho para os arquivos PE's>"`

Exemplo:

**Entrada**

`$ python3 pe.py .`

**Saída**

```
########
 SEÇÕES EXECUTAVEIS 
########

calc.exe  Sections:  ['.text']
netstat.exe  Sections:  ['.text']
```



Para executar pe_compare.py:

`$ python3 pe_compare.py <binario 1> <binario 2> `

Exemplo:

**Entrada**

`python3 pe_compare.py calc.exe netstat.exe`

**Saída**

```

########
 SEÇÕES COMUNS
########

['.text', '.data', '.idata', '.rsrc', '.reloc']

########
 SEÇÕES UNICAS  calc.exe 
########

[]

########
 SEÇÕES UNICAS  netstat.exe 
########

[]
```

