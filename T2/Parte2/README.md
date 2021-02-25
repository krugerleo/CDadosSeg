Para executar a parte 1:

`$ python3 pe.py -p "<Caminho para os arquivos PE's>"`

Exemplo:

**Entrada**

`$ python3 pe.py -p "./"`

**Saída**

```
######## SEÇÕES EXECUTAVEIS ########

Binary: calc copy.exe - Sections : ['.text']

Binary: calc.exe - Sections : ['.text']
```



Para executar a parte 2:

`$ python3 pe_compare.py <binario 1> <binario 2> `

Exemplo:

**Entrada**

`python3 pe_compare.py calc\ copy.exe calc.exe`

**Saída**

```
['.text', '.data', '.idata', '.rsrc', '.reloc']


######## Seções únicas de calc copy.exe ########

[]


######## Seções únicas de calc.exe ########

[]
```



Ou para melhor demonstração, alterei o nome de algumas seções do segundo arquivo para imprimir as diferenciações únicas

```
######## Seções comuns entre os binários calc copy.exe e calc.exe ########

['.data', '.idata', '.reloc']


######## Seções únicas de calc copy.exe ########

['.text', '.rsrc']


######## Seções únicas de calc.exe ########

['.text_alterado', '.rsrc_alterado']
```


