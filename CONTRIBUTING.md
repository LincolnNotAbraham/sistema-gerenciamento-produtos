# Contribuindo para o Sistema de Gerenciamento de Produtos

Obrigado por seu interesse em contribuir! Este guia explica como participar do projeto.

## Como Contribuir

### Reportar Bugs

1. Verifique se o bug já foi reportado em [Issues](https://github.com/LincolnNotAbraham/sistema-gerenciamento-produtos/issues)
2. Se não existir, abra uma nova issue com:
   - Descrição clara do problema
   - Passos para reproduzir
   - Comportamento esperado vs. comportamento atual
   - Versão do Python e sistema operacional

### Sugerir Funcionalidades

Abra uma issue com a tag **enhancement** descrevendo:
- A funcionalidade desejada
- Por que seria útil
- Como imaginaria que funcionaria

### Enviar Alterações

1. Fork o repositório
2. Crie uma branch para sua alteração:
   ```bash
   git checkout -b feature/nome-da-feature
   ```
3. Faça suas alterações seguindo o estilo do projeto
4. Teste localmente com `python main.py`
5. Commit com mensagens descritivas:
   ```bash
   git commit -m "Add: descrição da alteração"
   ```
6. Push e abra um Pull Request

## Diretrizes

- **Estilo de código**: Mantenha consistência com o código existente
- **Commits**: Uma alteração lógica por commit
- **PRs**: Descreva o que mudou e por quê
- **Testes**: Verifique que o sistema funciona antes de enviar

## Estrutura de Commits

| Prefixo | Uso |
|---------|-----|
| `Add:` | Nova funcionalidade |
| `Fix:` | Correção de bug |
| `Docs:` | Alterações em documentação |
| `Refactor:` | Refatoração sem mudança de comportamento |
| `Style:` | Formatação, espaços em branco |
