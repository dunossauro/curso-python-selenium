# Passos para contribuir para as legendas

O processo será feito da seguinte forma:  
* As traduções serão feitas a partir das legendas geradas automaticamente pelo YouTube. Estes arquivos são de extensão [srt].
* Se o arquivo de legenda da aula não estiver no repositório, deverá ser feito o download do mesmo e salvo no diretório da respectiva aula e nomeado com o nome desta. Veja [como fazer o download das legendas].
* Os vídeos serão divididos em partes de 5 minutos, para o processo não ficar massante.
* Cada parte será um arquivo nomeado com o tempo de início e fim. Este tempo é baseado no tempo do arquivo.  
    ```Ex.: hh_mm_ss__hh_mm_ss.srt```
* Os diretórios das legendas devem seguir a seguinte estrutura de exemplo:
            
    ```
    |____legendas/
    | |____00_abertura/
    | | |____00_abertura.srt
    | | |____00_00_00__00_05_00.srt
    | | |____00_05_00__00_10_00.srt
    | | |____00_10_00__00_15_00.srt
    | |____01_aula1/
    | | |____01_aula1.srt
    | | |____00_00_00__00_05_00.srt
    | | |____00_05_00__00_10_00.srt
    ```


## Como fazer o download das legendas

Para fazer o download do arquivo de legenda, basta pegar o link do vídeo e ir até o site [Downsub] e baixar o arquivo na extensão **[srt]**.

## Formato dos arquivos SRT

Os arquivos de extensão srt possuem o seguinte sintaxe:

```
1097
01: 20: 45,138 -> 01: 20: 48,164
Você diria qualquer coisa agora
para conseguir o que você quer.

```

### Função de cada item

|Item   |Conteúdo   |Função   |
|:-:|:-:|---|
|1   |1097   |Posição do fragmento.   |  
|2   |01: 20: 45,138 -> 01: 20: 48,164   |Tempo de exibição do fragmento. hh:mm:ss,ms   |   
|3   |Você diria qualquer coisa agora para conseguir o que você quer.   |Conteúdo a ser exibido.   |   
|4   ||Final do bloco representado por uma linha em branco.|


<!-- LINKS ÚTEIS -->
[como fazer o download das legendas]:#como-fazer-o-download-das-legendas
[srt]:#formato-dos-arquivos-srt
[Downsub]:https://downsub.com/