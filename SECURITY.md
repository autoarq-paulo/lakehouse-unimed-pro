# Segurança e Boas Práticas

Este projeto é um laboratório educacional. Ainda assim, algumas medidas básicas de segurança são recomendadas para qualquer implantação, mesmo em ambientes de testes:

1. **Variáveis Sensíveis**: Nunca comite senhas e chaves diretamente no repositório. Utilize o arquivo `.env` (não versionado) para armazenar credenciais.
2. **Políticas de Acesso**: Crie usuários específicos no MinIO e atribua permissões mínimas necessárias para cada serviço (ingestão, processamento, consultas).
3. **TLS e Autenticação**: Considere a inclusão de um proxy reverso (Traefik, Nginx) com TLS e autenticação básica/OAuth para interfaces Web (Airflow, Trino, Grafana, MinIO).
4. **Atualizações**: Mantenha as imagens Docker e dependências atualizadas para evitar vulnerabilidades conhecidas.
5. **Dados de Exemplo**: Este projeto utiliza dados fictícios. Para dados reais, implemente mascaramento/anonymização conforme LGPD/GDPR.
6. **Segurança do Catálogo**: Controle o acesso ao Hive Metastore e ao catálogo Iceberg/Delta com permissões de leitura/escrita adequadas.

Estas práticas não esgotam o tema de segurança, mas servem como um ponto de partida para evoluir o projeto de laboratório para um ambiente mais robusto.