import openpyxl
from bs4 import BeautifulSoup
import requests
# 打开 Excel 文件
workbook = openpyxl.load_workbook('Articles2022.xlsx')

# 选择第一个工作表
worksheet = workbook.worksheets[0]

# 遍历每一行数据
for row in worksheet.iter_rows(min_row=2, values_only=True):
    # 生成文件
    with open(row[2]+'.mdx', 'w') as f:
        f.write('# '+row[2])
        f.write('\n')
        f.write('## 正文\n')
        f.write(BeautifulSoup(row[0], 'html.parser').get_text())


