# Verificação de rastreabilidade

## Ordem de leitura

1. fonte externa ou requisito integral;
2. contexto AS-IS equivalente;
3. necessidades, stories, specs e decisões relacionadas;
4. código, configuração, migrations, dados e testes;
5. evidência atual que demonstra cada condição.

## Vereditos sugeridos

- `verificado`: todas as condições relevantes estão presentes e provadas;
- `parcial`: parte das condições está presente; liste existente e ausente;
- `divergente`: a implementação existe, mas difere da fonte esperada;
- `nao-iniciado`: a busca delimitada não encontrou implementação;
- `nao-rastreavel`: o texto não permite uma verificação objetiva.

Matriz ou dashboard ajudam a localizar relações, mas não decidem implementação. Uma story
declara intenção/trabalho; só evidência técnica atual sustenta `verificado`.

Ao descobrir uma regra durável ausente, atualize a fonte AS-IS. Ao descobrir uma lacuna não
coberta, volte à triagem em vez de inventar requisito.
