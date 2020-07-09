# Selenium + Behave

### Instação
```
python -m venv ./venv
source venv/bin/activate    # Linux
\env\Scripts\activate.ps1   # Windows

pip install behave selenium
```

#### Gerar arquivo requirements
`pip freeze > requirements.txt`

### Estrutura de diretórios

```
/
/features
/features/feature.gherkin
/features/environment.py

/features/steps
/features/steps/steps.py

/behave.ini
```

### O que vai dentro de cada arquivo?

| Arquivo | O que vai dentro? |
| ------- | ----------------- |
| *.feature | Arquivo do gherking contendo as regras de execução|
| behave.ini | configurações do projeto |
| environment.py | Hooks do projeto |
| /steps/*.py | Arquivos com implementações dos steps |
