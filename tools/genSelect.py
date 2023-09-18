"""
 @功能描述： 根据剪切板中表格数据，批量生成select/union脚本，形成临时表数据
 @创建人:    tik.xie
 @创建日期： 2023-08-12
"""
import pandas as pd

# 为列数据添加后缀
def add_suffix(s):
    column_name = s.name
    if s.dtype == "object":  # 某列为字符串类型
        return s.apply(lambda x: f"'{x}' as {column_name},")
    else:
        return s.apply(lambda x: f"{x} as {column_name},")

def gen_select():

    df = pd.read_clipboard(header=0)
    df = df.apply(add_suffix)

    sql = "select "
    # 所有列都拼接成一个字符串列
    for col in df.columns:
        sql = sql + df[col]

    sql = sql.str[:-1] + " union all "
    sql.iloc[-1] = sql.iloc[-1].replace(" union all ", "")  # 处理最后一行

    sql.to_clipboard(index=False, header=False)  # 输出到剪切板

    return sql.to_string(index=False)