# flake8: noqa
from django import forms


class HeartDiseasePredictionForm(forms.Form):
    age = forms.FloatField(
        label="Idade",
        help_text="Idade do paciente em anos."
    )
    sex = forms.ChoiceField(
        label="Sexo",
        choices=((0, "Feminino"), (1, "Masculino")),
        help_text="Sexo do paciente. Escolha entre 'Feminino' ou 'Masculino' para identificar o gênero do paciente."
    )
    cp = forms.ChoiceField(
        label="Tipo de Dor no Peito",
        choices=(
            (0, "Angina Típica"),
            (1, "Angina Atípica"),
            (2, "Dor Não Anginosa"),
            (3, "Assintomático"),
        ),
        help_text="Tipo de dor no peito relatada pelo paciente. Escolha uma das opções que melhor descreva a sensação de dor."
    )
    trestbps = forms.FloatField(
        label="Pressão Arterial de Repouso",
        help_text="Pressão arterial de repouso do paciente (mm Hg). Insira o valor da pressão arterial em milímetros de mercúrio (mm Hg). "
        "Por exemplo, uma pressão arterial normal está na faixa de 90/60 mm Hg a 120/80 mm Hg. Valores acima dessa faixa podem indicar pressão alta."
    )
    chol = forms.FloatField(
        label="Colesterol Sérico",
        help_text="Nível de colesterol sérico do paciente (mg/dl). Insira o valor do colesterol em miligramas por decilitro (mg/dl). "
        "O colesterol é uma substância gordurosa no sangue e valores elevados podem indicar risco de doenças cardiovasculares."
        "Por exemplo, um nível de colesterol total abaixo de 200 mg/dl é considerado desejável, enquanto um nível acima de 240 mg/dl pode ser preocupante."
    )
    fbs = forms.ChoiceField(
        label="Açúcar no Sangue em Jejum",
        choices=((0, "Menor ou igual a 120 mg/dl"),
                 (1, "Maior que 120 mg/dl")),
        help_text="Nível de açúcar no sangue em jejum do paciente. Escolha entre 'Menor ou igual a 120 mg/dl' ou 'Maior que 120 mg/dl' para indicar se o nível de açúcar está elevado."
    )
    restecg = forms.ChoiceField(
        label="Resultados do Eletrocardiograma em Repouso",
        choices=(
            (0, "Normal"),
            (1, "Anormalidade da Onda ST-T"),
            (2, "Hipertrofia Ventricular Esquerda Provável ou Definitiva (Critérios de Estes)"),
        ),
        help_text="Resultados do eletrocardiograma em repouso do paciente. Escolha a opção que melhor descreva o resultado do eletrocardiograma."
    )
    thalach = forms.FloatField(
        label="Frequência Cardíaca Máxima Alcançada",
        help_text="Frequência cardíaca máxima alcançada durante o exercício. Insira o valor da frequência cardíaca em batimentos por minuto (bpm). "
        "A frequência cardíaca máxima é um indicador do esforço cardiovascular durante o exercício e pode variar com a idade. "
        "Por exemplo, uma frequência cardíaca máxima de 220 - idade do paciente é frequentemente usada como uma estimativa geral. "
        "Uma frequência cardíaca máxima saudável durante o exercício depende do condicionamento físico do paciente."
    )
    exang = forms.ChoiceField(
        label="Angina Induzida por Exercício",
        choices=((0, "Não"), (1, "Sim")),
        help_text="Angina induzida por exercício relatada pelo paciente. Escolha entre 'Não' ou 'Sim' para indicar se o paciente teve angina após o exercício."
    )
    oldpeak = forms.FloatField(
        label="Depressão do Segmento ST Induzida por Exercício",
        help_text="Depressão do segmento ST induzida por exercício em relação ao repouso. Insira o valor da depressão do segmento ST. "
        "A depressão do segmento ST é uma medida do deslocamento para baixo do segmento ST no eletrocardiograma após o exercício, "
        "indicando possíveis problemas de fluxo sanguíneo para o coração. Uma depressão maior pode ser um sinal de isquemia cardíaca, "
        "enquanto uma depressão menor pode ser considerada normal. Valores elevados podem indicar um risco maior de doença cardíaca. "
        "Consulte um profissional de saúde para interpretação clínica precisa."
    )
    slope = forms.ChoiceField(
        label="Inclinação do Segmento ST no Pico do Exercício",
        choices=(
            (0, "Ascendente"),
            (1, "Plano"),
            (2, "Descendente"),
        ),
        help_text="Inclinação do segmento ST no pico do exercício. Escolha a opção que melhor descreva a inclinação do segmento ST."
    )
    ca = forms.IntegerField(
        label="Número de Vasos Principais Coloridos por Fluoroscopia",
        min_value=0, max_value=3,
        help_text="Número de vasos principais coloridos por fluoroscopia. Insira a quantidade de vasos principais que apresentaram coloração durante o procedimento. "
        "A fluoroscopia é um exame médico que utiliza radiação para criar imagens em tempo real do interior do corpo, "
        "geralmente utilizado para visualizar os vasos sanguíneos. O número de vasos coloridos pode indicar a presença de obstruções ou problemas nos vasos, "
        "com um valor maior sugerindo um possível risco maior de doença cardíaca. Consulte um profissional de saúde para interpretação clínica precisa."
    )
    thal = forms.ChoiceField(
        label="Resultado do Teste de Thallium",
        choices=(
            (3, "Normal"),
            (6, "Defeito Fixo"),
            (7, "Defeito Reversível"),
        ),
        help_text="Resultado do teste de estresse com thallium. O teste de thallium, também conhecido como cintilografia miocárdica, é um exame que avalia o fluxo sanguíneo para o músculo cardíaco durante o repouso e o esforço físico. "
        "Os resultados podem ser classificados em três categorias: 'Normal' indica que o fluxo sanguíneo é adequado durante o repouso e o esforço; 'Defeito Fixo' indica uma redução no fluxo sanguíneo que é consistente durante repouso e esforço, "
        "indicando uma possível cicatriz cardíaca ou dano permanente; 'Defeito Reversível' indica uma redução no fluxo sanguíneo apenas durante o esforço, sugerindo um possível bloqueio temporário em uma artéria coronária. "
        "Consulte um profissional de saúde para interpretação clínica precisa dos resultados."
    )
