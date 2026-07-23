# Avaliação de modelos em ciência de dados

# Treinar um modelo de machine learning é apenas uma parte do problema. A questão realmente importante é:
# Como sabermos se o modelo é bom?
# O modelo está superajustado (overfitting)?
# O modelo está subajustado (underfitting)
# O erro é aceitável para o problema?
# Comocomparar modelos diferentes?

# Nesta aula veremos métricas para três tipos de problemas:
# 1. Regressão                - prever valores contínuos
# 2. Classificação            - prever categorias
# 3. Agrupamento (Clustering) - descobrir padrões nos dados

# Erro vs Resíduo
# Considere em um modelo que tenta prever um valor real. Denotamos:
# yi : valor observado
# ^yi : valor predito pelo modelo

# O erro verdadeiro é definido como:

# Ei = y1 - ^yi

# Entretanto, o erro verdadeiro não é observável diretamente, pois o modelo é apenas uma aproximação do processo gerador de dados. Na prática utilizamos o resíduo. O resíduo é definido como:

# ei = y1 - ^yi

# Ou seja:

# O resíduo é uma estimativa observada do erro.

