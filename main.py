import streamlit as st


st.title('Streamlit 超入門')

st.write('ProgressBarの表示')
'start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i+1)
  time.sleep(0.01)

'DONE!!!'

left_column, right_column = st.beta_columns(2)
button = left_column.button('右に文字を表示')
if button:
  right_column.write('文字です')

expander = st.beta_expander('問い合わせ')
expander.write('問い合わせ内容を書く')

# option = st.text_input('あなたの趣味を教えてください。')
# condition = st.slider('あなたの今の調子は？',0,10,50)
# 'コンディション:', condition
# 'あなたの趣味：', option, 'です'

# if st.checkbox('Show Image'):
#   img = Image.open('0-1578977158.jpg')
#   st.image(img, caption='fruit', use_column_width=True)

# df = pd.DataFrame(
#   np.random.randn(100,2)/[50,50] + [35.69, 139.70],
#   columns=['lat','lon']
# )
# st.map(df)

#st.table(df.style.highlight_max(axis=0))




# dff = pd.DataFrame(
#       np.random.randn(50,20),
#       columns=('col %d' % i for i in range(20)))

# st.dataframe(dff)