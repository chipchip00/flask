from datetime import datetime
import numpy as np
import pandas as pd
import json

def find_product(path1, path2, start_date, end_date):
    df_hoadon = pd.read_excel(path1)
    df_ct_sanpham = pd.read_excel(path2)

    df_merge = pd.merge(left=df_hoadon, right=df_ct_sanpham, left_on='Mã sản phẩm', right_on='Mã sản phẩm')
    print (df_merge)
    df_merge_by_condition = df_merge[(df_merge["Ngày"]> start_date) & (df_merge["Ngày"]< end_date)]
    date_column_in_range = df_hoadon[(df_hoadon["Ngày"]> start_date) & (df_hoadon["Ngày"]< end_date)]
    last_data = date_column_in_range.tail(1)
    ma_sanpham = last_data["Mã sản phẩm"].values[0]

    # df_ctsp_by_ma = df_ct_sanpham[df_ct_sanpham["Mã sản phẩm"] == ma_sanpham]
    # response_data = {
    #     "ma" : ma_sanpham,
    #     "ten": last_data["Tên sản phẩm"].values[0],
    #     "date": last_data["Ngày"].dt.date.values[0],
    #     "so_luong": df_ctsp_by_ma["Số lượng"].values[0],
    #     "don_gia": df_ctsp_by_ma["Đơn giá"].values[0],
    #     "thanh_tien": df_ctsp_by_ma["Số lượng"].values[0]*df_ctsp_by_ma["Đơn giá"].values[0]
    # }
    # return response_data
    return (df_merge_by_condition)
if __name__ == "__main__":
    print(find_product("upload/Book1.xlsx","upload/Book2.xlsx",datetime(2019,1,1),datetime(2020,2,2)))
