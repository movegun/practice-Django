import openpyxl
import pandas as pd
import numpy as np
import wordcloud

# [1] 2012년 엑셀파일 읽기
df_2012 = pd.read_excel("C:/Users/Kosmo/Desktop/파이썬데이터베이스자료실/excels/2012.xlsx", engine="openpyxl")

# [2] 데이터 확인
print("df_2012 :", df_2012)                   #(1) 읽혔는지 확인
print("df_2012.shape :", df_2012.shape)       #(2) 데이터의 ( 행 / 열 ) 갯수 확인 (41079, 15)
print("df_2012.count() :", df_2012.count())   #(3) 각 열마다 값이 채워져있는 행의 갯수 확인
#print("df_2012.dtypes :", df_2012.dtypes)     #(4) 각 열의 dtype 확인
print("df_2012.describe() \n:",df_2012.describe())
                                               #                     (3)      (4)
                                                    #시군구         41079    object
                                                    #번지           41079    object
                                                    #본번           41079    int64
                                                    #부번           41079    int64
                                                    #단지명         41079    object
                                                    #전용면적(㎡)    41079   float64
                                                    #계약년월        41079   int64
                                                    #계약일          41079   int64
                                                    #거래금액(만원)   41079  object
                                                    #층              41079   int64
                                                    #건축년도        41079   int64
                                                    #도로명          41079   object
                                                    #해제사유발생일     0    float64
                                                    #거래유형         41079  object
                                                    #중개사소재지     41079  object

# [3] 데이터 정제  
                                                  
# (1) 각 컬럼의 dtype을 알맞게 변경          계약년월/계약일/건축년도 필요하면 date타입으로 변경해야할듯
df_2012 =df_2012.astype({'계약년월':'object','계약일':'object','본번':'object','부번':'object','거래금액(만원)':'int64'})
#print("df_2012.dtypes :", df_2012.dtypes)

# 시각화

import matplotlib as mat
import matplotlib.pyplot as plt
mat.rcParams['font.family'] = 'Hancom Gothic'

#   층 - 매매가격
# print(df_2012.loc[df_2012['층']==-4])
# input()
# df = df_2012.groupby('층').mean()
# df = df.reset_index()
# df.plot(kind='bar',x='층',y='거래금액(만원)')
# plt.show()

#   층 - 거래량
# df_count = df_2012.groupby('층').count()
# df_count = df_count.reset_index()
# df_count = df_count.rename(columns={'시군구':'거래량'})
# df_count.plot(kind='bar' , x='층', y = '거래량')
#plt.show()

#   건축년도 - 매매가격
# df = df_2012.groupby('건축년도').mean()
# df = df.reset_index()
# df.plot(kind='bar',x='건축년도',y='거래금액(만원)')
# plt.show()

#   건축년도 - 거래량
# df = df_2012.groupby('건축년도').count()
# df = df.reset_index()
# df = df.rename(columns={'시군구':'거래량'})
# df.plot(kind='bar',x='건축년도',y='거래량')
# plt.show()


#   연도 - 매매가격
# df = df_2012.groupby('계약년월').mean()
# df = df.reset_index()
# df.plot(kind='bar',x='계약년월',y='거래금액(만원)')
# plt.show()

#   연도 - 거래량
# df = df_2012.groupby('계약년월').count()
# df = df.reset_index()
# df = df.rename(columns={'시군구':'거래량'})
# df.plot(kind='bar',x='계약년월',y='거래량')
# plt.show()

# 새로운 테이블 준비 (XX동 이 없는...)

#   지역구 - 매매가격
# df_n = df_2012
# for i,item in df_2012['시군구'].iteritems(): # 새로운 테이블 준비 (XX동 이 없는...)
#      df_n['시군구'][i] = item[6:9]
# df = df_n.groupby('시군구').mean()
# df = df.reset_index()
# df.plot(kind='bar',x='시군구',y='거래금액(만원)')
# plt.show()

#   지역구 - 거래량 
# df_n = df_2012
# for i,item in df_2012['시군구'].iteritems(): # 새로운 테이블 준비 (XX동 이 없는...)
#      df_n['시군구'][i] = item[6:9]
# df = df_n.groupby('시군구').count()
# df = df.reset_index()
# df = df.rename(columns={'번지':'거래량'})
# df.plot(kind='bar',x='시군구',y='거래량')
# plt.show()


from wordcloud import WordCloud

df_n = df_2012
for i,item in df_2012['시군구'].iteritems():
     df_n['시군구'][i] = item[6:9]
     
df = df_n.groupby('시군구').count()
df = df.reset_index()
print(df)

input("--------"*20)

df = df.rename(columns={'번지':'거래량'})
df = df.astype({'거래량':'float'})
print(df.set_index('시군구'))

input("--------"*20)
wc_dict = df.set_index('시군구').to_dict()['거래량']

print(df)

print(wc_dict)
input("--------"*20)
from wordcloud import WordCloud

wcwcwc = WordCloud(
     font_path="C:\Windows\Fonts\HANCOM GOTHIC BOLD.TTF",#폰트지정
     width=2000,#너비
     height=2000,#높이
     max_font_size=200,#빈도수 젤많이나온놈 사이즈
     background_color='white'#배경색
).generate_from_frequencies(wc_dict)# 워드클라우드 소스(dict형식)

plt.figure()
plt.imshow(wcwcwc)
plt.axis('off')
plt.show()