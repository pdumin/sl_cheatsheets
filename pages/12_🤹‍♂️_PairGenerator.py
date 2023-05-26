import streamlit as st
from aux.random_people_choice import random_people_choice
import streamlit.components.v1 as components

st.header('Генератор команд')

teams = st.multiselect('Названия команд', [
    'pandas', 'matplotlib', 'seaborn', 
    'sklearn', 'CountVectorizer', 'TfIDFVectorizer',
    'LogRegression', 'Ridge', 'LASSO', 'ElasticNet',
    'Poisson', 'Bernoulli', 'Gauss',
    'XGBoost', 'LightGBM', 'CatBoost',
    'Dropout', 'Convolution','Linear',
    'GPT', 'BERT', 'LSTM', 'RNN', 'LSTM', 
    'ResNet', 'Inception', 'DenseNet', 
    'YOLO', 'FasterRCNN', 'SQL', 'PySpark'
])

names = st.radio(
            ' ', 
            [
                # 'Сиражудин, Мила, Семен, Анатолий, Гор, Матвей', 
                'Никита, Сева, Костя, Катя, Ваня, Рома',
                'Алексей, Аня, Галина, Владислав, Егор, Елена',
                'Александр М, Анна С, Анна Ф, Мария, Осана, Василий, \
                Вероника, Виктория, Иван, Ильвир'
                # add here more names as str
            ]
        )

gen_btn = st.button('Generate')
# print(labels)
st.markdown('---------')
if names and len(teams) != 0 and gen_btn:
    pairs = random_people_choice(names.split(','), teams)
    for team_name, names in pairs.items():
        st.markdown(f'__{team_name}__:  {(", ".join(names))}')

components.html(
    """
    <!-- Yandex.Metrika counter -->
<script type="text/javascript" >
   (function(m,e,t,r,i,k,a){m[i]=m[i]||function(){(m[i].a=m[i].a||[]).push(arguments)};
   m[i].l=1*new Date();
   for (var j = 0; j < document.scripts.length; j++) {if (document.scripts[j].src === r) { return; }}
   k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)})
   (window, document, "script", "https://mc.yandex.ru/metrika/tag.js", "ym");

   ym(92504528, "init", {
        clickmap:true,
        trackLinks:true,
        accurateTrackBounce:true,
        webvisor:true
   });
</script>
<noscript><div><img src="https://mc.yandex.ru/watch/92504528" style="position:absolute; left:-9999px;" alt="" /></div></noscript>
<!-- /Yandex.Metrika counter -->
""")
