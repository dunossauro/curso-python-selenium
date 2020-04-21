# Passos para contribuir para as legendas

A princípio, usaremos o vídeo da [live de 3 anos](https://www.youtube.com/watch?v=M0T4ZvtzYNs) do canal como experiência do projeto de tradução.

O processo será feito da seguinte forma:  
* Criar os arquivos com o texto transcrito sem se preocupar com o tempo do vídeo.
    * Os vídeos serão divididos em partes de 5 minutos.
    * Cada parte será um arquivo nomeado com o tempo de início e fim.  
    ```Ex.: 0_5.txt```
    * Serão criadas issues do vídeo que estiver em processo de legenda.
    * Nesta issue quem for se dedicar a alguma parte do vídeo, deve infomar nos comentários que o está fazendo.
    * Os diretórios devem segiur a seguinte estrutura:
            
        ```
        .
        |____legendas/
        | |____live_3_anos/
        | | |____0_5.txt
        | | |____5_10.txt
        | | |____10_20.txt
        | |____aula1/
        | | |____0_5.txt
        | | |____5_10.txt
        ```

* Transformar os arquivos de texto em arquivo **srt** (arquivos de legenda).
    * Este processo ainda não foi definido como será feito.
