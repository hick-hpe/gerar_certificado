# app.py
from flask import Flask, render_template, request, send_file
import pdfkit
import os
import base64
from datetime import datetime

app = Flask(__name__)

def imagem_para_base64(caminho):
    with open(caminho, 'rb') as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

def data_extenso(data:datetime):
    meses = [
        "Janeiro", "Fevereiro", "Março", "Abril",
        "Maio", "Junho", "Julho", "Agosto",
        "Setembro", "Outubro", "Novembro", "Dezembro"
    ]

    return f"{data.day} de {meses[data.month]} de {data.year}"

@app.route('/')
def index():
    return render_template('certificado_form.html')

@app.route('/gerar_certificado', methods=['POST'])
def gerar_certificado():
    nome = request.form['nome']
    # data = "2025-06-06"
    data_datetime = datetime.today()#datetime.strptime(data, "%Y-%m-%d")
    data_formatada = data_extenso(data_datetime)
    logo_path = os.path.join(os.getcwd(), 'static', 'logo.png')
    logo_base64 = imagem_para_base64(logo_path)
    percentual_acertos=80

    rendered = render_template('certificado_pdf.html',
                           nome=nome.upper(),
                           data=data_formatada,
                           logo_base64=logo_base64,
                           percentual_acertos=percentual_acertos)

    pdf_path = f'certificado_{nome.replace(" ", "_")}.pdf'
    pdfkit.from_string(rendered, pdf_path, options={'enable-local-file-access': ''})

    return send_file(pdf_path, as_attachment=True)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
    

