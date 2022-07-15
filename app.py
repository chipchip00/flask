from flask import Flask, render_template
from main import find_product
from datetime import datetime
import pandas as pd
from flask import request
import os
from jinja2 import Template

app = Flask(__name__)
app.run(debug = True)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods = ['POST'])
def result():
    try: 
        file1 = request.files["file1"]
        path1 = os.path.join("upload/", file1.filename)
        file1.save(path1)
        file2 = request.files["file2"]
        path2 = os.path.join("upload/", file2.filename)
        file2.save(path2)

        start_date = request.form["start_date"]
        end_date = request.form["end_date"]

        df_hoadon = pd.read_excel(path1, index_col=False)
        df_cthd = pd.read_excel(path2, index_col=False)
        df_result = find_product(path1,path2,start_date, end_date)
        df_result["Thành tiền"] = df_result["Số lượng"]*df_result["Đơn giá"]
        return render_template('result.html', 
            product_info = df_result.to_html(index=False,classes="table table-dark"),
            hoadon = df_hoadon.to_html(index=False,classes="table table-dark"),
            cthd = df_cthd.to_html(index=False,classes="table table-dark")
        ) 
    except Exception as e:
        return render_template("index.html",error_mes = "Có lỗi xảy ra, vui lòng kiểm tra lại thông tin nhập!"+str(e))
