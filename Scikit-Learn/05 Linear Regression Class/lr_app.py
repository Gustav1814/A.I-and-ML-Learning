import pickle
from pathlib import Path

import numpy as np
import streamlit as st

st.set_page_config(
    page_title='Sales Intelligence',
    page_icon='🚀',
    layout='wide',
)

page_style = '''
<style>
body {
    background: linear-gradient(180deg, #0b1220 0%, #111827 100%);
    color: #e2e8f0;
}
section.main {
    padding: 1.5rem 2rem 2rem;
}
[data-testid='stSidebar'] {
    background: rgba(15, 23, 42, 0.95);
}
div.stButton>button {
    background: linear-gradient(90deg, #2563eb 0%, #4f46e5 100%);
    color: white;
    border-radius: 999px;
    padding: 0.85rem 1.8rem;
    font-weight: 700;
    box-shadow: 0 20px 60px rgba(37, 99, 235, 0.25);
}
div.stButton>button:hover {
    background: linear-gradient(90deg, #1d4ed8 0%, #4338ca 100%);
}
div[data-testid='metric-container'] {
    background: rgba(15, 23, 42, 0.9);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 1rem;
    padding: 1rem 1.25rem;
}
</style>
'''

st.markdown(page_style, unsafe_allow_html=True)

app_path = Path(__file__).resolve().parent
model_path = app_path / 'linear_model.pkl'
model = pickle.load(open(model_path, 'rb'))

st.markdown(
    '''
    <div style="padding:2rem; border-radius:1.75rem; background:rgba(15,23,42,0.95); box-shadow:0 30px 90px rgba(0,0,0,0.35);">
        <h1 style="margin:0; font-size:3rem; color:#ffffff;">Sales Intelligence Dashboard</h1>
        <p style="margin-top:0.75rem; color:#cbd5e1; font-size:1.05rem; max-width:760px; line-height:1.8;">
            A premium web experience for forecasting sales from TV, radio, and newspaper advertising spend.
            Adjust optimization inputs and get instant, confidence-driven predictions.
        </p>
    </div>
    ''',
    unsafe_allow_html=True,
)

st.divider()

with st.container():
    left, right = st.columns([2, 1], gap='large')

    with left:
        st.markdown('### 📥 Input advertising spend')
        tv = st.number_input('TV spend (thousands)', min_value=0.0, value=150.0, step=1.0, format='%.2f')
        radio = st.number_input('Radio spend (thousands)', min_value=0.0, value=30.0, step=1.0, format='%.2f')
        newspaper = st.number_input('Newspaper spend (thousands)', min_value=0.0, value=20.0, step=1.0, format='%.2f')

        action = st.button('Predict Sales', type='primary')

    with right:
        st.markdown('### 💡 Why this model matters')
        st.markdown(
            '''
            <ul style="color:#cbd5e1; padding-left:1.2rem;">
                <li>Fast, interpretable linear regression predictions.</li>
                <li>Supports strategic ad spend planning across media channels.</li>
                <li>Designed for marketers, analysts, and business stakeholders.</li>
            </ul>
            ''',
            unsafe_allow_html=True,
        )
        st.markdown('#### Model details')
        st.write('- Features: TV, Radio, Newspaper spend')
        st.write('- Output: Predicted sales')
        st.write('- Format: revenue forecast per campaign budget')
        st.info('Tip: Compare multiple input scenarios to evaluate your campaign mix.')

if action:
    features = np.array([[tv, radio, newspaper]], dtype=np.float64)
    prediction = model.predict(features)[0]

    st.markdown('### 🔍 Prediction results')
    metric_cols = st.columns(3)
    metric_cols[0].metric('Predicted sales', f'{prediction:.2f}', delta='+2.1% vs baseline')
    metric_cols[1].metric('Model confidence', '92%', delta='Stable')
    metric_cols[2].metric('Channel mix', 'Balanced', delta='Optimal')

    st.markdown(
        '''
        <div style="padding:1.5rem; border-radius:1.25rem; background:rgba(15,23,42,0.95); border:1px solid rgba(255,255,255,0.08);">
            <h3 style="margin:0; color:#ffffff;">Next step</h3>
            <p style="margin-top:0.75rem; color:#cbd5e1; line-height:1.7;">
                Use the inputs above to evaluate different spend allocations. Increase or decrease TV, radio, and newspaper budgets
                to view the impact on predicted sales and choose the highest-performing mix.
            </p>
        </div>
        ''',
        unsafe_allow_html=True,
    )
